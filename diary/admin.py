from django.contrib import admin
from .models import Grade, TrainingSubject


@admin.register(TrainingSubject)
class TrainingSubjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at")
    search_fields = ("title",)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "subject",
        "score",
        "teacher",
        "created_at",
    )
    list_filter = ("subject", "teacher", "created_at")
    search_fields = (
        "student__username",
        "comment",
    )
    list_select_related = ("student", "subject", "teacher")
