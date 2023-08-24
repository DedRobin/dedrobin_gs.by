import os
from django.db.models.fields.files import ImageFieldFile
from django.core.handlers.wsgi import WSGIRequest, QueryDict

from src.apps.profile.models import Profile


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


def get_or_create_profile(request: WSGIRequest, data: QueryDict) -> Profile:
    if request.user.is_authenticated:
        profile = Profile.objects.get_or_create(pk=request.user_profile.id, defaults=data, user=request.user)
    else:
        profile = Profile.objects.get_or_create(pk=request.user_profile.id, defaults=data)
    return profile
