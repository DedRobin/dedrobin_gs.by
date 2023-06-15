from django.urls import path

from src.apps.news.views import index

urlpatterns = [
    path("", index, name="index"),
]
