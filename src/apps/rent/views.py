from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Prefetch

from src.apps.user.models import CustomUser
from src.apps.rent.models import Console, ConsoleRent
from src.apps.rent.forms import RentConsoleForm


def rent_list(request: WSGIRequest):
    return render(request, "rent/rent_list.html")


def rent_order_list(request: WSGIRequest):
    contex = {}
    console_rent_qs = ConsoleRent.objects.select_related("console")
    user = CustomUser.objects.prefetch_related(
        Prefetch(
            "rented_consoles", queryset=console_rent_qs, to_attr="console_orders"
        )
    ).filter(pk=request.user.id)[0]
    contex["console_orders"] = user.console_orders
    return render(request, "rent/orders/rent_order_list.html", contex)


def console_list(request: WSGIRequest):
    contex = {}
    consoles = Console.objects.all()
    form = RentConsoleForm()
    contex["consoles"] = consoles
    contex["form"] = form
    return render(request, "rent/console/console_list.html", contex)


def rent_console(request: WSGIRequest):
    contex = {}
    console_name = request.POST.get("console")
    console = Console.objects.get(name=console_name)
    days = int(request.POST.get("days"))
    comment = request.POST.get("comment")
    ConsoleRent.objects.create(user=request.user, console=console, days=days, comment=comment)
    return redirect("console_list")
