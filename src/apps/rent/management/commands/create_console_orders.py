import random
from django.core.management.base import BaseCommand

from src.apps.rent.models import ConsoleRent, Console
from src.apps.user.models import CustomUser
from src.apps.rent.factories import ConsoleRentFactory, ConsoleFactory
from src.apps.user.factories import UserFactory


class Command(BaseCommand):
    help = "Create console orders"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Create console orders",
        )

    def handle(self, *args, **options):
        clear = options.get("clear")
        if clear:
            ConsoleRent.objects.all().delete()
        count = 0
        users = CustomUser.objects.all()
        if not users:
            users = UserFactory.create_batch(size=5)
        consoles = Console.objects.all()
        if not consoles:
            consoles = ConsoleFactory.create_batch(size=5)
        for console in consoles:
            ConsoleRentFactory.create_batch(size=3, console=console, user=random.choice(users))
            count += 3

        print(f"{count} console orders have been created")
