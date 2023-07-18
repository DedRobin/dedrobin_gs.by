from django import forms

from src.apps.news.models import Company

SORT_BY = (
    ("desc", "Desc"),
    ("asc", "Asc"),
)


class NewsFilterForm(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=False)
    sort_by_date = forms.ChoiceField(choices=SORT_BY, widget=forms.RadioSelect, required=False)
    date_from = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date"}))
    date_to = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date"}))
