from django.views.generic import ListView, DetailView

from .models import ForumTopic


class ForumTopicListView(ListView):
    model = ForumTopic
    template_name = "forum/list.html"
    context_object_name = "topics"


class ForumTopicDetailView(DetailView):
    model = ForumTopic
    template_name = "forum/detail.html"
    context_object_name = "topic"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()
        return context
