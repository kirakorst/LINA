from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import entries

class EntriesForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = entries
        fields = ['body']