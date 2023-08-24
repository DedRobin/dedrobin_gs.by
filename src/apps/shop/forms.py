from django import forms

from src.apps.shop.models import PRODUCT_TYPES
from src.apps.address.models import Address
from src.apps.profile.models import Profile
from src.apps.profile.validators import check_phone_number

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


class OrderAddressAnonymousForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ("user",)


class OrderAddressForm(forms.Form):
    class Meta:
        fields = ("address",)

    def __init__(self, queryset, *args, **kwargs):
        super(OrderAddressForm, self).__init__(*args, **kwargs)
        self.fields["address"] = forms.ModelChoiceField(queryset=queryset, required=True)


class OrderProfileForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    phone_number = forms.CharField(max_length=150, validators=[check_phone_number])


class PurchaseFilterForm(forms.Form):
    name = forms.CharField(required=False, max_length=150)
    order_by_date = forms.ChoiceField(choices=ORDER_BY, required=False, widget=forms.RadioSelect)
