from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import NewsSerializer, StockSerializer, WeatherSerializer
from news.models import News
from stock.models import Stock
from weather.models import Weather

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticated]

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [permissions.IsAuthenticated]