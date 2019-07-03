from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Province(models.Model):
    no = models.IntegerField()
    
    def __str__(self):
        return "{} - {}".format("Province", self.no)

class District(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='districts')
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)

# class City(models.Model):
#     district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='citys')
#     name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return "{}".format(self.name)

# class Ward(models.Model):
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='wards')
#     name = models.CharField(max_length=100)
#     no = models.IntegerField()

#     def __str__(self):
#         return "{}(Ward no:{})".format(self.name, self.no)

class Ambulance(models.Model):
    user = models.name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ambulances')
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    ward_name = models.CharField(max_length=100)
    ward_no = models.IntegerField()
    name = models.CharField(max_length=100, blank=False)
    owner_name = models.CharField(max_length=100, blank=True)
    owner_email = models.EmailField(blank=True)
    phone_number = PhoneNumberField()
    telephone_number = PhoneNumberField(blank=True)