# forum/urls.py
from django.urls import path
from .views import ForumTopicListView, ForumTopicDetailView

app_name = 'forum'

urlpatterns = [
    path('', ForumTopicListView.as_view(), name='topic_list'),
    path('<int:pk>/', ForumTopicDetailView.as_view(), name='topic_detail'),
]