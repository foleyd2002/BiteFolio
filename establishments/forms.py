from django import forms
from .models import Establishment

class EstablishmentForm(forms.ModelForm):
    class Meta:
        model = Establishment
        fields = ['name', 'county', 'town', 'type', 'rating', 'visited_at']
        widgets = {
            'visited_at': forms.DateInput(attrs={'type': 'date'}),
        }
