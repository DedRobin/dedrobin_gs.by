from django.core.management.base import BaseCommand

from src.apps.rent.models import Console
from src.apps.rent.factories import ConsoleFactory


class Command(BaseCommand):
    help = "Create consoles"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Create consoles",
        )

    def handle(self, *args, **options):
        clear = options.get("clear")
        if clear:
            Console.objects.all().delete()
        consoles = []
        console_name = ["PlayStation 4", "Nintendo Switch", "Steam Deck", "Xbox Series X"]
        for name in console_name:
            console = ConsoleFactory.build(name=name)
            if not Console.objects.filter(name=console.name).exists():
                consoles.append(console)
        Console.objects.bulk_create(consoles)
        print(f"{len(consoles)} console objects have been created")
