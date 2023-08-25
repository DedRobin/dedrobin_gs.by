from django import forms

from src.apps.profile.models import Profile
from src.apps.profile.validators import check_phone_number


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ("user", "photo")
        widgets = {"birthday": forms.DateInput(attrs={"type": "date"})}


class OrderProfileForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    phone_number = forms.CharField(max_length=150, validators=[check_phone_number])
