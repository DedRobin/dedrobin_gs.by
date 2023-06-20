import random
import factory.fuzzy
from factory.django import DjangoModelFactory

from src.apps.profile.models import Profile, GENDER
from src.apps.user.factories import UserFactory

last_seven_numbers = random.randint(0, 9999999)
code = random.choice([25, 29, 33, 44])


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    gender = factory.fuzzy.FuzzyChoice([g[1] for g in GENDER])
    phone_number = "+375{0}{1:07d}".format(code, last_seven_numbers)
    age = factory.Faker("pyint", min_value=1, max_value=99)
    birthday = factory.Faker("date")
    user = factory.SubFactory(UserFactory)
