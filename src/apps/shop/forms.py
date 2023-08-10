from django import forms

from src.apps.shop.models import PRODUCT_TYPES

ORDER_BY = (
    ("asc", "Ascending"),
    ("desc", "Descending"),
)


class ProductFilterForm(forms.Form):
    name = forms.CharField(required=False, max_length=150)
    product_type = forms.ChoiceField(required=False, choices=PRODUCT_TYPES, widget=forms.RadioSelect)


class PurchaseForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    comment = forms.CharField(required=False)


class PurchaseFilterForm(forms.Form):
    name = forms.CharField(required=False, max_length=150)
    order_by_date = forms.ChoiceField(choices=ORDER_BY, required=False, widget=forms.RadioSelect)
