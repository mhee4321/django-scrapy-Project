"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from news.views import NewsLV, NewsDV, RefreshFormView, SearchFormView

app_name = 'news'

urlpatterns = [
    path('', NewsLV.as_view(), name='index'),
    path('list/', NewsLV.as_view(), name='list'),
    path('<int:pk>', NewsDV.as_view(), name='detail'),
    path('', RefreshFormView.as_view(), name='refresh'),
    path('search/', SearchFormView.as_view(), name='search'),
]
