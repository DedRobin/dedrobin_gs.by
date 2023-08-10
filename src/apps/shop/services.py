from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings
from django.core.handlers.wsgi import WSGIRequest

from src.apps.shop.forms import PurchaseForm
from src.apps.shop.spiders import MouseSpider, KeyboardSpider, HeadphoneSpider
from src.apps.shop.models import Product, Purchase


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


def create_purchase(request: WSGIRequest, product_id: int) -> tuple[Purchase | None, dict | None]:
    """Create a purchase"""

    form = PurchaseForm(request.POST)
    if form.is_valid():
        purchase = Purchase.objects.create(
            quantity=form.cleaned_data["quantity"],
            comment=form.cleaned_data["comment"],
            user=request.user,
            product_id=product_id
        )
        return purchase, None
    else:
        return None, form.errors


def get_product_list_by_filter(request: WSGIRequest) -> list[Product]:
    """Receive product list by filter(request.GET)"""

    products = Product.objects.all()
    filter_query_dict = request.GET
    if filter_query_dict:
        name = filter_query_dict.get("name")
        product_type = filter_query_dict.get("product_type")
        if name:
            products = products.filter(name__icontains=name)
        if product_type:
            products = products.filter(product_type=product_type)
    return products


def get_purchase_list_by_filter(request: WSGIRequest) -> list[Purchase]:
    """Receive purchase list by filter(request.GET)"""

    purchases = Purchase.objects.select_related("product", "user").filter(user=request.user)
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
