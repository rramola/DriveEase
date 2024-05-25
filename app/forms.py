from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django import forms

from .models import *


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)
    group = forms.ModelChoiceField(
        queryset=Group.objects.filter(Q(name="rentor") | Q(name="rentee")),
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "group",
        ]


class AddVehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ["year", "make", "model", "vehicle_image"]


class CreateListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ["vehicle", "price"]

    def __init__(self, *args, **kwargs):
        user_profile = kwargs.pop("user_profile", None)
        listing_id = kwargs.pop("test", None)
        super(CreateListingForm, self).__init__(*args, **kwargs)
        if user_profile:
            unlisted_vehicles = []
            listed_vehicles = []
            user_listings = Listing.objects.filter(profile=user_profile)
            user_vehicles = Vehicle.objects.filter(profile=user_profile)
            for listing in user_listings:
                listed_vehicles.append(listing.vehicle)
            for vehicle in user_vehicles:
                if vehicle not in listed_vehicles:
                    unlisted_vehicles.append(vehicle.pk)
            self.fields["vehicle"].queryset = Vehicle.objects.filter(
                pk__in=unlisted_vehicles
            )
        if listing_id:
            listing = Listing.objects.filter(id=listing_id)
            listed_vehicle = []
            for item in listing:
                listed_vehicle .append(item.vehicle.pk)
            self.fields["vehicle"].queryset = Vehicle.objects.filter(
                pk__in=listed_vehicle
            )