from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView

from .models import Portfolio
from .forms import PortfolioForm


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


class PortfolioUpdateView(LoginRequiredMixin, UpdateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = "portfolio/edit.html"


    def get_object(self, queryset=None):
        portfolio, _ = Portfolio.objects.get_or_create(
            user=self.request.user,
            defaults={
                "codename": self.request.user.username,
                "specialization": "gunsmith",
                "level": 1,
            }
        )

        return portfolio


    def get_success_url(self):
        return reverse("portfolio:detail", kwargs={"id": self.object.id})
