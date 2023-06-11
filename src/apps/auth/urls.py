from django.urls import path

from src.apps.auth.views import login

urlpatterns = [
    path("", login, name="login"),
]
