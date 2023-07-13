from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from src.apps.rent.models import Club, ClubAddress
from src.apps.rent.factories import ClubFactory


class Command(BaseCommand):
    help = "Create clubs"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Create consoles",
        )

    def handle(self, *args, **options):
        clear = options.get("clear")
        if clear:
            Club.objects.all().delete()
            ClubAddress.objects.all().delete()
        count = 0
        try:
            while count < 5:
                ClubFactory()
                count += 1
        except IntegrityError:
            ClubFactory()

        print(f"{count} clubs objects have been created")
