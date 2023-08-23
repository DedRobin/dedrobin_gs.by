from django.core.handlers.wsgi import WSGIRequest

from src.apps.address.models import Address


def create_address(request: WSGIRequest, data: dict):
    if request.user.is_authenticated:
        Address.objects.create(**data, user=request.user)
    else:
        Address.objects.create(**data)
