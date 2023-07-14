from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required

from src.apps.rent.services import create_console_order, create_room_order, create_club_order, get_console_order_list, \
    get_club_order_list, get_room_order_list
from src.apps.rent.models import Console, Club, Room
from src.apps.rent.forms import RentConsoleForm, RentRoomForm, RentClubForm


def console_list(request: WSGIRequest):
    contex = {}
    consoles = Console.objects.all()
    form = RentConsoleForm()
    contex["consoles"] = consoles
    contex["form"] = form
    return render(request, "rent/console/console_list.html", contex)


@login_required(redirect_field_name="", login_url="login")
def rent_console(request: WSGIRequest):
    create_console_order(request)
    return redirect("console_list")


def room_list(request: WSGIRequest):
    contex = {}
    rooms = Room.objects.all()
    form = RentRoomForm()
    contex["rooms"] = rooms
    contex["form"] = form
    return render(request, "rent/rooms/room_list.html", contex)


@login_required(redirect_field_name="", login_url="login")
def rent_room(request: WSGIRequest):
    create_room_order(request)
    return redirect("room_list")


def club_list(request: WSGIRequest):
    contex = {}
    clubs = Club.objects.all()
    form = RentClubForm()
    contex["clubs"] = clubs
    contex["form"] = form
    return render(request, "rent/clubs/club_list.html", contex)


@login_required(redirect_field_name="", login_url="login")
def rent_club(request: WSGIRequest):
    create_club_order(request)
    return redirect("club_list")


@login_required(redirect_field_name="", login_url="login")
def console_order_list(request: WSGIRequest):
    contex = {}
    console_orders = get_console_order_list(request)
    contex["console_orders"] = console_orders
    return render(request, "rent/orders/consoles/console_order_list.html", contex)


@login_required(redirect_field_name="", login_url="login")
def club_order_list(request: WSGIRequest):
    contex = {}
    club_orders = get_club_order_list(request)
    contex["club_orders"] = club_orders
    return render(request, "rent/orders/clubs/club_order_list.html", contex)


@login_required(redirect_field_name="", login_url="login")
def room_order_list(request: WSGIRequest):
    contex = {}
    room_orders = get_room_order_list(request)
    contex["room_orders"] = room_orders
    return render(request, "rent/orders/rooms/room_order_list.html", contex)
