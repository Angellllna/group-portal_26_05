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

    def clean_score(self):
        score = self.cleaned_data["score"]
        if not 1 <= score <= 12:
            raise forms.ValidationError("Бал має бути в межах від 1 до 12.")
        return score
