from __future__ import annotations

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
            self,
            email,
            username,
            password: str = None,
            is_staff: bool = False,
            is_superuser: bool = False,
    ) -> CustomUser | None:
        if email is None:
            raise ValueError("Users must have an email")
        if username is None:
            raise ValueError("Users must have an username")

        user = self.model(
            email=email,
            username=username,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )
        user.set_password(password)
        user.save()

        return user

    def create_staffuser(self, email: str, username: str, password: str):
        return self.create_user(
            email=email, username=username, password=password, is_staff=True
        )

    def create_superuser(self, email: str, username: str, password: str):
        return self.create_user(
            email=email, username=username, password=password, is_staff=True, is_superuser=True
        )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    username = models.CharField(max_length=150, unique=True, db_index=True)
    email = models.EmailField(max_length=150, unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()
