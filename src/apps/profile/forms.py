from django import forms

from src.apps.profile.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ("user", "photo")
        widgets = {"birthday": forms.DateInput(attrs={"type": "date"})}
