from django.core.handlers.wsgi import WSGIRequest, QueryDict

from src.apps.address.models import Address
from src.apps.address.forms import OrderAddressForm, AddressForm


def get_address(address_id: int) -> Address:
    """Get a specific user address"""

    return Address.objects.get(pk=address_id)


def get_addresses(request: WSGIRequest):
    """Get a user addresses"""

    addresses = Address.objects.filter(user=request.user)
    return addresses


def update_address(address: Address, updated_data: QueryDict, contex) -> tuple[Address | None, None | str]:
    """Update a specific address"""

    form = AddressForm(updated_data)
    if form.is_valid():
        address.city = form.cleaned_data.get("city")
        address.street = form.cleaned_data.get("street")
        address.building = form.cleaned_data.get("building")
        address.flet = form.cleaned_data.get("flet")
        address.floor = form.cleaned_data.get("floor")
        address.entrance = form.cleaned_data.get("entrance")
        address.save()
        contex["success"] = "Address has been updated"
    else:
        contex["errors"] = form.errors
    return address, contex


def delete_address(request: WSGIRequest) -> None:
    address_id = request.POST["address_id"]
    Address.objects.filter(pk=address_id).delete()


def get_or_create_address(request: WSGIRequest) -> Address:
    if request.user.is_authenticated:
        form = OrderAddressForm(data=request.POST)
    else:
        form = AddressForm(request.POST)
    if form.is_valid():
        address = Address.objects.get_or_create(
            pk=form.cleaned_data.get("address"),
            defaults=form.cleaned_data,
            user=request.user.id)
        return address[0]
    else:
        print(form.errors)
