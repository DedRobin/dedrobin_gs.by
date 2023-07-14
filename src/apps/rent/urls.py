from django.urls import path

from src.apps.rent.views import console_order_list, console_list, rent_console, club_order_list, \
    room_order_list, room_list, rent_room, club_list, rent_club

urlpatterns = [
    path("consoles/", console_list, name="console_list"),
    path("consoles/rent", rent_console, name="rent_console"),
    path("rooms/", room_list, name="room_list"),
    path("rooms/rent", rent_room, name="rent_room"),
    path("clubs/", club_list, name="club_list"),
    path("clubs/rent", rent_club, name="rent_club"),
    path("console_orders/", console_order_list, name="console_order_list"),
    path("club_orders/", club_order_list, name="club_order_list"),
    path("room_orders/", room_order_list, name="room_order_list"),

]
