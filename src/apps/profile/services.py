import os
from django.db.models.fields.files import ImageFieldFile
from django.core.handlers.wsgi import WSGIRequest

from src.apps.profile.models import Profile
from src.apps.profile.forms import OrderProfileForm


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


def get_or_create_profile(request: WSGIRequest) -> Profile:
    form = OrderProfileForm(request.POST)
    if form.is_valid():
        if request.user.is_authenticated:
            pk = request.user_profile.id
        else:
            pk = None
        profile = Profile.objects.get_or_create(pk=pk, defaults=form.cleaned_data, user=request.user.id)
        return profile[0]
    else:
        print(form.errors)
