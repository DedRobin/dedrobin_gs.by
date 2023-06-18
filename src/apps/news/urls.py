from django.urls import path

from src.apps.news.views import index, news_list

urlpatterns = [
    path("", index, name="index"),
    path("news/", news_list, name="news_list"),
]
