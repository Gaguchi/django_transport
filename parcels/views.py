from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.utils import timezone
from .models import Ride



def index(request):
    destination = request.GET.get('destination', 'Poland') # default to 'Poland' if not provided
    rides = Ride.objects.filter(destination=destination).order_by('start_date')
    context = {
        'destination': destination,
        'rides': rides
    }
    return render(request, 'parcels/index.html', context)