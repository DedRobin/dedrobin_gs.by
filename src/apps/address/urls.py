from django.urls import path

from src.apps.address.views import address_list, edit_address

app_name = "address"
urlpatterns = [
    path("", address_list, name="address_list"),
    path("<int:address_id>/", edit_address, name="edit_address"),
]
