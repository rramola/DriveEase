from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .forms import *
def home(request):
    context ={}
    return render(request, "home.html",context)

def registration_page(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        form = CreateUserForm()

    context = {"form": form}
    return render(request, "registration.html", context)