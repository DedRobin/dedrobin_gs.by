from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest

from src.apps.rent.models import Console, ConsoleRent
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


def rent_console(request: WSGIRequest):
    contex = {}
    console_name = request.POST.get("console")
    console = Console.objects.get(name=console_name)
    days = int(request.POST.get("days"))
    comment = request.POST.get("comment")
    ConsoleRent.objects.create(user=request.user, console=console, days=days, comment=comment)
    return redirect("console_list")
