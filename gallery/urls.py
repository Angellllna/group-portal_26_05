from django.urls import path
from .views import MediaListView, MediaDetailView, MediaUploadView

app_name = "gallery"

urlpatterns = [
    path("", MediaListView.as_view(), name="list"),
    path("upload/", MediaUploadView.as_view(), name="upload"),
    path("<int:id>/", MediaDetailView.as_view(), name="detail"),
]