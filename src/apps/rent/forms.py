from django import forms

from src.apps.rent.models import ConsoleRent, ClubRent, RoomRent

SORT_BY = (
    ("asc_by_creation_date", "Ascending by the creation date"),
    ("desc_by_creation_date", "Descending by the creation date"),
    ("asc_by_completed_date", "Ascending by the completed date"),
    ("desc_by_completed_date", "Descending by the completed date"),
)
IS_COMPLETED = (
    ("yes", "Yes"),
    ("no", "No"),
)


class RentConsoleForm(forms.Form):
    days = forms.IntegerField(min_value=1, label="How many days would you like to rent the console?")
    comment = forms.CharField(required=False)


class RentRoomForm(forms.Form):
    comment = forms.CharField(required=False)
    hours = forms.IntegerField()
    people = forms.IntegerField()

    def __init__(self, **kwargs):
        max_seats = kwargs.pop("max_seats", None)
        super(RentRoomForm, self).__init__(**kwargs)
        if max_seats:
            self.fields["people"] = forms.IntegerField(max_value=max_seats)


class RentClubForm(forms.Form):
    comment = forms.CharField(required=False)


class RentFilterForm(forms.Form):
    order_by = forms.ChoiceField(
        label="Sort by creation or completed date",
        choices=SORT_BY,
        widget=forms.RadioSelect,
        required=False
    )
    is_completed = forms.ChoiceField(choices=IS_COMPLETED, widget=forms.RadioSelect, required=False)


class ConsoleRentAdminForm(forms.ModelForm):
    class Meta:
        model = ConsoleRent
        widgets = {
            "is_completed": forms.CheckboxInput
        }
        fields = "__all__"


class ClubRentAdminForm(forms.ModelForm):
    class Meta:
        model = ClubRent
        widgets = {
            "is_completed": forms.CheckboxInput
        }
        fields = "__all__"


class RoomRentAdminForm(forms.ModelForm):
    class Meta:
        model = RoomRent
        widgets = {
            "is_completed": forms.CheckboxInput
        }
        fields = "__all__"
