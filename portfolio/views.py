from django.views.generic import ListView, DetailView
from .models import Portfolio


class PortfolioListView(ListView):
    model = Portfolio
    template_name = "portfolio/list.html"
    context_object_name = "portfolios"
    ordering = ["-level", "codename"]


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "portfolio/detail.html"
    context_object_name = "portfolio"
    pk_url_kwarg = "id"
