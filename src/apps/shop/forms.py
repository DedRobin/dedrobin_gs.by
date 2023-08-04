from django import forms


class PurchaseForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    comment = forms.CharField(required=False)
