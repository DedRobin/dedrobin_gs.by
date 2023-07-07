from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from src.apps.console.models import Console


def console_list(request: WSGIRequest):
    contex = {}
    consoles = Console.objects.all()
    contex["consoles"] = consoles
    return render(request, "console_list.html", contex)
