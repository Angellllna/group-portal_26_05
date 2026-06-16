from django import forms
from .models import Profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("codename", "bio")
        widgets = {
            "codename": forms.TextInput(attrs={"placeholder": "e.g. Ghost, Cipher, Nova"}),
            "bio":      forms.Textarea(attrs={"rows": 4, "placeholder": "Tell something about yourself..."}),
        }