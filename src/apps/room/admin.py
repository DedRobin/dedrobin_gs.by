from django.contrib import admin

from src.apps.room.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "seats")
    fields = ("name", "number", "seats")
