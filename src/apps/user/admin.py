from django.contrib import admin

from src.apps.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "password", "is_staff", "is_superuser", "created_at")
    fields = ("username", "email", "password", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser")
    readonly_fields = ("created_at",)
    search_fields = ("username", "email", "is_staff", "is_superuser")
