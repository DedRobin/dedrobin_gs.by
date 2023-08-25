from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator, Page
from django.db.models.query import QuerySet
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from src.apps.shop.forms import PurchaseForm
from src.apps.shop.spiders import MouseSpider, KeyboardSpider, HeadphoneSpider
from src.apps.shop.models import Product, Purchase, Basket


#
def run_parser(clear):
    if clear:
        Product.objects.all().delete()

    async def crawler_results(signal, sender, item, response, spider):
        if spider.name == "Mouse":
            item["product_type"] = "mouse"
        elif spider.name == "Keyboard":
            item["product_type"] = "keyboard"
        elif spider.name == "Headphone":
            item["product_type"] = "headphone"
        else:
            item["product_type"] = "unknown"

        await Product.objects.aupdate_or_create(image=item["image"], defaults=item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)
    settings = get_project_settings()
    process = CrawlerProcess(settings=settings)
    crawlers = [
        MouseSpider,
        KeyboardSpider,
        HeadphoneSpider,
    ]
    for crawler in crawlers:
        process.crawl(crawler)
    process.start()


def create_purchase(request: WSGIRequest, product_id: int, address_id: int, profile_id: int = None) -> None:
    """Create a purchase"""

    form = PurchaseForm(request.POST)
    if form.is_valid():
        data = {
            "quantity": form.cleaned_data["quantity"],
            "comment": form.cleaned_data["comment"],
            "product_id": product_id,
            "address_id": address_id,
            "profile_id": profile_id,
        }
        if request.user.is_authenticated:
            data["user"] = request.user
        Purchase.objects.create(**data)
    else:
        print(form.errors)


def get_product_list_by_filter(request: WSGIRequest) -> QuerySet:
    """Receive product list by filter(request.GET)"""

    products = Product.objects.order_by("updated_at")
    filter_query_dict = request.GET
    if filter_query_dict:
        name = filter_query_dict.get("name")
        product_type = filter_query_dict.get("product_type")
        if name:
            products = products.filter(name__icontains=name)
        if product_type:
            products = products.filter(product_type=product_type)
    return products


def get_purchase_list_by_filter(request: WSGIRequest) -> QuerySet:
    """Receive purchase list by filter(request.GET)"""

    purchases = Purchase.objects.select_related("product", "user").filter(user=request.user).order_by("is_completed")
    filter_query_dict = request.GET
    if filter_query_dict:
        name = filter_query_dict.get("name")
        order_by_date = filter_query_dict.get("order_by_date")
        if name:
            purchases = purchases.filter(product__name__icontains=name)
        if order_by_date == "asc":
            purchases = purchases.order_by("created_at")
        elif order_by_date == "desc":
            purchases = purchases.order_by("-created_at")
    return purchases


def get_page_from_request(request: WSGIRequest, queryset: QuerySet, obj_per_page: int) -> Page:
    paginator = Paginator(object_list=queryset, per_page=obj_per_page)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return page_obj


def get_displayed_pages(page: Page, show_pages: int) -> range:
    def is_odd(num: int) -> bool:
        return True if num % 2 else False

    page_number = page.number
    page_range = page.paginator.page_range
    last_page = page.paginator.num_pages
    displayed_pages = page_range
    if last_page > show_pages:
        if page_number - (show_pages // 2 + 1) <= 0:
            start = 0
            end = show_pages
        elif page_number - (show_pages // 2 + 1) > 0 and page_number + (show_pages // 2) > last_page:
            start = last_page - show_pages
            end = last_page + 1
        else:
            start = page_number - (show_pages // 2) - 1
            end = page_number + (show_pages // 2) - 1
            if is_odd(show_pages):
                end += 1
        displayed_pages = page_range[start:end]
    return displayed_pages


def get_products_from_user_basket(request: WSGIRequest):
    if request.user.is_authenticated:
        basket = Basket.objects.get(user=request.user)
        products = basket.products.all()
    else:
        products_in_basket = request.session.get("products_in_basket")
        if products_in_basket:
            products = Product.objects.filter(pk__in=products_in_basket)
        else:
            products = Product.objects.none()
    return products


def add_product_to_basket(request: WSGIRequest):
    product_id = int(request.POST["add_product_to_basket"])
    if request.user.is_authenticated:
        basket = Basket.objects.get(user=request.user)
        if basket.products.filter(pk=product_id).exists():
            basket.products.remove(product_id)
        else:
            basket.products.add(product_id)
    else:
        products_in_basket = request.session.get("products_in_basket")
        if products_in_basket:
            if product_id not in products_in_basket:
                products_in_basket.append(product_id)
                request.session["products_in_basket"] = products_in_basket
        else:
            request.session["products_in_basket"] = [product_id]


def remove_product_from_basket(request: WSGIRequest, product_id: int = None):
    if product_id is None:
        product_id = int(request.POST["remove_product"])
    if request.user.is_authenticated:
        basket = Basket.objects.get(user=request.user)
        basket.products.remove(product_id)
    else:
        products_in_basket: list = request.session["products_in_basket"]
        products_in_basket.remove(product_id)
        request.session["products_in_basket"] = products_in_basket
