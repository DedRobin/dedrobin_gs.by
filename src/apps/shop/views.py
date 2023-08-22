from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required

from src.apps.shop.models import Product
from src.apps.shop.forms import PurchaseForm
from src.apps.shop.services import create_purchase, get_purchase_list_by_filter, get_product_list_by_filter, \
    get_page_from_request, get_displayed_pages, get_products_from_user_basket, remove_product_from_basket, \
    add_product_to_basket
from src.apps.shop.forms import ProductFilterForm, PurchaseFilterForm


def product_list(request: WSGIRequest, contex: dict = None):
    """Receive a product list for a specific user"""

    if contex is None:
        contex = {}

    if request.method == "POST":
        # Add product to basket
        add_product_to_basket(request)

    products = get_product_list_by_filter(request)
    form = PurchaseForm()

    # Basket
    products_in_basket = get_products_from_user_basket(request)
    request.basket_quantity = len(products_in_basket)

    # Pagination
    page = get_page_from_request(request=request, queryset=products, obj_per_page=10)
    displayed_pages = get_displayed_pages(page=page, show_pages=5)

    filter_form = ProductFilterForm(request.GET)

    contex["page"] = page
    contex["form"] = form
    contex["displayed_pages"] = displayed_pages
    contex["quantity"] = len(page.object_list)
    contex["products_in_basket"] = products_in_basket
    contex["filter_form"] = filter_form
    status = contex.get("status")
    return render(request, "product/product_list.html", contex, status=status)


def about_product(request: WSGIRequest, product_id: int):
    """Follow to a product description"""

    contex = {}
    product = Product.objects.get(id=product_id)
    form = PurchaseForm()
    contex["product"] = product
    contex["form"] = form
    return render(request, "product/about_product.html", contex)


@login_required(redirect_field_name="", login_url="login")
def make_purchase(request: WSGIRequest, product_id: int):
    """Create a purchase for specific user"""

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
    """Receive a purchase list for a specific user"""

    contex = {}
    filter_form = PurchaseFilterForm(request.GET)
    purchases = get_purchase_list_by_filter(request)

    # Pagination
    page = get_page_from_request(request=request, queryset=purchases, obj_per_page=10)
    displayed_pages = get_displayed_pages(page=page, show_pages=5)

    contex["page"] = purchases
    contex["displayed_pages"] = displayed_pages
    contex["count"] = len(page.object_list)
    contex["filter_form"] = filter_form
    return render(request, "purchase/purchase_list.html", contex)


def basket_list(request: WSGIRequest):
    """
    GET method:
    Receive a product list added to a basket

    PORT method:
    Remove a specific product from a basket
    """

    contex = {}

    if request.method == "POST":
        # Remove product from basket
        remove_product_from_basket(request)
    if not request.user.is_authenticated:
        if request.session.get("products_in_basket"):
            product_ids = request.session.get("products_in_basket")
            if not product_ids:
                request.session["products_in_basket"] = []
                products = Product.objects.none()
            else:
                products = Product.objects.filter(pk__in=product_ids)
        else:
            products = Product.objects.none()
    else:
        products = get_products_from_user_basket(request)
    request.basket_quantity = len(products)
    contex["page"] = products
    return render(request, "basket/basket.html", contex)
