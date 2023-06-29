from django import forms

from src.apps.news.models import Company


class NewsFilterForm(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=False)
