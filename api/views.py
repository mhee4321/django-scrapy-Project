from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import PostSerializer
from news.models import News

class PostViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]