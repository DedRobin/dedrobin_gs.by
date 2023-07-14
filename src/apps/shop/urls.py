from django.urls import path

from src.apps.shop.views import product_list

urlpatterns = [
    path("", product_list, name="product_list"),
]
