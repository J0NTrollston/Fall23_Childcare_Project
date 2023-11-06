from django import forms
from .models import child 

class ChilForm(forms.Form):
    Child_First_Name  = forms.CharField(label='Child First Name')
    Child_Last_Name  = forms.CharField(label='Child Last Name')
    Child_allergies  = forms.CharField(label='Child Allergies')
    Child_DBO = forms.DateField()
    Parent_FullName  = forms.CharField(label='Parent Full Name')

##    c_lname  = forms.CharField(max_length=30)
##    c_class  = forms.CharField(max_length=30)
##    c_addr  = forms.CharField(max_length=30)
##    c_school  = forms.CharField(max_length=30)
##    c_enmail  = forms.CharField(max_length=30)
##    Child_DBO  = forms.DateField()


class SearchC (forms.Form):
    Child_First_Name  = forms.CharField()


   