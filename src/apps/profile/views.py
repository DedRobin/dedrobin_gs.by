from django.shortcuts import render, redirect, HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from src.apps.profile.queries import update_profile
from src.apps.profile.services import uploaded_photo
from src.apps.profile.forms import ProfileForm
from src.apps.user.queries import update_user, delete_user
from src.apps.user.forms import UserForm


@login_required(redirect_field_name="", login_url="login")
def edit_profile(request: WSGIRequest):
    """Edit a specific user profile"""

    contex = {}
    user = request.user
    profile = request.user_profile

    if request.method == "POST":
        profile_form = ProfileForm(data=request.POST)
        user_form = UserForm(data=request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            profile_updated_data = profile_form.cleaned_data
            user_updated_data = user_form.cleaned_data
            if request.FILES.get("photo"):
                if profile.photo.name:
                    photo_path = uploaded_photo(photo=request.FILES["photo"], path=profile.photo.url)
                else:
                    photo_name = request.FILES["photo"].name
                    photo_path = uploaded_photo(photo=request.FILES["photo"], path=f"profile/media/{photo_name}")
                if photo_path:
                    profile_updated_data["photo"] = photo_path
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

    user_form = UserForm(data={"username": user.username, "email": user.email})
    profile_form = ProfileForm(data=profile.__dict__)
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
