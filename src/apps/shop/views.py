from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from src.apps.shop.models import Product


def product_list(request: WSGIRequest):
    contex = {}
    products = Product.objects.all()
    contex["products"] = products
    return render(request, "product_list.html", contex)
