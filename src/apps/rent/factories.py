import factory.fuzzy
from factory.django import DjangoModelFactory

from src.apps.rent.models import Club, ClubAddress, Console


class ConsoleFactory(DjangoModelFactory):
    class Meta:
        model = Console

    price_per_day = factory.Faker("pydecimal", right_digits=2, positive=True, min_value=10, max_value=1000)


class ClubAddressFactory(DjangoModelFactory):
    class Meta:
        model = ClubAddress

    city = factory.Faker("city")
    street = factory.Faker("street_name")
    building = factory.Faker("building_number")


class ClubFactory(DjangoModelFactory):
    class Meta:
        model = Club

    name = factory.Faker("color_name")
    description = factory.Faker("text")
    address = factory.SubFactory(ClubAddressFactory)
