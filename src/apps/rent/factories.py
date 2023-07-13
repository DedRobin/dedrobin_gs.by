import factory.fuzzy
from factory.django import DjangoModelFactory

from src.apps.rent.models import Club, ClubAddress, Console, Room, ClubRent, RoomRent, ConsoleRent
from src.apps.user.models import CustomUser


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
    seats = factory.Faker("pyint")


class ClubRentFactory(DjangoModelFactory):
    class Meta:
        model = ClubRent

    comment = factory.Faker("text")
    club = factory.SubFactory(ClubFactory)
    user = factory.SubFactory(CustomUser)


class RoomRentFactory(DjangoModelFactory):
    class Meta:
        model = RoomRent

    comment = factory.Faker("text")
    room = factory.SubFactory(RoomFactory)
    user = factory.SubFactory(CustomUser)


class ConsoleRentFactory(DjangoModelFactory):
    class Meta:
        model = ConsoleRent

    comment = factory.Faker("text")
    console = factory.SubFactory(ConsoleFactory)
    user = factory.SubFactory(CustomUser)
