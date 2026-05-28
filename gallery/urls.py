from django.urls import path
from .views import MediaListView, MediaDetailView

app_name = "gallery"

urlpatterns = [
    path("", MediaListView.as_view(), name="list"),
    path("<int:id>/", MediaDetailView.as_view(), name="detail"),
]