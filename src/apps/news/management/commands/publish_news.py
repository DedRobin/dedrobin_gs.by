from django.core.management.base import BaseCommand

from src.apps.news.models import News


class Command(BaseCommand):
    help = "Make all news published"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Make all news published",
        )

    def handle(self, *args, **options):
        news = News.objects.filter(is_published=False)
        number = news.update(is_published=True)
        print("{0} news have been published".format(number))
