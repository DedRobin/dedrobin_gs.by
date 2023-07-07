from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def rent_list(request: WSGIRequest):
    return render(request, "rent_list.html")
