import random
import factory.fuzzy
from factory.django import DjangoModelFactory

from src.apps.shop.models import Product, Purchase, PRODUCT_TYPES
from src.apps.user.factories import UserFactory

product_types = [p_type[0] for p_type in PRODUCT_TYPES]


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("word")
    product_type = random.choice(product_types)
    price = factory.Faker("pydecimal", right_digits=2, positive=True, min_value=10, max_value=1000)
    description = factory.Faker("text")


class PurchaseFactory(DjangoModelFactory):
    class Meta:
        model = Purchase

    quantity = factory.Faker("pyint", min_value=1, max_value=10)
    comment = factory.Faker("text")

    user = factory.SubFactory(UserFactory)
    product = factory.SubFactory(ProductFactory)
