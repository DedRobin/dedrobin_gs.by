from django.urls import path, include

from src.apps.rent.views import rent_list

urlpatterns = [
    path("", rent_list, name="rent_list"),
    path("consoles/", include("src.apps.console.urls")),
]
