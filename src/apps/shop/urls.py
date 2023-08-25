from django.urls import path

from src.apps.shop.views import product_list, about_product, purchase_list, basket_list, order_page

app_name = "shop"
urlpatterns = [
    path("products/", product_list, name="product_list"),
    path("products/<int:product_id>/", about_product, name="about_product"),
    path("products/<int:product_id>/order/", order_page, name="order_page"),
    path("purchases/", purchase_list, name="purchase_list"),
    path("basket/", basket_list, name="basket_list"),
]
