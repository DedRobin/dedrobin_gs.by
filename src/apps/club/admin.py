from django.contrib import admin

from src.apps.club.models import Club, ClubAddress


@admin.register(ClubAddress)
class ClubAddressAdmin(admin.ModelAdmin):
    list_display = ("city", "street", "building")
    fields = ("city", "street", "building")


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "address")
    fields = ("name", "description", "address")
