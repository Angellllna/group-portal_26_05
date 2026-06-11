from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import MediaItemForm
from .models import MediaItem


class MediaListView(ListView):
    model = MediaItem
    template_name = "gallery/list.html"
    context_object_name = "media_items"
    paginate_by = 12

    def get_queryset(self):
        qs = (
            MediaItem.objects.filter(is_approved=True)
            .select_related("author")
        )

        media_type = self.request.GET.get("type", "")
        if media_type:
            qs = qs.filter(media_type=media_type)

        category = self.request.GET.get("category", "")
        if category:
            qs = qs.filter(category=category)

        search = self.request.GET.get("q", "").strip()
        if search:
            qs = qs.filter(
                Q(title__icontains=search) |
                Q(action_name__icontains=search)
            )

        sort = self.request.GET.get("sort", "-created_at")
        allowed_sorts = {
            "-created_at": "-created_at",
            "created_at": "created_at",
            "title": "title",
            "-title": "-title",
        }
        qs = qs.order_by(allowed_sorts.get(sort, "-created_at"))

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["media_type_filter"] = self.request.GET.get("type", "")
        context["category_filter"] = self.request.GET.get("category", "")
        context["search_query"] = self.request.GET.get("q", "")
        context["sort"] = self.request.GET.get("sort", "-created_at")
        context["media_types"] = MediaItem.MediaType.choices
        context["categories"] = MediaItem.Category.choices
        context["sort_options"] = [
            ("-created_at", "Нові спочатку"),
            ("created_at", "Старі спочатку"),
            ("title", "Назва А→Я"),
            ("-title", "Назва Я→А"),
        ]
        return context


class MediaDetailView(DetailView):
    model = MediaItem
    template_name = "gallery/detail.html"
    context_object_name = "item"
    pk_url_kwarg = "id"

    def get_queryset(self):
        return MediaItem.objects.filter(is_approved=True).select_related("author")


class MediaUploadView(LoginRequiredMixin, CreateView):
    model = MediaItem
    form_class = MediaItemForm
    template_name = "gallery/upload.html"
    success_url = reverse_lazy("gallery:list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(
            self.request,
            "Матеріал успішно завантажено і очікує підтвердження модератором.",
        )
        return super().form_valid(form)