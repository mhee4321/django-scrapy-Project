from django import forms
from .models import News

class RefreshForm(forms.Form):
    forms = News

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label = 'Search News')