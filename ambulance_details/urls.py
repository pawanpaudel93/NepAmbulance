from django.contrib import admin
from django.urls import path
from .views import ListProvinces, ListDistricts, ListAmbulances, Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('provinces/', ListProvinces.as_view(), name='provinces'),
    path('province-<int:province>/districts/', ListDistricts.as_view() ,name='districts'),
    # path('province-<int:province>/<slug:district>/cities/', ListCities.as_view() ,name='cities'),
    # path('province-<int:province>/<slug:district>/<slug:city>/wards/', ListWards.as_view() ,name='wards'),
    # path('province-<int:province>/<slug:district>/<slug:city>/ward-<int:ward>/ambulances/', ListAmbulances.as_view(
    # ) ,name='ambulances')
    path('province-<int:province>/<slug:district>/ambulances/', ListAmbulances.as_view() ,name='ambulances')
]