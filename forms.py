from django import forms
from .models import LocalAccount


class LocalAccountForm(forms.ModelForm):
    class Meta:
        model = LocalAccount
        fields = ["role", "code", "username", "email", "password"]
