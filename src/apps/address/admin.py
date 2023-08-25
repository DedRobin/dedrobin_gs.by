from django.contrib import admin

from src.apps.address.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    # class Meta:

    list_display = ("city", "street", "building", "flet", "floor", "entrance", "user")
    fields = ("city", "street", "building", "flet", "floor", "entrance", "user")
