from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
import requests

from .serializers import AmbulanceSerializer, DistrictSerializer, ProvinceSerializer
from ambulance_details.models import Ambulance, District, Province

class ListCreateAmbulance(generics.ListCreateAPIView):
    serializer_class = AmbulanceSerializer

    def get_queryset(self):
        queryset = Ambulance.objects.filter(ward=self.kwargs['ward'])
        return queryset
    
    def post(self, request, **kwargs):
        ambulance = request.data.get('ambulance')
        serializer = AmbulanceSerializer(data=ambulance)
        if serializer.is_valid(raise_exception=True):
            ambulance_saved = serializer.save()
        return Response({"success": "Ambulance '{}' detail created successfully".format(ambulance_saved.name)})

class RetrieveUpdateDeleteAmbulance(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AmbulanceSerializer

    def get_queryset(self):
        queryset = Ambulance.objects.filter(ward=self.kwargs['ward'])
        return queryset

    def put(self, request, pk, **kwargs):
        saved_ambulance = get_object_or_404(Ambulance.objects.all(), pk=pk)
        data = request.data.get('ambulance')
        serializer = AmbulanceSerializer(instance=saved_ambulance, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            ambulance_saved = serializer.save()
        return Response({"success": "Ambulance '{}' detail created successfully".format(ambulance_saved.name)})

# class ListWard(generics.ListAPIView):
#     serializer_class = WardSerializer
    
#     def get_queryset(self):
#         queryset = Ward.objects.filter(city__name=self.kwargs['city'])
#         return queryset

# class ListCity(generics.ListAPIView):
#     serializer_class = CitySerializer
    
#     def get_queryset(self):
#         queryset = City.objects.filter(district__name=self.kwargs['district'])
#         return queryset

class ListDistrict(generics.ListAPIView):
    serializer_class = DistrictSerializer
    
    def get_queryset(self):
        queryset = District.objects.filter(province__no=self.kwargs['province'])
        return queryset

class ListProvince(generics.ListAPIView):
    serializer_class = ProvinceSerializer
    queryset = Province.objects.all()
