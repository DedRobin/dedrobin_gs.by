import factory.fuzzy
from factory.django import DjangoModelFactory

from src.apps.console.models import Console


class ConsoleFactory(DjangoModelFactory):
    class Meta:
        model = Console

    price_per_hour = factory.Faker("pydecimal", right_digits=2, positive=True, min_value=10, max_value=1000)
    price_per_month = factory.Faker("pydecimal", right_digits=2, positive=True, min_value=10, max_value=1000)
