from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest

from src.apps.console.models import Console
from src.apps.console.forms import RentConsoleForm


def console_list(request: WSGIRequest):
    contex = {}
    consoles = Console.objects.all()
    form = RentConsoleForm()
    contex["consoles"] = consoles
    contex["form"] = form
    if request.method == "POST":
        if request.user.is_authenticated:
            days = request.POST.get("days")
            print("RENT")
        else:
            return redirect("login")
    return render(request, "console_list.html", contex)
