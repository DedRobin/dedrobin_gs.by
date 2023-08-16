from django.db.models import Q, Count

from src.apps.user.models import CustomUser
from src.apps.profile.models import Profile


class ProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            profile = Profile.objects.get_or_create(user=request.user)[0]
            request.user_profile = profile
        response = self.get_response(request)
        return response


class OrderCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            r_console_count = Count("rented_consoles", distinct=True, filter=Q(rented_consoles__is_completed=False))
            r_club_count = Count("rented_clubs", distinct=True, filter=Q(rented_clubs__is_completed=False))
            r_room_count = Count("rented_rooms", distinct=True, filter=Q(rented_rooms__is_completed=False))

            result = CustomUser.objects.filter(pk=request.user.id).aggregate(
                rented_console_count=r_console_count,
                rented_club_count=r_club_count,
                rented_room_count=r_room_count,
            )
            request.rented_console_count = result["rented_console_count"]
            request.rented_club_count = result["rented_club_count"]
            request.rented_room_count = result["rented_room_count"]

            request.sum_count = result["rented_console_count"] + result["rented_club_count"] + result[
                "rented_room_count"]

        response = self.get_response(request)
        return response
