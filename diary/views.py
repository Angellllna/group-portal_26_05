from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Grade


class GradeListView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = "diary/list.html"
    context_object_name = "grades"

    def get_queryset(self):
        qs = Grade.objects.select_related("student", "subject", "teacher")
        if self.request.user.is_staff:
            return qs
        return qs.filter(student=self.request.user)
