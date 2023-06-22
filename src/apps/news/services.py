from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings
from django.db.models.query import QuerySet
from src.apps.news.spiders import CapcomSpider
from src.apps.news.models import News, Company
from django.core.handlers.wsgi import WSGIRequest

from django.core.paginator import Paginator, Page
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required

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


def get_page_from_request(request: WSGIRequest, queryset: QuerySet, obj_per_page: int) -> tuple[Page, int]:
    paginator = Paginator(object_list=queryset, per_page=obj_per_page)
    num_pages = paginator.num_pages
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return page_obj, num_pages
