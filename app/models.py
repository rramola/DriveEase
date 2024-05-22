from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Profile(models.Model):
    account_type = (("Rentor", "Rentor"), ("Rentee", "Rentee"))
    user = models.OneToOneField(
        User,
        null=True,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    groups = models.CharField(max_length=6, choices=account_type, default="")


class Vehicle(models.Model):
    profile = models.ForeignKey(
        Profile, verbose_name="user_profile", on_delete=models.CASCADE, default=""
    )
    vehicle_image = models.ImageField(default="car.png", null=True, blank=True)
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class Listing(models.Model):
    profile = models.ForeignKey(Profile, verbose_name="user", on_delete=models.CASCADE)
    vehicle = models.ForeignKey(
        Vehicle, verbose_name="vehicle", on_delete=models.CASCADE
    )
    price = models.IntegerField(null=True)
