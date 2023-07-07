from django.db import models


class Console(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    price_per_day = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="src/apps/console/media/images/console", blank=True, null=True)

    def __str__(self):
        return self.name
