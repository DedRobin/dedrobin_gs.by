import scrapy
import re
from abc import ABC
from datetime import datetime
from scrapy.http import HtmlResponse
from scrapy import Selector
from scrapy_playwright.page import PageMethod


class MouseSpider(scrapy.Spider):
    name = "Products"
    start_urls = ["https://catalog.onliner.by/mouse?type_mk%5B0%5D=mouse_games&type_mk%5Boperation%5D=union"]

    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    }
    meta = {
        "playwright": True,
        "playwright_include_page": True,
        "playwright_page_methods": [
            PageMethod("wait_for_selector", "a.schema-pagination__main")
        ],
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta=self.meta)

    async def parse(self, response: HtmlResponse, **kwargs) -> dict | None:
        products = response.css(".schema-products .schema-product__group")[:10]
        for product in products:
            href = product.css(".js-product-title-link").attrib.get("href")
            print()
        # next_page = response.xpath('//*[@id="pagination-next"]').attrib.get("href")
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
