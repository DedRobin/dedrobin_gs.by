from django.db import models

from src.apps.console.models import Console
from src.apps.room.models import Room
from src.apps.club.models import Club
from src.apps.user.models import CustomUser


class ConsoleOrder(models.Model):
    console = models.ForeignKey(Console, on_delete=models.PROTECT, related_name="orders")
    description = models.TextField()
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)

    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    def __str__(self):
        return f"ConsoleOrder for the {self.console.name} ({self.user.username})"


class RoomOrder(models.Model):
    room = models.ForeignKey(Room, on_delete=models.PROTECT, related_name="orders")
    description = models.TextField()
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)

    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    def __str__(self):
        return f"RoomOrder for the {self.room.name} ({self.user.username})"


class ClubOrder(models.Model):
    club = models.ForeignKey(Club, on_delete=models.PROTECT, related_name="orders")
    description = models.TextField()
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)

    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    def __str__(self):
        return f"ClubOrder for the {self.club.name} ({self.user.username})"
