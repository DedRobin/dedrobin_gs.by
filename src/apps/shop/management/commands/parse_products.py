from django.core.management.base import BaseCommand

from src.apps.shop.services import run_parser


class Command(BaseCommand):
    help = "Crawl products from 'onliner.by'"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Clear all products",
        )

    def handle(self, *args, **options):
        clear = options.get("clear")
        # run_parser.delay(clear)
        run_parser(clear)
