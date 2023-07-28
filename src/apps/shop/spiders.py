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
            # PageMethod("wait_for_selector", "a.schema-pagination__main")
            PageMethod("wait_for_selector", ".schema-product__part.schema-product__part_1")
        ],
    }
    meta2 = {
        "playwright": True,
        "playwright_include_page": True,
        "playwright_page_methods": [
            PageMethod("wait_for_selector", ".offers-description__link.offers-description__link_nodecor")
        ],
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.get_urls, meta=self.meta)

    async def get_urls(self, response: HtmlResponse, **kwargs):
        urls = []
        products = response.css(".schema-products .schema-product__group")[:10]
        for product in products:
            url = product.css(".js-product-title-link").attrib.get("href")
            urls.append(url)
            print()
        for url in urls:
            yield response.follow(url, callback=self.parse)
            # yield response.follow(url, callback=self.parse, meta=self.meta2)

    async def parse(self, response: HtmlResponse, **kwargs):
        # price = response.css(
        #     ".offers-description__link.offers-description__link_nodecor.js-description-price-link::text").get()
        # table_body = response.css("table.product-specs__table tbody:nth-child(n+2):nth-child(-n+3)")
        # main = table_body[0].css("tr:nth-child(n+2):nth-child(-n+10)")
        # interface = main[0].css("td:nth-child(2) span::text").get()  # Интерфейс подключения мыши
        # sensor_type = main[4].css("td:nth-child(2) span::text").get()  # Тип сенсора
        # max_sensor_resolution = main[6].css("td:nth-child(2) span::text").get()  # Максимальное разрешение сенсора
        # tech_spec = table_body[0].css("tr:nth-child(n+2):nth-child(-n+10)")
        tbodies = response.css("table tbody")[0:3]
        tr1 = tbodies[0].css("tr")
        date = tr1[1].css("td:nth-child(2) span::text").get()
        tr2 = tbodies[1].css("tr")
        interface = tr2[1].css("td:nth-child(2) span::text").get()  # Интерфейс подключения мыши
        sensor_type = tr2[5].css("td:nth-child(2) span::text").get()  # Тип сенсора
        max_sensor_resolution = tr2[7].css("td:nth-child(2) span::text").get()  # Максимальное разрешение сенсора
        tr3 = tbodies[2].css("tr")
        length = tr3[1].css("tr:nth-child(2) span::text").get()
        print()
