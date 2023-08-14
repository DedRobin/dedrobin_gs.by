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
    user = models.ForeignKey(CustomUser, related_name="profile", on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile for user '{self.user.username}' ({self.user.email}))"
