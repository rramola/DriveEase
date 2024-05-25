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
from .decorators import authorized_user


@login_required(login_url="login")
def home_page(request):
    user_profile = request.user.profile
    user_type = request.user.groups.all()[0].name
    rentals = Listing.objects.filter(rentee_profile=user_profile)
    rentals_found = True
    if len(rentals) < 1:
        rentals_found = False
    context = {
        "user_type": user_type,
        "rentals": rentals,
        "rentals_found": rentals_found,
    }
    return render(request, "home.html", context)


def registration_page(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            fname = form.cleaned_data.get("first_name")
            email = form.cleaned_data.get("email")
            user.groups.add(form.cleaned_data["group"])
            Profile.objects.create(user=user, name=fname, email=email)
            messages.success(request, "Account was created for" + " " + username)
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


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def listings_page(request):
    user_profile = request.user.profile
    user_type = request.user.groups.all()[0].name
    listings = Listing.objects.filter(is_rented=False)
    listings_found = True
    if len(listings) < 1:
        listings_found = False
    context = {
        "listings": listings,
        "user_type": user_type,
        "listings_found": listings_found,
        "user_profile": user_profile,
    }
    return render(request, "listing.html", context)


@login_required(login_url="login")
@authorized_user(allowed_roles=["rentor", "admin"])
def garage_page(request):
    user = request.user.groups.all()[0]
    user_profile = request.user.profile
    vehicles = Vehicle.objects.filter(profile__name=request.user.first_name)
    listings = Listing.objects.filter(profile=user_profile)
    rented_listings = Listing.objects.filter(is_rented=True)
    rented_vehicles = []
    for listing in rented_listings:
        rented_vehicles.append(listing.vehicle)
    context = {"vehicles": vehicles, "user": user, "listings": listings, "rented_vehicles": rented_vehicles}
    return render(request, "garage.html", context)


@login_required(login_url="login")
@authorized_user(allowed_roles=["rentor", "admin"])
def add_vehicle_page(request):
    form = AddVehicleForm()
    profile = request.user.profile
    if request.method == "POST":
        form = AddVehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.profile = profile
            vehicle.save()
            return redirect("garage")
    context = {"form": form}
    return render(request, "add_vehicle.html", context)


@login_required(login_url="login")
@authorized_user(allowed_roles=["rentor", "admin"])
def update_vehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    form = AddVehicleForm(instance=vehicle)
    if request.method == "POST":
        form = AddVehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect("garage")
    context = {"form": form}
    return render(request, "add_vehicle.html", context)


@login_required(login_url="login")
@authorized_user(allowed_roles=["rentor", "admin"])
def delete_vehicle_page(request, pk):
    vehicle = Vehicle.objects.get(id=pk)

    context = {"vehicle": vehicle}
    if request.method == "POST":
        vehicle.delete()
        return redirect("garage")

    return render(request, "delete_vehicle.html", context)


@login_required(login_url="login")
@authorized_user(allowed_roles=["rentor", "admin"])
def new_listing_page(request):
    form = CreateListingForm(user_profile=request.user.profile)
    if request.method == "POST":
        form = CreateListingForm(request.POST, user_profile=request.user.profile)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.profile = request.user.profile
            listing.save()
            return redirect("garage")
    context = {"form": form}
    return render(request, "new_listing.html", context)


@login_required(login_url="login")
@authorized_user(allowed_roles=["rentor", "admin"])
def update_listing(request, pk):
    listing = Listing.objects.get(id=pk)
    form = CreateListingForm(test=pk)
    context = {"form": form}
    if request.method == "POST":
        form = CreateListingForm(request.POST, instance=listing)
        if form.is_valid():
            listing.save()
            return redirect("garage")
    return render(request, "new_listing.html", context)


@login_required(login_url="login")
@authorized_user(allowed_roles=["rentor", "admin"])
def delete_listing(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {"listing": listing}
    if request.method == "POST":
        listing.delete()
        return redirect("garage")
    return render(request, "delete_listing.html", context)

@login_required(login_url="login")
def rent_vehicle_page(request, pk):
    listing = Listing.objects.get(id=pk)
    profile = request.user.profile
    context = {"listing": listing}
    if request.method == "POST":
        listing.rentee_profile = profile
        listing.is_rented = True
        listing.save()
        return redirect("home")
    return render(request, "rent_vehicle.html", context)

@login_required(login_url="login")
def return_vehicle_page(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {"listing": listing}
    if request.method == "POST":
        listing.rentee_profile = None
        listing.is_rented = False
        listing.save()
        return redirect("home")
    return render(request, "return_vehicle.html", context)


def custom_404_view(request, exception):
    return render(request, 'error.html', status=404)
