from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import logout

from src.apps.user.services import check_passwords_and_create_user, user_authentication_and_login
from src.apps.user.forms import LoginForm, RegistrationForm


def register_user(request: WSGIRequest):
    contex = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            error, user_created = check_passwords_and_create_user(form.cleaned_data)
            if user_created and not error:
                return redirect("login")
            else:
                contex["error"] = error
        else:
            contex["error"] = form.errors
    form = RegistrationForm()
    contex["form"] = form
    return render(request, "registration.html", contex)


def login_user(request: WSGIRequest):
    contex = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            error, user_is_auth_and_login = user_authentication_and_login(request=request, data=form.cleaned_data)
            if not error and user_is_auth_and_login:
                return redirect("index")
            else:
                contex["error"] = error
        else:
            contex["error"] = form.errors

    form = LoginForm()
    contex["form"] = form
    return render(request, "login.html", contex)


def logout_user(request: WSGIRequest):
    logout(request)
    return redirect("login")
