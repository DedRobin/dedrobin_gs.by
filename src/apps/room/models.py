from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=150)
    number = models.IntegerField()
    seats = models.IntegerField()
    image = models.ImageField(upload_to="src/apps/room/static/images/room", blank=True, null=True)

