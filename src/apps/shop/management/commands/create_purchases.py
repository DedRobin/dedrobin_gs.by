import random
from django.core.management.base import BaseCommand

from src.apps.shop.models import Purchase
from src.apps.shop.factories import PurchaseFactory
from src.apps.user.models import CustomUser


class Command(BaseCommand):
    help = "Create purchases"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Create purchases",
        )

    def handle(self, *args, **options):
        clear = options.get("clear")
        if clear:
            Purchase.objects.all().delete()
        count = 0
        users = CustomUser.objects.all()
        while count < 5:
            if users:
                PurchaseFactory(user=random.choice(users))
            else:
                PurchaseFactory()
            count += 1

        print(f"{count} purchases objects have been created")
