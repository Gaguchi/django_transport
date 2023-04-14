from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from parcels.models import *
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    my_parcels = []
    parcels = Parcel.objects.all()
    for parcel in parcels:
        if parcel.assigned_to == request.user:
            my_parcels.append(parcel)
    return render(request, "users/user.html",{
        'my_parcels': my_parcels,
        'all_parcels':parcels,
    })
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "users/user.html")
        else:
            return render(request, "users/login.html",{
                "message":"Invalid credentials"
            })

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html",{
        "message":"You have been logged out."
    })