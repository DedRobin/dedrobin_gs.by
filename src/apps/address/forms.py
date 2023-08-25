from django import forms

from src.apps.address.models import Address


class OrderAddressAnonymousForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ("user",)


class OrderAddressForm(forms.Form):
    class Meta:
        fields = ("address",)

    def __init__(self, queryset=None, *args, **kwargs):
        super(OrderAddressForm, self).__init__(*args, **kwargs)
        if queryset:
            self.fields["address"] = forms.ModelChoiceField(queryset=queryset, required=True)
        else:
            self.fields["address"] = forms.IntegerField(required=True)
