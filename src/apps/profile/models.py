from django.db import models
from src.apps.user.models import CustomUser
from src.apps.profile.validators import check_phone_number

GENDER = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
)


class Profile(models.Model):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(choices=GENDER, blank=True, null=True)
    phone_number = models.CharField(max_length=150, blank=True, null=True, validators=[check_phone_number])
    age = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="profile/media/", blank=True, null=True)

    # Foreign key
    user = models.ForeignKey(CustomUser, related_name="profile", on_delete=models.CASCADE, db_index=True, null=True)

    def __str__(self):
        if self.user:
            message = f"{self.first_name} {self.last_name}"
        else:
            message = f"{self.first_name} {self.last_name} (Not registered)"
        return message
