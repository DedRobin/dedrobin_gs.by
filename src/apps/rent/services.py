from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Prefetch
from django.db.models.query import QuerySet
from django.http.request import QueryDict

from src.apps.rent.forms import RentRoomForm, RentConsoleForm
from src.apps.user.models import CustomUser
from src.apps.rent.models import Console, ConsoleRent, Club, ClubRent, Room, RoomRent


def _add_filter(queryset: QuerySet, filter_query_dict: QueryDict) -> QuerySet:
    if filter_query_dict.get("is_completed") == "yes":
        queryset = queryset.filter(is_completed=True)
    elif filter_query_dict.get("is_completed") == "no":
        queryset = queryset.filter(is_completed=False)
    if filter_query_dict.get("order_by_creation_date") == "asc":
        queryset = queryset.order_by("created_at")
    elif filter_query_dict.get("order_by_creation_date") == "desc":
        queryset = queryset.order_by("-created_at")
    if filter_query_dict.get("order_by_completed_date") == "asc":
        queryset = queryset.order_by("completed_date")
    elif filter_query_dict.get("order_by_completed_date") == "desc":
        queryset = queryset.order_by("-completed_date")
    return queryset


def create_console_order(request: WSGIRequest) -> tuple[ConsoleRent | None, dict | None]:
    """Create an order to rent one console"""

    console_name = request.POST.get("console")
    console = Console.objects.get(name=console_name)
    form = RentConsoleForm(request.POST)
    if form.is_valid():
        days = int(form.cleaned_data["days"])
        comment = form.cleaned_data["comment"]
        console_rent = ConsoleRent.objects.create(user=request.user, console=console, days=days, comment=comment)
        return console_rent, None
    else:
        return None, form.errors


def create_room_order(request: WSGIRequest) -> tuple[RoomRent | None, dict | None]:
    """Create an order to rent one club"""

    room_name = request.POST.get("room")
    room = Room.objects.get(name=room_name)
    form = RentRoomForm(data=request.POST, max_seats=room.seats)
    if form.is_valid():
        comment = form.cleaned_data["comment"]
        hours = form.cleaned_data["hours"]
        people = form.cleaned_data["people"]
        room_rent = RoomRent.objects.create(
            user=request.user, room=room, comment=comment, hours=hours, people=people
        )
        return room_rent, None
    else:
        return None, form.errors


def create_club_order(request: WSGIRequest) -> None:
    """Create an order to rent one room"""

    club_name = request.POST.get("club")
    club = Club.objects.get(name=club_name)
    comment = request.POST.get("comment")
    ClubRent.objects.create(user=request.user, club=club, comment=comment)


def get_console_order_list(request: WSGIRequest) -> list[ConsoleRent]:
    """Receive console orders"""

    console_rent_qs = ConsoleRent.objects.select_related("console")
    console_rent_qs = _add_filter(queryset=console_rent_qs, filter_query_dict=request.GET)

    user = CustomUser.objects.prefetch_related(
        Prefetch(
            "rented_consoles", queryset=console_rent_qs, to_attr="console_orders"
        )
    ).filter(pk=request.user.id)[0]
    return user.console_orders


def get_club_order_list(request: WSGIRequest) -> list[ClubRent]:
    """Receive club orders"""

    club_rent_qs = ClubRent.objects.select_related("club")
    user = CustomUser.objects.prefetch_related(
        Prefetch(
            "rented_clubs", queryset=club_rent_qs, to_attr="club_orders"
        )
    ).filter(pk=request.user.id)[0]
    return user.club_orders


def get_room_order_list(request: WSGIRequest) -> list[RoomRent]:
    """Receive room orders"""

    club_rent_qs = RoomRent.objects.select_related("room")
    user = CustomUser.objects.prefetch_related(
        Prefetch(
            "rented_rooms", queryset=club_rent_qs, to_attr="room_orders"
        )
    ).filter(pk=request.user.id)[0]

    return user.room_orders
