from django.db import models


class Room(models.Model):
    name = models.CharField()
    number = models.IntegerField()
    seats = models.IntegerField()
