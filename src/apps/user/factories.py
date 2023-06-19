import factory.fuzzy
from factory.django import DjangoModelFactory
from src.apps.user.models import CustomUser


class UserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.Faker("user_name")
    email = factory.Faker("email")
