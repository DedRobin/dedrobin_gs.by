from django.contrib import admin

from src.apps.rent.models import RoomOrder, ConsoleOrder, ClubOrder, Club, Console, Room, ClubAddress


@admin.register(ClubAddress)
class ClubAddressAdmin(admin.ModelAdmin):
    list_display = ("city", "street", "building")
    fields = ("city", "street", "building")


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "address")
    fields = ("name", "description", "address")


@admin.register(Console)
class ConsoleAdmin(admin.ModelAdmin):
    list_display = ("name", "price_per_day", "image")
    fields = ("name", "price_per_day", "image")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "seats")
    fields = ("name", "number", "seats")


@admin.register(ConsoleOrder)
class ConsoleOrderAdmin(admin.ModelAdmin):
    list_display = ("console", "days", "comment", "user", "created_at")
    fields = ("console", "days", "comment", "user", "created_at")
    readonly_fields = ("created_at",)


@admin.register(RoomOrder)
class RoomOrderAdmin(admin.ModelAdmin):
    list_display = ("room", "comment", "user", "created_at")
    fields = ("room", "comment", "user", "created_at")
    readonly_fields = ("created_at",)


@admin.register(ClubOrder)
class ClubOrderAdmin(admin.ModelAdmin):
    list_display = ("club", "comment", "user", "created_at")
    fields = ("club", "comment", "user", "created_at")
    readonly_fields = ("created_at",)
