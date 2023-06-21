import scrapy
import re
from datetime import datetime
from scrapy.http import HtmlResponse
from scrapy import Selector


class CapcomSpider(scrapy.Spider):
    name = "news.capcomusa.com/"
    start_urls = ["https://news.capcomusa.com/"]

    def parse(self, response: HtmlResponse, **kwargs) -> None:
        data = {}
        for article in response.css(".news_section article"):
            data["publish_data"] = self._get_publish_date(article)
            different = datetime.now() - data["publish_data"]
            print(different)
            if different.days > 366:
                return None
            data["topic"] = self._get_topic(article)
            data["link"] = self._get_link(article)
            data["image_src"] = self._get_image_src(article)
            data["text"] = self._get_text(article)
            yield data

        next_page = response.xpath('//*[@id="pagination-next"]').attrib.get("href")
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    @staticmethod
    def _get_topic(article: Selector) -> str:
        text = article.css(".major.mod-lt::text").get()
        return text

    @staticmethod
    def _get_link(article: Selector) -> str:
        link = article.attrib.get("data-url")
        return link

    @staticmethod
    def _get_text(article: Selector) -> str:
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
    def _get_image_src(article: Selector) -> str:
        tag = article.css("article .image_col.view.zoom.overlay.z-depth-2")
        css_style = tag.get()
        image_src = re.search(r"cdn\.capcom-unity\.com\/\S+(\.jpg|\.png)", css_style).group()
        return image_src

    @staticmethod
    def _get_publish_date(article: Selector) -> datetime:
        publish_date = article.css("article .text_col .attribution::text").get()
        publish_date = publish_date.replace(",", " ").split()[:3]
        str_date = " ".join(publish_date)
        publish_date = datetime.strptime(str_date, '%b %d %Y')
        return publish_date
