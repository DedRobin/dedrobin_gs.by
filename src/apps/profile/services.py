import os
from django.db.models.fields.files import ImageFieldFile


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
