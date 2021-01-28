from rest_framework import serializers
from news.models import News

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'company', 'saved_time')

