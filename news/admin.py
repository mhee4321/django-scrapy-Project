from django.contrib import admin
from news.models import News

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'company', 'saved_time')
    list_filter = ('saved_time',)
    search_fields = ('title', 'content', 'company')

admin.site.register(News, NewsAdmin)
