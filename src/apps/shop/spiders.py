import scrapy
from decimal import Decimal
from scrapy.http import HtmlResponse
from scrapy_playwright.page import PageMethod


class ProductBaseSpider(scrapy.Spider):
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
            PageMethod("wait_for_selector", ".value__text")
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
        for url in urls:
            yield response.follow(url, callback=self.parse)

    async def parse(self, response: HtmlResponse, **kwargs):
        item = dict()

        name = response.css(".catalog-masthead__title.js-nav-header::text").get()
        item["name"] = name.strip()
        item["image"] = response.css(".offers-description__preview img").attrib.get("src")
        item["description"] = response.css(".offers-description__specs p::text").get()

        price = response.css(
            ".offers-description__link.offers-description__link_nodecor.js-description-price-link::text").get()
        price = price.replace("р.", "").replace(",", ".").strip()
        price = Decimal(price)
        item["price"] = price

        return item


class MouseSpider(ProductBaseSpider):
    name = "Mouse"
    start_urls = ["https://catalog.onliner.by/mouse?type_mk%5B0%5D=mouse_games&type_mk%5Boperation%5D=union"]


class KeyboardSpider(ProductBaseSpider):
    name = "Keyboard"
    start_urls = ["https://catalog.onliner.by/keyboards?keyb_type%5B0%5D=keyb_games&keyb_type%5Boperation%5D=union"]


class HeadphoneSpider(ProductBaseSpider):
    name = "Headphone"
    start_urls = [
        "https://catalog.onliner.by/headphones?hp_destination%5B0%5D=gamer&hp_destination%5Boperation%5D=union"]
