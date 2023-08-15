from django.shortcuts import render, redirect, HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from src.apps.profile.queries import select_profile_for_user, update_profile
from src.apps.profile.services import convert_to_dict
from src.apps.profile.forms import ProfileForm
from src.apps.user.queries import update_user, delete_user
from src.apps.user.forms import UserForm


@login_required(redirect_field_name="", login_url="login")
def edit_profile(request: WSGIRequest):
    """Edit a specific user profile"""

    contex = {}
    user = request.user
    profile = select_profile_for_user(user=request.user)

    if request.method == "POST":
        profile_form = ProfileForm(data=request.POST)
        user_form = UserForm(data=request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            profile_updated_data = profile_form.cleaned_data
            user_updated_data = user_form.cleaned_data
            profile = update_profile(profile=profile, data=profile_updated_data)
            try:
                user = update_user(user=user, data=user_updated_data)
            except AssertionError:
                contex["error"] = "The two passwords doesn't match"
            except ValueError as ex:
                contex["error"] = ex
            else:
                contex["message"] = "Your data has been updated"
        else:
            contex["error"] = user_form.errors or profile_form.errors
    profile_updated_data = convert_to_dict(model=profile)
    user_updated_data = convert_to_dict(model=user)
    user_form = UserForm(data=user_updated_data)
    profile_form = ProfileForm(data=profile_updated_data)
    contex["profile"] = profile
    contex["user_form"] = user_form
    contex["profile_form"] = profile_form
    return render(request, "edit_profile.html", contex)


@login_required(redirect_field_name="", login_url="login")
def delete_profile(request: WSGIRequest):
    """Delete a specific user at all"""

    if request.method == "POST":
        delete_user(user=request.user)
        logout(request)
        return redirect("login")
    return HttpResponse(status=405)
