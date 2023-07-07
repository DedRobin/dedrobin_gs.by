from django.db import models

from src.apps.console.models import Console
from src.apps.room.models import Room
from src.apps.club.models import Club
from src.apps.user.models import CustomUser


class Order:
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)

    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)


class ConsoleOrder(Order, models.Model):
    console = models.ForeignKey(Console, on_delete=models.PROTECT, related_name="orders")
    days = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"ConsoleOrder for the {self.console.name} ({self.user.username})"


class RoomOrder(Order, models.Model):
    room = models.ForeignKey(Room, on_delete=models.PROTECT, related_name="orders")

    def __str__(self):
        return f"RoomOrder for the {self.room.name} ({self.user.username})"


class ClubOrder(Order, models.Model):
    club = models.ForeignKey(Club, on_delete=models.PROTECT, related_name="orders")

    def __str__(self):
        return f"ClubOrder for the {self.club.name} ({self.user.username})"
