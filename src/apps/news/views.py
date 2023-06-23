from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required

from src.apps.news.models import News, Company
from src.apps.news.services import get_page_from_request


@login_required(redirect_field_name="", login_url="login")
def index(request: WSGIRequest):
    return render(request, "index.html")


@login_required(redirect_field_name="", login_url="login")
def news_list(request: WSGIRequest):
    contex = {}
    news = News.objects.select_related("company") \
        .filter(is_published=True) \
        .values("topic", "link", "image_src", "text", "is_published", "created_at", "company__name") \
        .order_by("-created_at")

    page, num_pages = get_page_from_request(request=request, queryset=news, obj_per_page=24)
    contex["news"] = page

    return render(request, "news_list.html", contex)
