from django.db.models import Count

from src.apps.user.models import CustomUser


class OrderCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            r_console_count = Count("rented_consoles", distinct=True)
            r_club_count = Count("rented_clubs", distinct=True)
            r_room_count = Count("rented_rooms", distinct=True)

            result = CustomUser.objects.filter(pk=request.user.id).aggregate(
                rented_thing_count=(r_console_count + r_club_count + r_room_count)
            )
            request.rented_thing_count = result["rented_thing_count"]

        response = self.get_response(request)
        return response
