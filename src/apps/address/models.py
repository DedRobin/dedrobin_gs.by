from django.db import models

from src.apps.user.models import CustomUser


class Address(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    flet = models.IntegerField()
    floor = models.IntegerField(blank=True, null=True)
    entrance = models.IntegerField(blank=True, null=True)

    # Foreign keys
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name="addresses", null=True)

    def __str__(self):
        return f"Address (ID={self.id}) '{self.city}. {self.street}, {self.building} ...'"
