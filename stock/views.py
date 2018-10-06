from django.shortcuts import render
from .models import Data
import xlrd
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import generic
from .forms import StockForm
from django.db.models import Q


def read_from_excel(self,file):
    wb=open_workbook(filename=file.path)
    excel=[]
    for s in wb.sheets():
        for row in range(s.nrows):
            data=[]
            for col in range(s.ncols):
                value=(s.cell(row,col).value)
                data.append(value)
            excel.append(data)
        return excel

def users(request):

    form = StockForm()

    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']
            stocks=Data.objects.filter(Q(pur_date__range=(from_date,to_date))|
                                       Q(sell_date__range=(from_date,to_date)))
            # stocks=Data.objects.filter(pur_date__range=(from_date,to_date))
            return render(request,'stock/index.html',{'form':form, 'stocks':stocks})
        else:
            print('ERROR FORM INVALID')

    return render(request,'stock/index.html',{'form':form})

