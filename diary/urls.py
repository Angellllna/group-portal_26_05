from django.urls import path

from .views import GradeListView, GradeCreateView

app_name = "diary"

urlpatterns = [
    path("", GradeListView.as_view(), name="list"),
    path("add/", GradeCreateView.as_view(), name="add"),
]
