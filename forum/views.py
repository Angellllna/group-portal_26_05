# forum/views.py
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ForumTopic
from .forms import ForumTopicForm, ForumCommentForm


class ForumTopicListView(ListView):
    model = ForumTopic
    template_name = "forum/list.html"
    context_object_name = "topics"


class ForumTopicDetailView(FormMixin, DetailView):
    model = ForumTopic
    template_name = "forum/detail.html"
    context_object_name = "topic"
    form_class = ForumCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse('admin:login')}?next={request.path}")

        self.object = self.get_object()

        if self.object.is_closed:
            return self.get(request, *args, **kwargs)

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.topic = self.object
        comment.author = self.request.user
        comment.save()
        return redirect(reverse('forum:topic_detail', kwargs={'pk': self.object.pk}))


class ForumTopicCreateView(LoginRequiredMixin, CreateView):
    model = ForumTopic
    form_class = ForumTopicForm
    template_name = 'forum/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('forum:topic_detail', kwargs={'pk': self.object.pk})