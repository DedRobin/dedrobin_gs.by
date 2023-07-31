from django.db import models


class Product(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    release_date = models.DateField()
    image = models.URLField(blank=True, null=True)


class Mouse(Product):
    interface = models.CharField(max_length=100, blank=True, null=True)
    sensor_type = models.CharField(max_length=100, blank=True, null=True)
    max_sensor_resolution = models.CharField(max_length=100, blank=True, null=True)
    length_radius = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Mouse '{self.name}'"
