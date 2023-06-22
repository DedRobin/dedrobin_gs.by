from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required

from src.apps.news.models import News, Company


@login_required(redirect_field_name="", login_url="login")
def index(request: WSGIRequest):
    return render(request, "index.html")


@login_required(redirect_field_name="", login_url="login")
def news_list(request: WSGIRequest):
    contex = {}
    news = News.objects.select_related("company") \
        .filter(is_published=True) \
        .values("topic", "link", "image_src", "text", "is_published", "created_at", "company__name")\
        .order_by("-created_at")

    paginator = Paginator(news, 24)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    contex["news"] = page_obj
    return render(request, "news_list.html", contex)
