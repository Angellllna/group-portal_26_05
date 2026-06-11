from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import GradeForm
from .models import Grade


class StaffOrInstructorMixin(UserPassesTestMixin):
    """Дозволяє доступ тільки staff/admin або користувачам з роллю instructor."""

    def test_func(self):
        user = self.request.user
        if user.is_staff:
            return True
        # Перевіряємо роль через profile (accounts app)
        try:
            return user.profile.role == "instructor"
        except Exception:
            return False


class GradeListView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = "diary/list.html"
    context_object_name = "grades"

    def get_queryset(self):
        qs = Grade.objects.select_related("student", "subject", "teacher")
        if self.request.user.is_staff:
            return qs
        try:
            if self.request.user.profile.role == "instructor":
                return qs
        except Exception:
            pass
        return qs.filter(student=self.request.user)


class GradeCreateView(LoginRequiredMixin, StaffOrInstructorMixin, CreateView):
    model = Grade
    form_class = GradeForm
    template_name = "diary/add.html"
    success_url = reverse_lazy("diary:list")

    def form_valid(self, form):
        # Автоматично встановлюємо teacher як поточного користувача
        form.instance.teacher = self.request.user
        return super().form_valid(form)
