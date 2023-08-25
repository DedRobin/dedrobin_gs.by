from django.core.handlers.wsgi import WSGIRequest

from src.apps.address.models import Address
from src.apps.address.forms import OrderAddressForm, OrderAddressAnonymousForm


def get_or_create_address(request: WSGIRequest) -> Address:
    if request.user.is_authenticated:
        form = OrderAddressForm(data=request.POST)
    else:
        form = OrderAddressAnonymousForm(request.POST)
    if form.is_valid():
        address = Address.objects.get_or_create(
            pk=form.cleaned_data.get("address"),
            defaults=form.cleaned_data,
            user=request.user.id)
        return address[0]
    else:
        print(form.errors)