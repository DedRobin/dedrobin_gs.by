from django.db import models


class ClubAddress(models.Model):
    city = models.CharField()
    street = models.CharField()
    building = models.IntegerField()


class Club(models.Model):
    name = models.CharField()
    description = models.TextField()
    address = models.ForeignKey(ClubAddress, on_delete=models.CASCADE)
