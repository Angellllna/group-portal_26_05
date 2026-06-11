from django import forms
from .models import Grade


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["student", "subject", "score", "comment"]
        labels = {
            "student": "Курсант",
            "subject": "Навчальний напрямок",
            "score": "Бал",
            "comment": "Коментар",
        }
        widgets = {
            "comment": forms.TextInput(attrs={"placeholder": "За що виставлена оцінка..."}),
            "score": forms.NumberInput(attrs={"min": 1, "max": 12}),
        }
