from django import forms
from .models import Stock

class SearchForm(forms.Form):
    search_word = forms.CharField(label = 'Search Stock')