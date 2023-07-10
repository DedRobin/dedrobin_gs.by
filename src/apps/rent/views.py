from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from src.apps.rent.models import Console
from src.apps.rent.forms import RentConsoleForm


def rent_list(request: WSGIRequest):
    return render(request, "rent_list.html")


def console_list(request: WSGIRequest):
    contex = {}
    consoles = Console.objects.all()
    form = RentConsoleForm()
    contex["consoles"] = consoles
    contex["form"] = form
    return render(request, "console/console_list.html", contex)
