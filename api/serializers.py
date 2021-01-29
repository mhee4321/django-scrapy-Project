from rest_framework import serializers
from news.models import News
from stock.models import Stock
from weather.models import Weather


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'company', 'saved_time')

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('name', 'code', 'price', 'saved_time', 'url')

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('city', 'date', 'desc', 'temp_min', 'temp_max', 'humidity', 'pressure', 'deg', 'speed')

