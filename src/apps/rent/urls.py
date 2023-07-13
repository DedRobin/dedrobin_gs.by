from django.urls import path

from src.apps.rent.views import rent_list, console_order_list, console_list, rent_console, club_order_list, room_order_list

urlpatterns = [
    path("", rent_list, name="rent_list"),
    path("consoles/", console_list, name="console_list"),
    path("consoles/rent", rent_console, name="rent_console"),
    path("console_orders/", console_order_list, name="console_order_list"),
    path("club_orders/", club_order_list, name="club_order_list"),
    path("room_orders/", room_order_list, name="room_order_list"),

]


