from rest_framework import serializers
from ambulance_details.models import Ambulance, District, Province

class AmbulanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambulance
        fields = ("user", "district", "city", "ward_name", "ward_no", "name", "owner_name", "owner_email", "phone_number", "telephone_number")
    
# class WardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ward
#         fields = ['city', 'name', 'no']

# class CitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = City
#         fields = ['district', 'name']

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['province', 'name']

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['no']