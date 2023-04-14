from django.contrib import admin
from .models import City, Ride, RideCity, Parcel, UserProfile


class RideCityInline(admin.TabularInline):
    model = RideCity


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'status')
    inlines = [RideCityInline]


@admin.register(RideCity)
class RideCityAdmin(admin.ModelAdmin):
    list_display = ('ride', 'city', 'order')


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'ride', 'pickup_city', 'dropoff_city', 'status')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')
