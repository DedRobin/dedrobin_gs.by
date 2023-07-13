from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from src.apps.rent.models import Room
from src.apps.rent.factories import RoomFactory


class Command(BaseCommand):
    help = "Create rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Create rooms",
        )

    def handle(self, *args, **options):
        clear = options.get("clear")
        if clear:
            Room.objects.all().delete()
        rooms = RoomFactory.create_batch(size=5)
        print(f"{len(rooms)} rooms objects have been created")
