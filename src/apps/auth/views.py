from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from src.apps.auth.forms import LoginForm


def login(request: WSGIRequest):
    form = LoginForm()
    data = {
        "form": form,
    }
    return render(request, "login.html", data)
