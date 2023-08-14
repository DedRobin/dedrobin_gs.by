from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required

from src.apps.rent.services import create_console_order, create_room_order, create_club_order, get_order_list_by_filter
from src.apps.rent.models import Console, Club, Room, ConsoleRent, ClubRent, RoomRent
from src.apps.rent.forms import RentConsoleForm, RentRoomForm, RentClubForm, RentFilterForm


def console_list(request: WSGIRequest, contex: dict = None):
    if contex is None:
        contex = {}
    consoles = Console.objects.all()
    form = RentConsoleForm()
    contex["consoles"] = consoles
    contex["form"] = form
    status = contex.get("status")
    return render(request, "rent/console/console_list.html", contex, status=status)


@login_required(redirect_field_name="", login_url="login")
def rent_console(request: WSGIRequest):
    console_order, errors = create_console_order(request)
    if errors:
        contex = dict(errors=errors)
    else:
        notification = "The console order №{0} was created successfully".format(console_order.id)
        contex = dict(notification=notification)
        contex["status"] = 201
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
        contex["status"] = 201
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
        contex["status"] = 201
    render_obj = room_list(request, contex)
    return render_obj


@login_required(redirect_field_name="", login_url="login")
def console_order_list(request: WSGIRequest):
    contex = {}
    filter_form = RentFilterForm(request.GET)
    console_orders = get_order_list_by_filter(request=request, model=ConsoleRent)
    contex["console_orders"] = console_orders
    contex["filter_form"] = filter_form
    return render(request, "rent/orders/consoles/console_order_list.html", contex)


@login_required(redirect_field_name="", login_url="login")
def club_order_list(request: WSGIRequest):
    contex = {}
    filter_form = RentFilterForm(request.GET)
    club_orders = get_order_list_by_filter(request=request, model=ClubRent)
    contex["club_orders"] = club_orders
    contex["filter_form"] = filter_form
    return render(request, "rent/orders/clubs/club_order_list.html", contex)


@login_required(redirect_field_name="", login_url="login")
def room_order_list(request: WSGIRequest):
    contex = {}
    filter_form = RentFilterForm(request.GET)
    room_orders = get_order_list_by_filter(request=request, model=RoomRent)
    contex["room_orders"] = room_orders
    contex["filter_form"] = filter_form
    return render(request, "rent/orders/rooms/room_order_list.html", contex)
