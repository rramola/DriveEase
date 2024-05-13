from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class AddVehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ["year", "make", "model"]


class CreateListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ["vehicle", "price"]

    def __init__(self, **kwargs):
        user_profile = kwargs.pop("user_profile", None)
        super(CreateListingForm, self).__init__(**kwargs)
        if user_profile:
            self.fields["vehicle"].queryset = Vehicle.objects.filter(
                profile=user_profile
            )
