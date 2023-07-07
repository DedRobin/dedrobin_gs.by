from django.db import models


class ClubAddress(models.Model):
    city = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    building = models.IntegerField()


class Club(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    description = models.TextField()
    address = models.ForeignKey(ClubAddress, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="src/apps/club/media/images/club", blank=True, null=True)
