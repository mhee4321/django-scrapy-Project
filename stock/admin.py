from django.contrib import admin
from stock.models import Stock

class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'url')
    list_filter = ('saved_time',)

admin.site.register(Stock, StockAdmin)