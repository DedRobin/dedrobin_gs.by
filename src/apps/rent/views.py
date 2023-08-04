from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required

from src.apps.rent.services import create_console_order, create_room_order, create_club_order, get_console_order_list, \
    get_club_order_list, get_room_order_list
from src.apps.rent.models import Console, Club, Room
from src.apps.rent.forms import RentConsoleForm, RentRoomForm, RentClubForm, ConsoleFilterForm


def console_list(request: WSGIRequest, contex: dict = None):
    if contex is None:
        contex = {}
    consoles = Console.objects.all()
    form = RentConsoleForm()
    contex["consoles"] = consoles
    contex["form"] = form
    return render(request, "rent/console/console_list.html", contex)


@login_required(redirect_field_name="", login_url="login")
def rent_console(request: WSGIRequest):
    console_order, errors = create_console_order(request)
    if errors:
        contex = dict(errors=errors)
    else:
        notification = "The console order №{0} was created successfully".format(console_order.id)
        contex = dict(notification=notification)
    render_obj = console_list(request, contex)
    return render_obj


def room_list(request: WSGIRequest, contex: dict = None):
    if contex is None:
        contex = {}
    rooms = Room.objects.all()
    form = RentRoomForm()
    contex["rooms"] = rooms
    contex["form"] = form
    return render(request, "rent/rooms/room_list.html", contex)


@login_required(redirect_field_name="", login_url="login")
def rent_room(request: WSGIRequest):
    room_order, errors = create_room_order(request)
    if errors:
        contex = dict(errors=errors)
    else:
        notification = "The room order №{0} was created successfully".format(room_order.id)
        contex = dict(notification=notification)
    render_obj = room_list(request, contex)
    return render_obj


def club_list(request: WSGIRequest, contex: dict = None):
    if contex is None:
        contex = {}
    clubs = Club.objects.all()
    form = RentClubForm()
    contex["clubs"] = clubs
    contex["form"] = form
    return render(request, "rent/clubs/club_list.html", contex)


@login_required(redirect_field_name="", login_url="login")
def rent_club(request: WSGIRequest):
    club_order, errors = create_club_order(request)
    if errors:
        contex = dict(errors=errors)
    else:
        notification = "The club order №{0} was created successfully".format(club_order.id)
        contex = dict(notification=notification)
    render_obj = room_list(request, contex)
    return render_obj


@login_required(redirect_field_name="", login_url="login")
def console_order_list(request: WSGIRequest):
    contex = {}
    console_filter_form = ConsoleFilterForm(request.GET)
    console_orders = get_console_order_list(request)
    contex["console_orders"] = console_orders
    contex["console_filter_form"] = console_filter_form
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
