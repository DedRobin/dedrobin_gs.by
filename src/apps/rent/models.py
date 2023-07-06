from django.db import models
from src.apps.console.models import Console
from src.apps.room.models import Room
from src.apps.club.models import Club


class ConsoleOrder(models.Model):
    console = models.ForeignKey(Console, on_delete=models.PROTECT, related_name="orders")
    description = models.TextField()


class RoomOrder(models.Model):
    room = models.ForeignKey(Room, on_delete=models.PROTECT, related_name="orders")
    description = models.TextField()


class ClubOrder(models.Model):
    club = models.ForeignKey(Club, on_delete=models.PROTECT, related_name="orders")
    description = models.TextField()
