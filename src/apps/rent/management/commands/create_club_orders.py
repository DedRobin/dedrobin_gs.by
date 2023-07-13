import random
from django.core.management.base import BaseCommand

from src.apps.rent.models import ClubRent, Club
from src.apps.user.models import CustomUser
from src.apps.rent.factories import ClubRentFactory
from src.apps.user.factories import UserFactory
from src.apps.rent.factories import ClubFactory


class Command(BaseCommand):
    help = "Create club orders"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Create club orders",
        )

    def handle(self, *args, **options):
        clear = options.get("clear")
        if clear:
            ClubRent.objects.all().delete()
        count = 0
        users = CustomUser.objects.all()
        if not users:
            users = UserFactory.create_batch(size=5)
        clubs = Club.objects.all()
        if not clubs:
            clubs = ClubFactory.create_batch(size=5)
        for club in clubs:
            ClubRentFactory.create_batch(size=3, club=club, user=random.choice(users))
            count += 1

        print(f"{count} club orders have been created")
