from django.db import models

from src.apps.user.models import CustomUser


class ClubAddress(models.Model):
    city = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    building = models.IntegerField()


class Club(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    description = models.TextField()
    address = models.ForeignKey(ClubAddress, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="src/apps/rent/media/images/club", blank=True, null=True)


class Console(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    price_per_day = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="src/apps/rent/media/images/console", blank=True, null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    number = models.IntegerField()
    seats = models.IntegerField()
    image = models.ImageField(upload_to="src/apps/rent/media/images/room", blank=True, null=True)


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
