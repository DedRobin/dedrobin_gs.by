from django.contrib import admin
from src.apps.shop.models import Product, Purchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    list_display = ("name", "product_type", "price", "description", "image", "updated_at")
    fields = ("name", "product_type", "price", "description", "image", "updated_at")
    list_filter = ("product_type",)
    readonly_fields = ("updated_at",)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"

    list_display = ("quantity", "comment", "user", "product", "created_at")
    fields = ("quantity", "comment", "user", "product", "created_at")
    readonly_fields = ("created_at",)

