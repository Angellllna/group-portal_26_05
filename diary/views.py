from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Avg, Max, Count
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import GradeForm
from .models import Grade, TrainingSubject

User = get_user_model()


class StaffOrInstructorMixin(UserPassesTestMixin):
    """Дозволяє доступ тільки staff/admin або користувачам з роллю instructor."""

    def test_func(self):
        user = self.request.user
        if user.is_staff:
            return True
        try:
            return user.profile.role == "instructor"
        except Exception:
            return False


class GradeListView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = "diary/list.html"
    context_object_name = "grades"

    def _is_privileged(self):
        user = self.request.user
        if user.is_staff:
            return True
        try:
            return user.profile.role == "instructor"
        except Exception:
            return False

    def get_queryset(self):
        qs = Grade.objects.select_related("student", "subject", "teacher")

        if self._is_privileged():
            # Фільтр по курсанту (тільки для staff/admin/instructor)
            student_id = self.request.GET.get("student")
            if student_id:
                qs = qs.filter(student_id=student_id)
        else:
            qs = qs.filter(student=self.request.user)

        # Фільтр по навчальному напрямку (для всіх)
        subject_id = self.request.GET.get("subject")
        if subject_id:
            qs = qs.filter(subject_id=subject_id)

        return qs.order_by("-created_at")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user
        privileged = self._is_privileged()

        # Базовий queryset для статистики
        if privileged:
            student_id = self.request.GET.get("student")
            stat_qs = Grade.objects.all()
            if student_id:
                stat_qs = stat_qs.filter(student_id=student_id)
        else:
            stat_qs = Grade.objects.filter(student=user)

        subject_id = self.request.GET.get("subject")
        if subject_id:
            stat_qs = stat_qs.filter(subject_id=subject_id)

        # Статистика
        agg = stat_qs.aggregate(
            count=Count("id"),
            avg=Avg("score"),
            best=Max("score"),
        )
        ctx["stat_count"] = agg["count"] or 0
        ctx["stat_avg"] = round(agg["avg"], 1) if agg["avg"] else "—"
        ctx["stat_best"] = agg["best"] or "—"

        # Дані для фільтрів
        ctx["subjects"] = TrainingSubject.objects.all()
        ctx["selected_subject"] = self.request.GET.get("subject", "")
        ctx["privileged"] = privileged

        if privileged:
            ctx["students"] = User.objects.all().order_by("username")
            ctx["selected_student"] = self.request.GET.get("student", "")

        return ctx


class GradeCreateView(LoginRequiredMixin, StaffOrInstructorMixin, CreateView):
    model = Grade
    form_class = GradeForm
    template_name = "diary/add.html"
    success_url = reverse_lazy("diary:list")

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)
