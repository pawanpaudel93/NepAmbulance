from django.contrib import admin
from .models import Province, District, Ambulance

# Register your models here.
admin.site.site_header = "NepAmbulance";
admin.site.site_title = "NepAmbulance";
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Ambulance)