from src.apps.user.models import CustomUser


def update_user(user: CustomUser, data: dict) -> CustomUser | str:
    password1 = data.get("password1")
    password2 = data.get("password2")
    user.username = data.get("username")
    user.email = data.get("email")
    if (password1 and not password2) or (not password1 and password2):
        raise ValueError("Password field is empty")
    elif password1 and password2:
        assert password1 == password2
        user.set_password(password1)
    user.save()
    return user


def delete_user(user: CustomUser) -> None:
    # CustomUser.objects.get(user=user).delete()
    user.delete()
