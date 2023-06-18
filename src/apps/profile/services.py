from src.apps.user.models import CustomUser
from src.apps.profile.models import Profile


def convert_to_dict(model: CustomUser | Profile) -> dict:
    data = {}
    if isinstance(model, CustomUser):
        data["email"] = model.email
        data["username"] = model.username
        return data
    data = model.__dict__
    return data
