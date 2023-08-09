from django.db import models
from django.core.validators import MinValueValidator

from src.apps.user.models import CustomUser

PRODUCT_TYPES = (
    ("mouse", "Mouse"),
    ("keyboard", "Keyboard"),
    ("headphone", "Headphone"),
)


class Product(models.Model):
    name = models.CharField(max_length=150)
    product_type = models.CharField(choices=PRODUCT_TYPES, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.URLField(db_index=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Product {self.product_type} '{self.name}'"


class Purchase(models.Model):
    quantity = models.IntegerField(validators=[MinValueValidator(limit_value=1)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="purchases")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="purchases")

    def __str__(self):
        return f"Purchase '{self.product.name}' for {self.user.username}'"
