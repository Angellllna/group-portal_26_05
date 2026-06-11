from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display   = ("codename", "user", "role", "created_at", "updated_at")
    list_filter    = ("role",)
    search_fields  = ("codename", "user__username")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Identity", {
            "fields": ("user", "codename", "role"),
        }),
        ("Details", {
            "fields": ("bio",),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )