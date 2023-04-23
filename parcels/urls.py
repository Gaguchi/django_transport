from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rides/<int:ride_id>/add_parcel/', views.add_parcel, name='add_parcel'),
]
