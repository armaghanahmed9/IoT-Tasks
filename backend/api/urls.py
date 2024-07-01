from django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.get_device_list, name='get_device_list'),
]