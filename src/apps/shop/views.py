from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required

from src.apps.shop.models import Product, Purchase
from src.apps.shop.forms import PurchaseForm
from src.apps.shop.services import create_purchase


def product_list(request: WSGIRequest, contex: dict = None):
    if contex is None:
        contex = {}
    products = Product.objects.all()
    form = PurchaseForm()
    contex["products"] = products
    contex["form"] = form
    status = contex.get("status")
    if status:
        return render(request, "product_list.html", contex, status=status)
    else:
        return render(request, "product_list.html", contex)


@login_required(redirect_field_name="", login_url="login")
def make_purchase(request: WSGIRequest, product_id: int):
    contex = {}
    if request.method == "POST":
        purchase, errors = create_purchase(request, product_id)
        if errors:
            contex = dict(errors=errors)
        else:

            notification = "The Purchase for '{0}' is made out".format(purchase.product.name)
            contex = dict(notification=notification)
            contex["status"] = 201
    render_obj = product_list(request, contex)
    return render_obj
