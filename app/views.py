from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for" + user)
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


def listings_page(request):
    listings = Listing.objects.all()
    context = {"listings": listings}
    return render(request, "listing.html", context)
