# forum/forms.py
from django import forms
from .models import ForumTopic

class ForumTopicForm(forms.ModelForm):
    class Meta:
        model = ForumTopic
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть назву теми'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Опишіть вашу тему тут...', 'rows': 5}),
        }