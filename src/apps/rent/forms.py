from django import forms
from django.core.exceptions import ValidationError

SORT_BY = (
    ("asc", "Ascending"),
    ("desc", "Descending"),
)
IS_COMPLETED = (
    ("yes", "Yes"),
    ("no", "No"),
)


class RentConsoleForm(forms.Form):
    days = forms.IntegerField(min_value=1, label="How many days would you like to rent the console?")
    comment = forms.CharField(required=False)


class ConsoleFilterForm(forms.Form):
    order_by_creation_date = forms.ChoiceField(choices=SORT_BY, widget=forms.RadioSelect, required=False)
    order_by_completed_date = forms.ChoiceField(choices=SORT_BY, widget=forms.RadioSelect, required=False)
    is_completed = forms.ChoiceField(choices=IS_COMPLETED, widget=forms.RadioSelect, required=False)


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
