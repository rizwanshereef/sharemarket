from django import forms
from stock.models import Data

# class NewUserForm(forms.ModelForm):
#     class Meta():
#         model = Data
#         fields = '__all__'


class StockForm(forms.Form):
    from_date = forms.DateField()
    to_date = forms.DateField()

