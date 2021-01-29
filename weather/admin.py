from django.contrib import admin
from weather.models import Weather

class WeatherAdmin(admin.ModelAdmin):
    list_display = ('city', 'date', 'desc', 'temp_min', 'temp_max', 'humidity', 'pressure', 'deg', 'speed')
    list_filter = ('date',)

admin.site.register(Weather, WeatherAdmin)


