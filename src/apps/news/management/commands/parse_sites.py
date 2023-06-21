from django.core.management.base import BaseCommand

from src.apps.news.services import run_parser


class Command(BaseCommand):
    help = "Crawl sites"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Test clear",
        )

    def handle(self, *args, **options):
        clear = options.get("clear")
        # run_parser.delay(clear)
        run_parser(clear)
