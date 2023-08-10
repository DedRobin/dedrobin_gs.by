from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required

from src.apps.shop.models import Product
from src.apps.shop.forms import PurchaseForm
from src.apps.shop.services import create_purchase, get_purchase_list_by_filter, get_product_list_by_filter
from src.apps.shop.forms import ProductFilterForm, PurchaseFilterForm


def product_list(request: WSGIRequest, contex: dict = None):
    if contex is None:
        contex = {}
    products = get_product_list_by_filter(request)
    form = PurchaseForm()
    filter_form = ProductFilterForm(request.GET)
    contex["products"] = products
    contex["form"] = form
    contex["filter_form"] = filter_form
    status = contex.get("status")
    return render(request, "product/product_list.html", contex, status=status)


def about_product(request: WSGIRequest, product_id: int):
    contex = {}
    product = Product.objects.get(id=product_id)
    form = PurchaseForm()
    contex["product"] = product
    contex["form"] = form
    return render(request, "product/about_product.html", contex)


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


@login_required(redirect_field_name="", login_url="login")
def purchase_list(request: WSGIRequest):
    contex = {}
    filter_form = PurchaseFilterForm(request.GET)
    purchases = get_purchase_list_by_filter(request)
    contex["purchases"] = purchases
    contex["filter_form"] = filter_form
    return render(request, "purchase/purchase_list.html", contex)
