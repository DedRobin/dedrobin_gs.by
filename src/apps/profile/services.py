from src.apps.user.models import CustomUser
from src.apps.profile.models import Profile


def convert_to_dict(model: CustomUser | Profile) -> dict:
    data = model.__dict__
    if isinstance(model, CustomUser) and data.get("password"):
        # Clear passwords fields
        del data["password"]
    return data
