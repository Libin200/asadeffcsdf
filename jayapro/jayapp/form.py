from django import forms
from jayapp.models import abijith,saaa

class abijithform(forms.ModelForm):
    class Meta:
        model=abijith
        fields="__all__"

class saaaform(forms.ModelForm):
    class Meta:
        model=saaa
        fields="__all__"