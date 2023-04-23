from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.utils import timezone
from .models import Ride
from django.contrib import messages
from .models import Ride, Parcel
from .forms import ParcelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def index(request):
    destination = request.GET.get('destination', 'Poland') # default to 'Poland' if not provided
    rides = Ride.objects.filter(destination=destination).order_by('start_date')
    context = {
        'destination': destination,
        'rides': rides
    }
    return render(request, 'parcels/index.html', context)


@login_required(login_url='login')
def add_parcel(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            parcel = form.save(commit=False)
            parcel.ride = ride
            parcel.sender = request.user
            parcel.save()
            messages.success(request, 'Your parcel has been added successfully!')
            return redirect('ride_detail', ride_id=ride.id)
    else:
        form = ParcelForm()
    
    if request.user.is_authenticated:
        context = {'form': form, 'ride': ride}
    else:
        messages.error(request, 'You must be logged in to add parcels to the ride. Please log in or register.')
        context = {'login_url': 'login', 'register_url': 'register'}
    
    return render(request, 'parcels/add_parcel.html', context)