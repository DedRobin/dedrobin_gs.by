from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from src.apps.user.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff", "is_superuser", "created_at")
    list_filter = ("username", "email", "is_staff", "is_superuser", "created_at")

    fieldsets = (
        (None, {
            "fields": ("username", "email", "password")
        }),
        ("Permissions", {
            "fields": ("is_staff", "is_superuser")
        }),
    )
    add_fieldsets = (
        (None, {
            "fields": (
                "username", "email", "password1", "password2", "is_staff", "is_superuser"
            )}
         ),
    )
