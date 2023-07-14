from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def product_list(request: WSGIRequest):
    return render(request, "product_list.html")
