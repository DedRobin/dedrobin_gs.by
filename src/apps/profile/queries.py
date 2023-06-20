from src.apps.profile.models import Profile
from src.apps.user.models import CustomUser


def select_profile_for_user(user: CustomUser) -> Profile:
    profile = Profile.objects.get_or_create(user=user)[0]
    return profile


def update_profile(profile: Profile, data: dict) -> Profile:
    profile.first_name = data["first_name"]
    profile.last_name = data["last_name"]
    profile.gender = data["gender"]
    profile.phone_number = data["phone_number"]
    profile.age = data["age"]
    profile.birthday = data["birthday"]
    profile.save()
    return profile
