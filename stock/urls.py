from django.contrib import admin
from django.urls import path, include
from .views import StockLV, StockDV, SearchFormView

app_name = 'stock'

urlpatterns = [
    path('', StockLV.as_view(), name='index'),
    path('list/', StockLV.as_view(), name='list'),
    path('<int:pk>/', StockDV.as_view(), name='detail'),
    path('search/', SearchFormView.as_view(), name='search'),

]
