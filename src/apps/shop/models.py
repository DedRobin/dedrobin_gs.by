from django.db import models


class Product(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    release_date = models.DateField()


class Mouse(Product):
    interface = models.CharField(max_length=100)
    sensor_type = models.CharField(max_length=100)
    max_sensor_resolution = models.CharField(max_length=100)
    length_radius = models.CharField(max_length=100)

    def __str__(self):
        return f"Mouse '{self.name}'"
