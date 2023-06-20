from django.urls import path

from src.apps.profile.views import edit_profile, delete_profile

urlpatterns = [
    path("", edit_profile, name="edit_profile"),
    path("delete/", delete_profile, name="delete_profile"),
]
