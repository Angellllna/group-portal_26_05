from django import forms
from .models import MediaItem


class MediaItemForm(forms.ModelForm):
    class Meta:
        model = MediaItem
        fields = ["title", "description", "file", "media_type", "action_name"]
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Введіть назву матеріалу",
                "autocomplete": "off",
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Короткий опис (необов'язково)...",
                "rows": 4,
            }),
            "media_type": forms.Select(),
            "action_name": forms.TextInput(attrs={
                "placeholder": "Наприклад: Пограбування банку, Зачистка сліду...",
                "autocomplete": "off",
            }),
            "file": forms.ClearableFileInput(attrs={
                "accept": "image/*,video/*",
            }),
        }
        labels = {
            "title": "Назва",
            "description": "Опис",
            "file": "Файл",
            "media_type": "Тип медіа",
            "action_name": "Назва події",
        }
        error_messages = {
            "title": {"required": "Назва обов'язкова."},
            "file": {"required": "Будь ласка, додайте файл."},
            "action_name": {"required": "Вкажіть назву."},
        }