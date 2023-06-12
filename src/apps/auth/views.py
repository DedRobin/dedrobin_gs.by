from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse

from src.apps.auth.forms import LoginForm


def login_user(request: WSGIRequest):
    contex = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request=request, **form.cleaned_data)
            if user is None:
                contex["error"] = "The user does not exist"
            else:
                login(request, user)
                return redirect("index")
        else:
            contex["error"] = form.errors

    form = LoginForm()
    contex["form"] = form
    return render(request, "login.html", contex)


def logout_user(request: WSGIRequest):
    logout(request)
    return redirect("login")
