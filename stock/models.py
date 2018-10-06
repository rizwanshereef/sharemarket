from django.db import models
from .utils import read_from_excel
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime,xlrd
class File(models.Model):
    file=models.FileField()
@receiver(post_save, sender=File)
def create_data(sender, instance=None, created=False, **kwargs):
    data=read_from_excel(instance,instance.file)
    for item in data:
        #print(item)
        sl_no=item[0]
        stock=item[1]
        pur_price=item[2]
        pur_date=datetime.datetime(*xlrd.xldate_as_tuple(item[3],item[8] ))
        sell_qty=item[4]
        sell_price=item[5]
        sell_date=datetime.datetime(*xlrd.xldate_as_tuple(item[6],item[8] ))
        profit=item[7]
        print('pur_date',pur_date)
        print('sell_date',sell_date)
        Data.objects.create(sl_no=sl_no, stock=stock, pur_price=pur_price, pur_date=pur_date, sell_qty=sell_qty, sell_price=sell_price, sell_date=sell_date, profit=profit)




class Data(models.Model):
    sl_no=models.AutoField(primary_key=True)
    stock=models.CharField(max_length=30)
    pur_price=models.IntegerField()
    pur_date=models.DateField(blank=True,null=True)
    sell_qty=models.IntegerField()
    sell_price=models.IntegerField()
    sell_date=models.DateField(blank=True,null=True)
    profit=models.IntegerField()    
