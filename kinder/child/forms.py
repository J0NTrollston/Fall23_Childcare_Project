from django import forms
from .models import child 

# Custom widget for a date picker when registering child
class DateInput(forms.DateInput):
    input_type = 'date'

class ChilForm(forms.Form):
    Child_First_Name  = forms.CharField(label='Child First Name')
    Child_Last_Name  = forms.CharField(label='Child Last Name')
    Child_allergies  = forms.CharField(label='Child Allergies')
    Child_DoB = forms.DateField(label = 'Child Date of Birth',widget=DateInput)

    Parent_First_Name  = forms.CharField(label='Parent First Name')
    Parent_Last_Name  = forms.CharField(label='Parent Last Name')
    Parent_Phone = forms.CharField(label='Parent Phone Number')
    Parent_Address = forms.CharField(label='Parent Address')

    #Consent_Box = forms.CharField(label='Please type in your initials to confirm you have read the concent form and agree to it\'s conditions')


##    c_lname  = forms.CharField(max_length=30)
##    c_class  = forms.CharField(max_length=30)
##    c_addr  = forms.CharField(max_length=30)
##    c_school  = forms.CharField(max_length=30)
##    c_enmail  = forms.CharField(max_length=30)
##    Child_DBO = forms.DateField()


class SearchC (forms.Form):
    Child_First_Name  = forms.CharField()



   