import scrapy
import re
from abc import ABC
from datetime import datetime
from scrapy.http import HtmlResponse
from scrapy import Selector
from scrapy_playwright.page import PageMethod


class CustomSpider(scrapy.Spider, ABC):
    def get_item(self, article: Selector, item: dict = None) -> dict:
        if item is None:
            item = {}
        item["created_at"] = self.get_publish_date(article)
        item["topic"] = self.get_topic(article)
        item["link"] = self.get_link(article)
        item["image_src"] = self.get_image_src(article)
        item["text"] = self.get_text(article)
        return item

    @staticmethod
    def get_publish_date(article: Selector) -> datetime:
        raise NotImplementedError

    @staticmethod
    def get_topic(article: Selector) -> str:
        raise NotImplementedError

    @staticmethod
    def get_link(article: Selector) -> str:
        raise NotImplementedError

    @staticmethod
    def get_text(article: Selector) -> str:
        raise NotImplementedError

    @staticmethod
    def get_image_src(article: Selector) -> str:
        raise NotImplementedError


class CapcomSpider(CustomSpider):
    name = "Capcom"
    start_urls = ["https://news.capcomusa.com/"]

    custom_settings = {
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    }

    async def parse(self, response: HtmlResponse, **kwargs) -> dict | None:
        for article in response.css(".news_section article"):
            item = self.get_item(article)
            different = datetime.now() - item["created_at"]
            if different.days > 366:
                return
            yield item

        next_page = response.xpath('//*[@id="pagination-next"]').attrib.get("href")
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    @staticmethod
    def get_publish_date(article: Selector) -> datetime:
        publish_date = article.css("article .text_col .attribution::text").get()
        publish_date = publish_date.replace(",", " ").split()[:3]
        str_date = " ".join(publish_date)
        publish_date = datetime.strptime(str_date, '%b %d %Y')
        return publish_date

    @staticmethod
    def get_topic(article: Selector) -> str:
        text = article.css(".major.mod-lt::text").get()
        return text

    @staticmethod
    def get_link(article: Selector) -> str:
        link = article.attrib.get("data-url")
        return link

    @staticmethod
    def get_text(article: Selector) -> str:
        text = []
        tags = article.css("article .text_col p")
        for tag in tags:
            p_tag_text = tag.css("p::text").get()
            strong_tag_text = tag.css("strong::text").get()
            if p_tag_text:
                text.append(p_tag_text)
            elif strong_tag_text:
                text.append(strong_tag_text)
            else:
                text.append("Error")
        return "\n".join(text)

    @staticmethod
    def get_image_src(article: Selector) -> str:
        tag = article.css("article .image_col.view.zoom.overlay.z-depth-2")
        css_style = tag.get()
        image_src = re.search(r"cdn\.capcom-unity\.com/\S+(\.jpg|\.png)", css_style).group()
        return "https://" + image_src


class BungieSpider(CustomSpider):
    name = "Bungie"
    start_urls = ["https://www.bungie.net/7/en/News"]

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
            PageMethod("wait_for_selector", ".NewsPreview_previewContainer__3wvXq")
        ],
    }
    page = 1

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta=self.meta)

    async def parse(self, response: HtmlResponse, **kwargs) -> None:
        articles = response.css(".NewsByCategory_articleList__1luur a.NewsPreview_previewContainer__3wvXq")
        for article in articles:
            item = self.get_item(article)
            different = datetime.now() - item["created_at"]
            if different.days > 366:
                return
            yield item
        self.page += 1
        next_page = f"https://www.bungie.net/7/en/News?page={self.page}"
        yield response.follow(next_page, callback=self.parse, meta=self.meta)

    @staticmethod
    def get_publish_date(article: Selector) -> datetime:
        publish_date = article.css("span::text").get()
        match = re.match(r"^ – \d{1,2}[smh]$", publish_date)
        if match:
            return datetime.now()
        match = re.match(r"^ – \d{1,2}/\d{1,2}/\d{4}$", publish_date)
        if match:
            publish_date = publish_date[3:]
            month, day, year = map(int, publish_date.split("/"))
            created_at = datetime(year=year, month=month, day=day)
            return created_at

    @staticmethod
    def get_topic(article: Selector) -> str:
        topic = article.css("h1.NewsPreview_title__1U06W::text").get()
        return topic

    @staticmethod
    def get_link(article: Selector) -> str:
        swagger = article.attrib.get("href")
        base_url = article.root.base_url[:22]
        link = base_url + swagger
        return link

    @staticmethod
    def get_text(article: Selector) -> str:
        text = article.css("h4.NewsPreview_subtitle__12s33::text").get()
        return text if text else ""

    @staticmethod
    def get_image_src(article: Selector) -> str:
        tag = article.css("div.NewsPreview_thumbnail__DSUsw").get()
        image_src = re.search(r"https://images.contentstack.io/\S+(\.jpg|\.png)", tag).group()
        return image_src
