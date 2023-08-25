from django.db import models

from src.apps.user.models import CustomUser


class Address(models.Model):
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    flet = models.IntegerField()
    floor = models.IntegerField(blank=True, null=True)
    entrance = models.IntegerField(blank=True, null=True)

    # Foreign keys
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name="addresses", null=True)

    def __str__(self):
        sentence = [
            f"{self.city} city",
            f"{self.street} street",
            f"{self.building} building",
            f"{self.flet} flet",
        ]
        if self.floor:
            sentence.append(f"{self.floor} floor")
        if self.entrance:
            sentence.append(f"{self.entrance} entrance")
        return ", ".join(sentence)

    def __repr__(self):
        return f"Address (ID={self.id}) '{self.city}. {self.street}, {self.building} ...'"
