import factory.fuzzy
from factory.django import DjangoModelFactory

from src.apps.rent.models import Club, ClubAddress, Console, Room, ClubRent, RoomRent, ConsoleRent
from src.apps.user.factories import UserFactory


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


class RoomFactory(DjangoModelFactory):
    class Meta:
        model = Room

    name = factory.Faker("color_name")
    number = factory.Faker("pyint")
    seats = factory.Faker("pyint", min_value=5, max_value=10)


class ClubRentFactory(DjangoModelFactory):
    class Meta:
        model = ClubRent

    comment = factory.Faker("text")
    club = factory.SubFactory(ClubFactory)
    user = factory.SubFactory(UserFactory)
    is_completed = factory.Faker("pybool")


class RoomRentFactory(DjangoModelFactory):
    class Meta:
        model = RoomRent

    comment = factory.Faker("text")
    hours = factory.Faker("pyint", min_value=1, max_value=24)
    people = factory.Faker("pyint", min_value=1, max_value=10)
    is_completed = factory.Faker("pybool")

    room = factory.SubFactory(RoomFactory)
    user = factory.SubFactory(UserFactory)


class ConsoleRentFactory(DjangoModelFactory):
    class Meta:
        model = ConsoleRent

    comment = factory.Faker("text")
    days = factory.Faker("pyint", min_value=1, max_value=31)
    is_completed = factory.Faker("pybool")

    console = factory.SubFactory(ConsoleFactory)
    user = factory.SubFactory(UserFactory)
