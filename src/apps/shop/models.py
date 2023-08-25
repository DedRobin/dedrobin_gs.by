from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator
from django.shortcuts import reverse

from src.apps.user.models import CustomUser
from src.apps.address.models import Address
from src.apps.profile.models import Profile

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

    def get_absolute_url(self):
        return reverse(viewname="shop:about_product", kwargs={"product_id": self.id})


class Purchase(models.Model):
    quantity = models.IntegerField(validators=[MinValueValidator(limit_value=1)])
    comment = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name="purchases", null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="purchases")
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name="profiles", null=True, default=None)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name="purchases", null=True)

    def save(self, **kwargs):
        if self.is_completed:
            self.finished_at = datetime.now()
        super().save(**kwargs)

    def __str__(self):
        return f"Purchase '{self.product.name}' for {self.user.username}'"


class Basket(models.Model):
    products = models.ManyToManyField(Product, related_name="products")
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="basket")

    def product_quantity(self):
        return self.products.count()

    def __str__(self):
        return f"Basket №{self.id} - Owner '{self.user.username}'"
