from django.urls import path

from src.apps.auth.views import login_user, logout_user, register_user

urlpatterns = [
    path("registration/", register_user, name="registration"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]
