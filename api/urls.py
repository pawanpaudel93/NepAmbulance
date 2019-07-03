from django.contrib import admin
from django.urls import path
from .views import ListCreateAmbulance, RetrieveUpdateDeleteAmbulance, ListDistrict, ListProvince

urlpatterns = [
    path('ambulance/<int:province>/<slug:district>/<slug:city>/<int:ward>/', ListCreateAmbulance.as_view(), name="list-create-api"),
    path('ambulance/<int:province>/<slug:district>/<slug:city>/<int:ward>/<int:pk>/', RetrieveUpdateDeleteAmbulance.as_view()),
    # path('get/wards/<slug:city>/', ListWard.as_view(), name="get-wards"),
    # path('get/cities/<slug:district>/', ListCity.as_view(), name='get-cities'),
    path('get/districts/<slug:province>/', ListDistrict.as_view(), name='get-districts'),
    path('get/provinces/', ListProvince.as_view(), name='get-provinces'),
]