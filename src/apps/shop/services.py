from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings
from src.apps.shop.spiders import MouseSpider, KeyboardSpider, HeadphoneSpider

from src.apps.shop.models import Product


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

    #
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
