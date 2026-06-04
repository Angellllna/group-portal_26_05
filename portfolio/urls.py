from django.urls import path
from .views import PortfolioListView, PortfolioDetailView

app_name = "portfolio"

urlpatterns = [
    path("", PortfolioListView.as_view(), name="list"),
    path("<int:id>/", PortfolioDetailView.as_view(), name="detail"),
]
