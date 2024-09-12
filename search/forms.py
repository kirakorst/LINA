from django import forms
from .models import SearchQuery

class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchQuery
        fields = ['query']
        widgets = {
            'query': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите поисковый запрос'
            })
        }