from django.forms import ModelForm
from django import forms

from .models import Ambulance, Province, District

class AmbulanceCreateForm(ModelForm):
    province = forms.ModelChoiceField(queryset=Province.objects.all())
    class Meta:
        model = Ambulance
        fields = ("province", "user", "district", "city", "ward_name", "ward_no", "name", "owner_name", "owner_email", "phone_number", "telephone_number")