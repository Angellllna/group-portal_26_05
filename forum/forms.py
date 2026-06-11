from django import forms

from .models import ForumTopic


class ForumTopicForm(forms.ModelForm):
    class Meta:
        model = ForumTopic
        fields = ["title", "content"]
        labels = {
            "title": "Назва теми",
            "content": "Зміст",
        }
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Введіть назву теми"}),
            "content": forms.Textarea(attrs={"placeholder": "Опишіть вашу тему тут...", "rows": 5}),
        }
