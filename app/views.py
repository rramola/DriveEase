from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
# Create your views here.
from .forms import *
from .models import *


def home_page(request):
    context = {}
    return render(request, "home.html", context)


def registration_page(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            group = Group.objects.get(name='regular')
            user.groups.add(group)
            Profile.objects.create(
                user=user
            )
            messages.success(request, "Account was created for" + username)
            return redirect("login")
    else:
        form = CreateUserForm()

    context = {"form": form}
    return render(request, "registration.html", context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or password is incorrect")
            return render(request, "login.html")

    context = {}
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")

def listings_page(request):
    listings = Listing.objects.all()
    context = {"listings": listings}
    return render(request, "listing.html", context)

@login_required(login_url="login")
def garage_page(request):
    context = {}
    return render(request, "garage.html", context)


@login_required(login_url="login")
def add_vehicle_page(request):
    form = AddVehicleForm()
    profile = request.user.profile
    if request.method == "POST":
        form = AddVehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.profile = profile
            vehicle.save()
            return redirect('home')
    context = {"form": form
    }
    return render(request, "add_vehicle.html", context)


@login_required(login_url="login")
def new_listing_page(request):
    form = CreateListingForm(user_profile=request.user.profile)
    if request.method == "POST":
        form = CreateListingForm(request.POST, user_profile=request.user.profile)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.profile = request.user.profile
            listing.save()
            return redirect('home')
    context = {"form":form}
    return render(request, "new_listing.html", context)
