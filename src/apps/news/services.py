from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from src.apps.news.spiders import CapcomSpider
from src.apps.news.models import News, Company


def run_parser(clear):
    if clear:
        News.objects.all().delete()

    def crawler_results(signal, sender, item, response, spider):
        company = Company.objects.get_or_create(name="Capcom")  # -> ("Company" obj, bool)
        item["company"] = company[0]  # ("Company" obj, bool) -> "Company" obj
        News.objects.update_or_create(external_id=item["external_id"], defaults=item)
        # print("Item =", item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)
    settings = get_project_settings()
    process = CrawlerProcess(settings=settings)
    crawlers = [
        CapcomSpider,
    ]
    for crawler in crawlers:
        process.crawl(crawler)
    process.start()
