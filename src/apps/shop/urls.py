from django.urls import path

from src.apps.shop.views import product_list, make_purchase

urlpatterns = [
    path("", product_list, name="product_list"),
    path("<int:product_id>/buy/", make_purchase, name="make_purchase"),
]
