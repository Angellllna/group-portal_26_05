from django.shortcuts import render

from gallery.models import MediaItem


def home(request):
    gallery_preview = (
        MediaItem.objects.filter(is_approved=True)
        .select_related("author")
        .order_by("-created_at")[:4]
    )
    return render(request, "core/home.html", {"gallery_preview": gallery_preview})
