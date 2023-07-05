from django.urls import path

from src.apps.rent.views import rent

urlpatterns = [
    path("", rent, name="rent"),
]
