from django.core.validators import MinValueValidator
from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

from src.apps.user.models import CustomUser


class ClubAddress(models.Model):
    class Meta:
        verbose_name_plural = "Club addresses"

    city = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    building = models.IntegerField()

    def __str__(self):
        return f"{self.city}, {self.street}, {self.building}"


class Club(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    description = models.TextField()
    address = models.ForeignKey(ClubAddress, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="src/apps/rent/media/images/club", blank=True, null=True)

    def __str__(self):
        return f"Club '{self.name}'"


class Console(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    price_per_day = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="src/apps/rent/media/images/console", blank=True, null=True)

    def __str__(self):
        return f"Console '{self.name}'"


class Room(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    number = models.IntegerField()
    seats = models.IntegerField()
    image = models.ImageField(upload_to="src/apps/rent/media/images/room", blank=True, null=True)

    def __str__(self):
        return f"Room '{self.name}'"


class Rent(models.Model):
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, blank=True, null=True)
    is_completed = models.BooleanField(default=False, blank=True, null=True)
    completed_date = models.DateTimeField(db_index=True, blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, **kwargs):
        if self.is_completed:
            self.completed_date = datetime.now()
        super().save(**kwargs)


class ConsoleRent(Rent):
    days = models.IntegerField(blank=True, null=True)

    console = models.ForeignKey(Console, on_delete=models.PROTECT, related_name="rented_consoles")
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="rented_consoles")

    def __str__(self):
        return f"ConsoleOrder for the {self.console.name} ({self.user.username})"


class RoomRent(Rent):
    hours = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(limit_value=1)])
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="rented_rooms")

    people = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(limit_value=1)])
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="rented_rooms")

    def clean(self):
        if self.room.seats < self.people:
            error_text = "The number of people is more than the number of seats \n(Seats={0} < People={1})"
            raise ValidationError(error_text.format(self.room.seats, self.people))

    def __str__(self):
        return f"RoomOrder for the {self.room.name} ({self.user.username})"


class ClubRent(Rent):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="rented_clubs", null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="rented_clubs", null=True)

    def __str__(self):
        return f"ClubOrder for the {self.club.name} ({self.user.username})"
