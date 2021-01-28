from django import forms
from .models import News

class RefreshForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    company = forms.CharField()
    saved_time = forms.CharField()

class SearchForm(forms.Form):
    search_word = forms.CharField(label = 'Search News')