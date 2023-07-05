from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def rent(request: WSGIRequest):
    return render(request, "rent.html")
