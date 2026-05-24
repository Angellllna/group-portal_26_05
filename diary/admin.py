from django.contrib import admin
from .models import Grade, Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "subject",
        "grade",
        "comment",
        "date_issued",
        "issued_by",
    )
    list_filter = ("subject", "student", "date_issued")
    search_fields = (
        "student__username",
        "student__first_name",
        "student__last_name",
        "comment",
    )
    date_hierarchy = "date_issued"
    autocomplete_fields = ["student", "issued_by"]
    list_select_related = ("student", "subject", "issued_by")
