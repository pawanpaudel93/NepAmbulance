from django.forms import ModelForm
from django import forms

from .models import Ambulance, District, Province


class AmbulanceCreateForm(ModelForm):
    class Meta:
        model = Ambulance
        fields = ("district", "city", "ward_name", "ward_no", "name", "owner_name", "owner_email",
                  "phone_number", "telephone_number")

    def __init__(self, province, *args, **kwargs):
        super(AmbulanceCreateForm, self).__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.filter(province__no=province).order_by('name')
