from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)


class Vehicle(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()

class Listing(models.Model):
    vehicle = models.ForeignKey(Vehicle, verbose_name="vehicle_listing", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="user_listing", on_delete=models.CASCADE)
    
