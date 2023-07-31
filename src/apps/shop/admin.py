from django.contrib import admin
from src.apps.shop.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    list_display = ("name", "product_type", "price", "description", "image", "updated_at")
    fields = ("name", "product_type", "price", "description", "image", "updated_at")
    list_filter = ("product_type",)
    readonly_fields = ("updated_at",)
