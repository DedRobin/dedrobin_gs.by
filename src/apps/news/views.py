from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required

from src.apps.news.models import News
from src.apps.news.forms import NewsFilterForm
from src.apps.news.services import get_page_from_request, get_displayed_pages, get_news


@login_required(redirect_field_name="", login_url="login")
def index(request: WSGIRequest):
    return render(request, "index.html")


@login_required(redirect_field_name="", login_url="login")
def news_list(request: WSGIRequest):
    contex = {}
    params = {}

    # Filter
    filter_form = NewsFilterForm(request.GET)
    if filter_form.is_valid():
        # Remove all values where it is None
        params = {field: value for field, value in filter_form.cleaned_data.items() if value}

    # Queryset
    news = get_news(params=params)

    # Pagination
    page = get_page_from_request(request=request, queryset=news, obj_per_page=24)
    displayed_pages = get_displayed_pages(page=page, show_pages=5)

    # Output data
    contex["news"] = page
    contex["displayed_pages"] = displayed_pages
    contex["filter_form"] = filter_form

    return render(request, "news_list.html", contex)
