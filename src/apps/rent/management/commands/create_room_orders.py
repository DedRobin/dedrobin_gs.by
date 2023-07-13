import random
from django.core.management.base import BaseCommand

from src.apps.rent.models import RoomRent, Room
from src.apps.user.models import CustomUser
from src.apps.user.factories import UserFactory
from src.apps.rent.factories import RoomFactory, RoomRentFactory


class Command(BaseCommand):
    help = "Create room orders"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Create room orders",
        )

    def handle(self, *args, **options):
        clear = options.get("clear")
        if clear:
            RoomRent.objects.all().delete()
        count = 0
        users = CustomUser.objects.all()
        if not users:
            users = UserFactory.create_batch(size=5)
        rooms = Room.objects.all()
        if not rooms:
            rooms = RoomFactory.create_batch(size=5)
        for room in rooms:
            RoomRentFactory.create_batch(size=3, room=room, user=random.choice(users))
            count += 1

        print(f"{count} room orders have been created")
