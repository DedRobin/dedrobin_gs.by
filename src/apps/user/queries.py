from src.apps.user.models import CustomUser


def update_user(user: CustomUser, data: dict) -> CustomUser:
    password1 = data.get("password1")
    password2 = data.get("password1")
    user.username = data.get("username")
    user.email = data.get("email")
    if password1 and password2 and password1 == password2:
        user.set_password(password1)
    user.save()
    return user
