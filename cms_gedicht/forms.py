from django import forms

from .models import Bestellung

class BestellungForm(forms.ModelForm):
    class Meta:
        model = Bestellung
        fields = ['name']
