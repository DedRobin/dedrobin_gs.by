import scrapy
import re
from abc import ABC
from datetime import datetime
from scrapy.http import HtmlResponse
from scrapy import Selector
from scrapy_playwright.page import PageMethod


class OnlinerSpider(scrapy.Spider):
    name = "Products"
    start_urls = ["https://catalog.onliner.by/"]

    custom_settings = {
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    }

    async def parse(self, response: HtmlResponse, **kwargs) -> dict | None:
        # selector = response.xpath('//*[@id="container"]/div/div/div/div/div[1]/div[4]/div/div[13]/div[1]/div/div[6]')
        selectors = response.css(".catalog-navigation-list__category")
        products = selectors.css(".catalog-navigation-list__dropdown-list .catalog-navigation-list__dropdown-item")
        for product in products:
            print(product)
        # next_page = response.xpath('//*[@id="pagination-next"]').attrib.get("href")
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
