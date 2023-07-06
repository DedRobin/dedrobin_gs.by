from django.db import models


class Console(models.Model):
    name = models.CharField(max_length=150)
    price_per_hour = models.DecimalField()
    price_per_month = models.DecimalField()
