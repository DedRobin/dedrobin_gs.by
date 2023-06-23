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


def get_page_from_request(request: WSGIRequest, queryset: QuerySet, obj_per_page: int) -> Page:
    paginator = Paginator(object_list=queryset, per_page=obj_per_page)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return page_obj


def get_displayed_pages(page: Page, page_numbers: int) -> range:
    page_number = page.number
    page_range = page.paginator.page_range
    last_page = page.paginator.num_pages
    displayed_pages = page_range
    if len(page_range) > page_numbers:
        if page_number - 3 <= 0:
            displayed_pages = page_range[:page_numbers]
        elif page_number - 3 > 0 and page_number + 2 > last_page:
            if page_number == last_page:
                displayed_pages = page_range[page_number - 5:last_page + 1]
            else:
                displayed_pages = page_range[page_number - 4:last_page + 1]
        else:
            displayed_pages = page_range[page_number - 3:page_number + 2]
    return displayed_pages
