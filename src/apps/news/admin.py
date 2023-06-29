from django.contrib import admin
from src.apps.news.models import News, Company


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("topic", "link", "image_src", "is_published", "created_at", "company")
    fields = ("topic", "link", "image_src", "text", "is_published", "created_at", "company")
    list_filter = ("is_published", "company__name",)
    search_fields = ("topic", "link")


@admin.register(Company)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    fields = ("name", "url")
