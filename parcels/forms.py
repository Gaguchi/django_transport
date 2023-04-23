from django import forms
from .models import Parcel

class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ['recipient', 'pickup_city', 'dropoff_city']
