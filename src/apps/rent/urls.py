from django.urls import path

from src.apps.rent.views import rent_list, console_list, rent_console

urlpatterns = [
    path("", rent_list, name="rent_list"),
    path("consoles/", console_list, name="console_list"),
    path("consoles/rent", rent_console, name="rent_console"),
]
