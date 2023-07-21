from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings
from django.db.models.query import QuerySet
from django.http.request import QueryDict
from src.apps.shop.spiders import MouseSpider

from django.core.paginator import Paginator, Page
from django.core.handlers.wsgi import WSGIRequest

from src.apps.news.models import News, Company


#
def run_parser(clear):
    #     if clear:
    #         Shop.objects.all().delete()
    #
    def crawler_results(signal, sender, item, response, spider):
        # Shop.objects.update_or_create(link=item["link"], defaults=item)
        print("crawler_results")

    #
    dispatcher.connect(crawler_results, signal=signals.item_scraped)
    settings = get_project_settings()
    process = CrawlerProcess(settings=settings)
    crawlers = [
        MouseSpider,
    ]
    for crawler in crawlers:
        process.crawl(crawler)
    process.start()
