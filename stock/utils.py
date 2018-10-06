from django.shortcuts import render
import xlrd
import datetime


def read_from_excel(self,file):
    wb=xlrd.open_workbook(filename=file.path)
    mode=wb.datemode
    excel=[]
    for s in wb.sheets():
        for row in range(1,s.nrows):
            data=[]
            for col in range(s.ncols):
                value=(s.cell(row,col).value)
                data.append(value)
            data.append(mode)
            excel.append(data)
        return excel

 
