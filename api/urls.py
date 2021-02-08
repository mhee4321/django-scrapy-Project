from django.urls import path, include
from api.views import NewsViewSet, StockViewSet, WeatherViewSet 

app_name = 'api'

news_list = NewsViewSet.as_view({ 'get' : 'list' })
news_detail = NewsViewSet.as_view({ 'get' : 'detail' })

stock_list = StockViewSet.as_view({ 'get' : 'list' })
stock_detail = StockViewSet.as_view({ 'get' : 'detail'})

weather_list = WeatherViewSet.as_view({ 'get' : 'list' })
weather_detail = WeatherViewSet.as_view({ 'get' : 'detail' })

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('news/', news_list, name='news_list'),
    path('news/<int:pk>', news_detail, name='news_detail'),
    path('stock/', stock_list, name='stock_list'),
    path('stock/<int:pk>', stock_detail, name='stock_detail'),
    path('weather/', weather_list, name='weather_list'),
    path('weather/<int:pk>', weather_detail, name='weather_detail'),
]