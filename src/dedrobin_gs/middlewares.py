from django.db.models import Count

from src.apps.rent.models import RoomRent, ConsoleRent, ClubRent
from src.apps.user.models import CustomUser


class OrderCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # result = CustomUser.objects.filter(pk=request.user.id).aggregate(
            #     rented_thing_count=(
            #             Count("rented_consoles") + Count("rented_clubs") + Count("rented_rooms")
            #     )
            # )

            # request.rented_thing_count = result["rented_thing_count"]
            result = CustomUser.objects.prefetch_related("test").filter(pk=request.user.id).first()
            # consoles = result.rented_consoles
            print()

        response = self.get_response(request)
        return response
