from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=150)
    number = models.IntegerField()
    seats = models.IntegerField()
