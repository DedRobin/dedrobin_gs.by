from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def login(request: WSGIRequest):
    print("index.html")
    return render(request, "index.html")
