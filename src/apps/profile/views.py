from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from src.apps.profile.queries import select_profile_for_user, update_profile
from src.apps.profile.services import convert_to_dict
from src.apps.profile.forms import ProfileForm
from src.apps.user.queries import update_user
from src.apps.user.forms import UserForm


def edit_profile(request: WSGIRequest):
    """Edit a specific user profile"""

    contex = {}
    profile = select_profile_for_user(user=request.user)
    user = profile.user

    if request.method == "POST":
        profile_form = ProfileForm(data=request.POST)
        user_form = UserForm(data=request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            profile_data = profile_form.cleaned_data
            user_data = user_form.cleaned_data
            profile = update_profile(profile=profile, data=profile_data)
            user = update_user(user=user, data=user_data)
            contex["message"] = "Your data has been updated"
            # return render(request, "edit_profile.html", contex)

    profile_data = convert_to_dict(model=profile)
    user_data = convert_to_dict(model=user)
    user_form = UserForm(data=user_data)
    profile_form = ProfileForm(data=profile_data)
    contex["user_form"] = user_form
    contex["profile_form"] = profile_form
    return render(request, "edit_profile.html", contex)
