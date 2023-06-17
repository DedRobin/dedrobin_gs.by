from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())


class RegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", min_length=8, widget=forms.PasswordInput())
    password2 = forms.CharField(label="Password confirmation", min_length=8, widget=forms.PasswordInput())


class UserForm(RegistrationForm):
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    password1 = forms.CharField(
        label="Password", min_length=8, required=False, widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label="Password confirmation", required=False, min_length=8, widget=forms.PasswordInput()
    )
