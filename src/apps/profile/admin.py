from django.contrib import admin

from src.apps.profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "gender", "phone_number", "age", "birthday", "photo")
    fields = ("user", "first_name", "last_name", "gender", "phone_number", "age", "birthday", "photo")
