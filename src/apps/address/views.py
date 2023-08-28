from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required

from src.apps.address.services import get_addresses, get_address, delete_address, update_address
from src.apps.address.forms import AddressForm


@login_required(redirect_field_name="", login_url="login")
def address_list(request: WSGIRequest):
    contex = dict()

    if request.method == "POST":
        delete_address(request)

    addresses = get_addresses(request)
    contex["addresses"] = addresses
    return render(request, "address_list.html", contex)


@login_required(redirect_field_name="", login_url="login")
def edit_address(request: WSGIRequest, address_id: int):
    contex = dict()
    address = get_address(address_id)

    if request.method == "POST":
        address, contex = update_address(address=address, updated_data=request.POST, contex=contex)

    form = AddressForm(address.__dict__)
    contex["form"] = form
    contex["address"] = address

    return render(request, "edit_address.html", contex)
