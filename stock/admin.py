from django.contrib import admin
from .models import *
# Register your models here.
# Register your models here.
@admin.register(Data)
class StockAdmin(admin.ModelAdmin):
	list_display = ('stock', 'pur_price', 'pur_date', 'sell_qty', 'sell_price', 'sell_date','profit')

admin.site.register(File)



