from django.db import models


class Console(models.Model):
    name = models.CharField(max_length=150)
    price_per_hour = models.DecimalField(max_digits=5, decimal_places=2)
    price_per_month = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="src/apps/console/static/images/console", blank=True, null=True)

    def __str__(self):
        return self.name
