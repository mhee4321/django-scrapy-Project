from django.contrib import admin
from django.urls import path, include
from weather.views import WeatherLV, WeatherDV

app_name = 'weather'

urlpatterns = [
    path('', WeatherLV.as_view(), name='index'),
    path('list/', WeatherLV.as_view(), name='list'),
    path('<int:pk>/', WeatherDV.as_view(), name='detail'),
]
