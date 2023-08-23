from django import forms

from src.apps.shop.models import PRODUCT_TYPES
from src.apps.address.models import Address

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


TEST_CHOICE = (
    ("TEST0", 0),
    ("TEST1", 1),
    ("TEST2", 2),
)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Address
        # fields = "__all__"
        exclude = ("user",)

# class OrderForm(forms.Form):
# address_from_exist = forms.ChoiceField(choices=TEST_CHOICE, required=False)
# city = forms.CharField()
# street = forms.ChoiceField()
# building = forms.CharField()
# flet = forms.IntegerField()
# floor = forms.IntegerField(required=False)
# entrance = forms.IntegerField(required=False)
# preferred_time = forms.TimeField(required=False)
# comment = forms.CharField(required=False)


class PurchaseFilterForm(forms.Form):
    name = forms.CharField(required=False, max_length=150)
    order_by_date = forms.ChoiceField(choices=ORDER_BY, required=False, widget=forms.RadioSelect)
