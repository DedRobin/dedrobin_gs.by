from django.contrib import admin

from src.apps.profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "gender", "phone_number", "age", "birthday", "user")
    fields = ("first_name", "last_name", "gender", "phone_number", "age", "birthday", "user")
