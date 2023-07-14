from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Prefetch

from src.apps.user.models import CustomUser
from src.apps.rent.models import Console, ConsoleRent, Club, ClubRent, Room, RoomRent
from src.apps.rent.forms import RentConsoleForm, RentRoomForm


def rent_list(request: WSGIRequest):
    return render(request, "rent/rent_list.html")


def console_list(request: WSGIRequest):
    contex = {}
    consoles = Console.objects.all()
    form = RentConsoleForm()
    contex["consoles"] = consoles
    contex["form"] = form
    return render(request, "rent/console/console_list.html", contex)


def rent_console(request: WSGIRequest):
    console_name = request.POST.get("console")
    console = Console.objects.get(name=console_name)
    days = int(request.POST.get("days"))
    comment = request.POST.get("comment")
    ConsoleRent.objects.create(user=request.user, console=console, days=days, comment=comment)
    return redirect("console_list")


def room_list(request: WSGIRequest):
    contex = {}
    rooms = Room.objects.all()
    form = RentRoomForm()
    contex["rooms"] = rooms
    contex["form"] = form
    return render(request, "rent/rooms/room_list.html", contex)


def rent_room(request: WSGIRequest):
    room_name = request.POST.get("room")
    room = Room.objects.get(name=room_name)
    comment = request.POST.get("comment")
    RoomRent.objects.create(user=request.user, room=room, comment=comment)
    return redirect("room_list")


def console_order_list(request: WSGIRequest):
    contex = {}
    console_rent_qs = ConsoleRent.objects.select_related("console")
    user = CustomUser.objects.prefetch_related(
        Prefetch(
            "rented_consoles", queryset=console_rent_qs, to_attr="console_orders"
        )
    ).filter(pk=request.user.id)[0]
    contex["console_orders"] = user.console_orders
    return render(request, "rent/orders/consoles/console_order_list.html", contex)


def club_order_list(request: WSGIRequest):
    contex = {}
    club_rent_qs = ClubRent.objects.select_related("club")
    user = CustomUser.objects.prefetch_related(
        Prefetch(
            "rented_clubs", queryset=club_rent_qs, to_attr="club_orders"
        )
    ).filter(pk=request.user.id)[0]
    contex["club_orders"] = user.club_orders
    return render(request, "rent/orders/clubs/club_order_list.html", contex)


def room_order_list(request: WSGIRequest):
    contex = {}
    club_rent_qs = RoomRent.objects.select_related("room")
    user = CustomUser.objects.prefetch_related(
        Prefetch(
            "rented_rooms", queryset=club_rent_qs, to_attr="room_orders"
        )
    ).filter(pk=request.user.id)[0]
    contex["room_orders"] = user.room_orders
    return render(request, "rent/orders/rooms/room_order_list.html", contex)
