from django.contrib import admin
from .models import MediaItem


@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "media_type",
        "game_name",
        "is_approved",
        "created_at",
    )
    list_filter = ("is_approved", "media_type", "game_name")
    list_editable = ("is_approved",)
    search_fields = ("title", "description", "game_name", "author__username")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)

    fieldsets = (
        (
            "Основна інформація",
            {
                "fields": ("author", "title", "description", "game_name"),
            },
        ),
        (
            "Медіа",
            {
                "fields": ("file", "media_type"),
            },
        ),
        (
            "Статус",
            {
                "fields": ("is_approved", "created_at"),
            },
        ),
    )