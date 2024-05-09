from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)


class Vehicle(models.Model):
    profile = models.ForeignKey(
        Profile, verbose_name="user_profile", on_delete=models.CASCADE, default=""
    )
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)


class Listing(models.Model):
    profile = models.ForeignKey(Profile, verbose_name="user", on_delete=models.CASCADE)
    vehicle = models.ForeignKey(
        Vehicle, verbose_name="vehicle", on_delete=models.CASCADE
    )
    price = models.IntegerField(null=True)


def create_profile(name, email):
    new_profile= Profile(name=name, email=email)
    new_profile.save()
    return new_profile


def create_vehicle(profile, year, make, model):
    new_vehicle = Vehicle(profile=profile,year=year, make=make, model=model)
    new_vehicle.save()
    return new_vehicle

def create_listing(profile, vehicle):
    new_listing = Listing(profile=profile, vehicle=vehicle)
    new_listing.save()
    return new_listing