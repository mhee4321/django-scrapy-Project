from django.shortcuts import render
from django.views.generic import ListView, DetailView
from weather.models import Weather

class WeatherLV(ListView):
    model = Weather
    template_name = "weather/weather_list.html"
    paginate_by = 10

class WeatherDV(DetailView):
    model = Weather

    
