from django.urls import path

from src.apps.profile.views import edit_profile

urlpatterns = [
    path("", edit_profile, name="edit_profile"),
]
