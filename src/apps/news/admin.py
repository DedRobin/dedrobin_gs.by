from django.contrib import admin
from src.apps.news.models import News, Company


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("topic", "link", "image_src", "text", "is_published", "created_at", "company")
    fields = ("topic", "link", "image_src", "text", "is_published", "created_at", "company")


@admin.register(Company)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)