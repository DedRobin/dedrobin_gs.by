import factory.fuzzy
from factory.django import DjangoModelFactory

from src.apps.rent.models import Console


class ConsoleFactory(DjangoModelFactory):
    class Meta:
        model = Console

    price_per_day = factory.Faker("pydecimal", right_digits=2, positive=True, min_value=10, max_value=1000)
