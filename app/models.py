from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    profile = models.ForeignKey(Profile, verbose_name="user_profile", on_delete=models.CASCADE, default="")
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.make + " " + self.model



class Listing(models.Model):
    profile = models.ForeignKey(Profile, verbose_name="user_profile", on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, verbose_name="vehicle_profile", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.profile.name + " " + self.vehicle.make + " " + self.vehicle.model