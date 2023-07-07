from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    number = models.IntegerField()
    seats = models.IntegerField()
    image = models.ImageField(upload_to="src/apps/room/media/images/room", blank=True, null=True)
