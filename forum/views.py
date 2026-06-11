# forum/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse
from .models import ForumTopic
from .forms import ForumTopicForm
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

class ForumTopicCreateView(LoginRequiredMixin, CreateView):
    model = ForumTopic
    form_class = ForumTopicForm
    template_name = 'forum/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('forum:topic_detail', kwargs={'pk': self.object.pk})
