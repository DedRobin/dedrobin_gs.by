from django import forms


class RentConsoleForm(forms.Form):
    days = forms.IntegerField(min_value=1, label="How many days would you like to rent the console?")
    comment = forms.CharField(required=False)
