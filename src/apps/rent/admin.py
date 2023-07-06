from django.contrib import admin

from src.apps.rent.models import RoomOrder, ConsoleOrder, ClubOrder


@admin.register(ConsoleOrder)
class ConsoleOrderAdmin(admin.ModelAdmin):
    list_display = ("console", "description", "user", "created_at")
    fields = ("console", "description", "user")


@admin.register(RoomOrder)
class RoomOrderAdmin(admin.ModelAdmin):
    list_display = ("room", "description", "user", "created_at")
    fields = ("room", "description", "user")


@admin.register(ClubOrder)
class RoomOrderAdmin(admin.ModelAdmin):
    list_display = ("club", "description", "user", "created_at")
    fields = ("club", "description", "user")
