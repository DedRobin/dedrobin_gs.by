from django.contrib import admin

from src.apps.console.models import Console


@admin.register(Console)
class ConsoleAdmin(admin.ModelAdmin):
    list_display = ("name", "price_per_day", "image")
    fields = ("name", "price_per_day", "image")
