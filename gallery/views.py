from django.views.generic import ListView, DetailView
from .models import MediaItem


class MediaListView(ListView):
    model = MediaItem
    template_name = "gallery/list.html"
    context_object_name = "media_items"
    paginate_by = 12

    def get_queryset(self):
        return (
            MediaItem.objects.filter(is_approved=True)
            .select_related("author")
            .order_by("-created_at")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["media_type_filter"] = self.request.GET.get("type", "")
        context["media_types"] = MediaItem.MediaType.choices
        return context


class MediaDetailView(DetailView):
    model = MediaItem
    template_name = "gallery/detail.html"
    context_object_name = "item"
    pk_url_kwarg = "id"

    def get_queryset(self):
        return MediaItem.objects.filter(is_approved=True).select_related("author")