import logging

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
    news = News.objects.all()
    contex["news"] = news
    return render(request, "news_list.html", contex)
