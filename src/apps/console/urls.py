from django.urls import path

from src.apps.console.views import console_list

urlpatterns = [
    path("", console_list, name="console_list"),
]
