from django.urls import path, include
from api.views import PostViewSet

app_name = 'api'

news_list = PostViewSet.as_view({ 'get':'list' })
news_detail = PostViewSet.as_view({ 'get':'detial' })

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('news/', news_list, name='news_list'),
    path('news/<int:pk>', news_detail, name='news_detail'),
]