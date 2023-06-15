from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import login, authenticate

from src.apps.user.models import CustomUser


def check_passwords_and_create_user(data: dict) -> tuple[str | None, bool]:
    """Checking two password. If the passwords are confirmed the user will be created"""

    password1 = data["password1"]
    password2 = data["password2"]
    passwords_match = password1 == password2
    if passwords_match:
        user = CustomUser.objects.create(
            username=data["username"],
            email=data["email"],
        )
        user.set_password(password1)
        user.save()
        return None, True
    else:
        error = "The two passwords doesn't match"
        return error, False


def user_authentication_and_login(request: WSGIRequest, data: dict) -> tuple[str | None, bool]:
    """If the user is authenticated, it logs in"""

    user = authenticate(request=request, **data)
    if user is None:
        error = "The user does not exist"
        return error, False
    else:
        login(request, user)
        return None, True
