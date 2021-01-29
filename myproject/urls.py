from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from rest_framework import routers
from news import rest_views

router = routers.DefaultRouter()
router.register(r'users', rest_views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('news/', include('news.urls', namespace='news')),
    path('weather/', include('weather.urls', namespace='weather')),
    path('stock/', include('stock.urls', namespace='stock')),

    path('api/', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('api.urls', namespace='api')),
]
