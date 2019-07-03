from django.shortcuts import render
from rest_framework import generics
from django.views import generic
import requests, json
from django.urls import reverse

# from .models import Ambulance, Ward, City, District, Province
from .models import Ambulance, District, Province
from .forms import AmbulanceCreateForm

## using apis
# class AmbulanceListCreate(generic.TemplateView):
#     template_name = 'ambulance_details/home.html'

#     def get(self, request, *args, **kwargs):
#         form = AmbulanceCreateForm()
#         ambulance = []
#         response = requests.get('http://127.0.0.1:8000/api/v1/ambulance/1/morang/urlabari/1/')
#         datas = response.json()
#         # print(datas)
#         for data in datas:
#             detail = {
#                 "user": data["user"], 
#                 "ward": data["ward"], 
#                 "name": data["name"],
#                 "owner_name": data["owner_name"],
#                 "owner_email": data["owner_email"],
#                 "phone_number": data["phone_number"],
#                 "telephone_number": data["telephone_number"]
#             }
#             ambulance.append(detail)
#         return render(request, self.template_name, {'datas': ambulance, 'form': form})
    
#     def post(self, request, *args, **kwargs):
#         form = AmbulanceCreateForm(request.POST)
#         try:
#             if form.is_valid():
#                 detail = {
#                 "user": request.user.pk, 
#                 "ward": form.cleaned_data["ward"].pk, 
#                 "name": form.cleaned_data["name"],
#                 "owner_name": form.cleaned_data["owner_name"],
#                 "owner_email": form.cleaned_data["owner_email"],
#                 "phone_number": form.cleaned_data["phone_number"]
#             }
#             headers = {'content-type': 'application/json'}
#             url = 'http://127.0.0.1:8000/api/v1/ambulance/1/morang/urlabari/1/'
#             data = {"ambulance": detail}
#             response = requests.post(url, data=json.dumps(data), headers=headers)
#             print(response)
#         except Exception as e:
#             print(e)
#         form = AmbulanceCreateForm()
#         ambulance = []
#         response = requests.get('http://127.0.0.1:8000/api/v1/ambulance/1/morang/urlabari/1/')
#         datas = response.json()
#         for data in datas:
#             detail = {
#                 "user": data["user"], 
#                 "ward": data["ward"], 
#                 "name": data["name"],
#                 "owner_name": data["owner_name"],
#                 "owner_email": data["owner_email"],
#                 "phone_number": data["phone_number"]
#             }
#             ambulance.append(detail)
#         return render(request, self.template_name, {'datas': ambulance, 'form': form})
class Home(generic.TemplateView):
    template_name = 'ambulance_details/home.html'

class ListProvinces(generic.TemplateView):
    template_name = 'ambulance_details/list_provinces.html'
  
    def get(self, request, *args, **kwargs):
        form = AmbulanceCreateForm()
        provinces = Province.objects.all()
        return render(request, self.template_name, {'provinces': provinces, 'form': form})
    
    def post(self, request, *args, **kwargs):
        form = AmbulanceCreateForm(request.POST)
        if form.is_valid():
            form.user = request.user.pk
            form.save()
        provinces = Province.objects.all()
        return render(request, self.template_name, {'provinces': provinces, 'form': form})


class ListDistricts(generic.ListView):
    template_name = 'ambulance_details/list_districts.html'
    context_object_name = 'districts'

    def get_queryset(self):
        return District.objects.filter(province__no=self.kwargs['province']).order_by('name')

# class ListCities(generic.ListView):
#     template_name = 'ambulance_details/list_cities.html'
#     context_object_name = 'cities'

#     def get_queryset(self):
#         return City.objects.filter(district__name=self.kwargs['district'])

# class ListWards(generic.ListView):
#     template_name = 'ambulance_details/list_wards.html'
#     context_object_name = 'wards'

#     def get_queryset(self):
#         return  Ward.objects.filter(city__name=self.kwargs['city'])

class ListAmbulances(generic.ListView):
    template_name = 'ambulance_details/list_ambulances.html'
    context_object_name = 'ambulances'

    def get_queryset(self):
        return  Ambulance.objects.filter(district__name=self.kwargs['district'])