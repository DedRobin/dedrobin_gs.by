from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings
from django.db.models.query import QuerySet
from src.apps.news.spiders import CapcomSpider, BungieSpider

from django.core.paginator import Paginator, Page
from django.core.handlers.wsgi import WSGIRequest

from src.apps.news.models import News, Company


def run_parser(clear):
    if clear:
        News.objects.all().delete()

    async def crawler_results(signal, sender, item, response, spider):

        company = []
        if spider.name == "Capcom":
            company = await Company.objects.aget_or_create(
                name="Capcom",
                url="https://www.capcom.com/"
            )  # -> ("Company" obj, bool)
        elif spider.name == "Bungie":
            company = await Company.objects.aget_or_create(
                name="Bungie",
                url="https://www.bungie.net/"
            )
        item["company"] = company[0]  # ("Company" obj, bool) -> "Company" obj
        try:
            await News.objects.aupdate_or_create(link=item["link"], defaults=item)
        except Exception as ex:
            print(item["text"], item["link"], ex)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)
    settings = get_project_settings()
    process = CrawlerProcess(settings=settings)
    crawlers = [
        CapcomSpider,
        BungieSpider,
    ]
    for crawler in crawlers:
        process.crawl(crawler)
    process.start()


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
