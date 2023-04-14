from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ride(models.Model):
    DESTINATIONS = [
        ('Poland', 'Poland'),
        ('Georgia', 'Georgia'),
    ]

    name = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=100, default='', blank=True)
    destination = models.CharField(max_length=16, choices=DESTINATIONS, default='PL')
    cities = models.ManyToManyField(City, through='RideCity')

    def __str__(self):
        return self.name


class RideCity(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.ride.name} - {self.city.name}"


class Parcel(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    recipient = models.CharField(max_length=100)
    ride = models.ForeignKey(Ride, related_name='ride_parcel', on_delete=models.CASCADE, default=None)
    pickup_city = models.ForeignKey(City, related_name='pickup_parcel', on_delete=models.CASCADE, default=None)
    dropoff_city = models.ForeignKey(City, related_name='dropoff_parcel', on_delete=models.CASCADE, default=None)
    status = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return f"{self.sender.username}'s parcel"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
