from django import forms

from .models import ForumTopic, ForumComment


class ForumCommentForm(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ваш коментар...', 'rows': 3}),
        }
        labels = {
            'content': 'коментар',
        }


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
