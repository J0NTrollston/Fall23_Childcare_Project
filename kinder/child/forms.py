from django import forms
from .models import child 

from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

from creditcards import types

assert types.get_type('4444333322221111') == types.CC_TYPE_VISA
assert types.get_type('343434343434343') == types.CC_TYPE_AMEX
assert types.get_type('0000000000000000') == types.CC_TYPE_GENERIC

# Custom widget for a date picker when registering child
class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

#class MyForm(forms.Form):
 #   my_checkbox = forms.BooleanField(label='My Checkbox', required=False, widget=forms.CheckboxInput(attrs={'class': 'checkbox-class'}))


class ChilForm(forms.Form):
    Child_First_Name  = forms.CharField(label='Child First Name')
    Child_Last_Name  = forms.CharField(label='Child Last Name')
    Child_allergies  = forms.CharField(label='Child Allergies')
    Child_DOB = forms.DateField(label = 'Child Date of Birth',widget=DateInput)
    Parent_First_Name  = forms.CharField(label='Parent First Name')
    Parent_Last_Name  = forms.CharField(label='Parent Last Name')
    Parent_Email = forms.CharField(label='Parent Email')
    Password  = forms.CharField(label='Password')
    Parent_Phone = forms.CharField(label='Parent Phone Number')
    Parent_Address = forms.CharField(label='Parent Address')
    my_checkbox = forms.BooleanField(label='My Checkbox', required=False, widget=forms.CheckboxInput(attrs={'class': 'checkbox-class'}))

class SearchC (forms.Form):
    Child_First_Name  = forms.CharField()


class ChildAttendance (forms.Form):
    Sign_In_Date = forms.DateField(label = 'Sign In Date',widget=DateInput)
    Sign_Out_Date = forms.DateField(label = 'Sign Out Date',widget=DateInput)
    Sign_In_Time = forms.TimeField(label = 'Sign In Time',widget=TimeInput)
    Sign_Out_Time = forms.TimeField(label = 'Sign Out Time',widget=TimeInput)
    Facility_Name = forms.CharField(label='Facility Name')
    Child_First_Name  = forms.CharField(label='Child First Name')
    Child_Last_Name  = forms.CharField(label='Child Last Name')

class EmpAttendance (forms.Form):
    Sign_In_Date = forms.DateField(label = 'Sign In Date',widget=DateInput)
    Sign_Out_Date = forms.DateField(label = 'Sign Out Date',widget=DateInput)
    Sign_In_Time = forms.TimeField(label = 'Sign In Time',widget=TimeInput)
    Sign_Out_Time = forms.TimeField(label = 'Sign Out Time',widget=TimeInput)
    Facility_Name = forms.CharField(label='Facility Name')
    Teacher_First_Name  = forms.CharField(label='Teacher First Name')
    Teacher_Last_Name  = forms.CharField(label='Teacher Last Name')
    #Hours_Worked = forms.IntegerField(label='Hours Worked')
    #Salary_Earned = forms.IntegerField(label='Salary Earned')
    
class LoginForm(forms.Form):
    UserName  = forms.CharField(label='Email Address')
    Password  = forms.CharField(label='Password')

class SearchC (forms.Form):
    Child_First_Name  = forms.CharField()
    Child_Last_Name = forms.CharField()

class paymentForm(forms.Form):
    transactionID = forms.AutoField(max_length=10, null=False,blank=False)
    price = forms.IntegerField()
    cardNum = forms.IntegerField()
    cvvNum = forms.IntegerField()
    expMonth = forms.IntegerField()
    expYear = forms.IntegerField()

class PaymentForm(forms.Form):
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')
   