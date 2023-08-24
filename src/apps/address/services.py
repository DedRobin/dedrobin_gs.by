from django.core.handlers.wsgi import WSGIRequest

from src.apps.address.models import Address


def get_or_create_address(request: WSGIRequest, data: dict) -> Address:
    if request.user.is_authenticated:
        address = Address.objects.get_or_create(pk=data["address"], defaults=data, user=request.user)
    else:
        address = Address.objects.get_or_create(pk=data["address"], defaults=data)
    return address
