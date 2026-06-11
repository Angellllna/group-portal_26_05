from django.urls import path
from .views import ForumTopicCreateView
from .views import ForumTopicListView, ForumTopicDetailView

app_name = "forum"

urlpatterns = [
    path("", ForumTopicListView.as_view(), name="topic_list"),
    path("<int:pk>/", ForumTopicDetailView.as_view(), name="topic_detail"),
    path('create/', ForumTopicCreateView.as_view(), name='topic_create'),
]
