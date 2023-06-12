from django.urls import path

from src.apps.entrypoint.views import index

urlpatterns = [
    path("", index, name="index"),
]
