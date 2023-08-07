from django.urls import path

from src.apps.shop.views import product_list, make_purchase, purchase_list

urlpatterns = [
    path("products/", product_list, name="product_list"),
    path("products/<int:product_id>/buy/", make_purchase, name="make_purchase"),
    path("purchases/", purchase_list, name="purchase_list"),
]
