import os
from django.db.models.fields.files import ImageFieldFile

from src.apps.user.models import CustomUser
from src.apps.profile.models import Profile


def convert_to_dict(model_object: CustomUser | Profile) -> dict:
    data = {}
    if isinstance(model_object, CustomUser):
        data["email"] = model_object.email
        data["username"] = model_object.username
        return data
    data = model_object.__dict__
    return data


def uploaded_photo(photo: ImageFieldFile, path: str) -> str:
    parts = path.split(".")
    file_format = path.split(".")[-1]
    if not photo.name.endswith(file_format):
        parts[-1] = photo.name.split(".")[-1]
        new_path = ".".join(parts)  # change file format
        os.rename(f"src/apps/{path}", f"src/apps/{new_path}")
        path = new_path
    with open(f"src/apps/{path}", "wb+") as destination:
        for chunk in photo.chunks():
            destination.write(chunk)
    return path
