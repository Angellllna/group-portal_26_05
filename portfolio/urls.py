from django.urls import path
from .views import PortfolioListView, PortfolioDetailView, PortfolioUpdateView

app_name = "portfolio"

urlpatterns = [
    path("", PortfolioListView.as_view(), name="list"),
    path("<int:id>/", PortfolioDetailView.as_view(), name="detail"),
    path("edit/", PortfolioUpdateView.as_view(), name="edit"),
]
