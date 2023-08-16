from src.apps.profile.models import Profile


def update_profile(profile: Profile, data: dict) -> Profile:
    profile.first_name = data["first_name"]
    profile.last_name = data["last_name"]
    profile.gender = data["gender"]
    profile.phone_number = data["phone_number"]
    profile.age = data["age"]
    profile.birthday = data["birthday"]
    if data.get("photo"):
        profile.photo = data["photo"]
    profile.save()
    return profile
