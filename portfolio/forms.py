from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['codename', 'specialization', 'level', 'bio', 'achievements', 'avatar']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'achievements': forms.Textarea(attrs={'rows': 4}),
        }