from __future__ import annotations

from django.contrib.auth.backends import BaseBackend
from django.http import HttpRequest

from src.apps.user.models import CustomUser


class EmailAuthBackend(BaseBackend):
    def authenticate(
            self, request: HttpRequest, email: str = None, password: str = None
    ) -> CustomUser | None:
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return

    def get_user(self, user_id: int) -> CustomUser | None:
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return
