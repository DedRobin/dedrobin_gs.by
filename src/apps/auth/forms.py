from django import forms
from src.apps.user.models import CustomUser


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "password")