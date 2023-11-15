from django import forms
##from .models import child 

class DateInput(forms.DateInput):
    input_type = 'date'


from .models import employee 

class EmployeeForm(forms.Form):
    Employee_First_Name  = forms.CharField(label='Employee First Name')
    Employee_Last_Name  = forms.CharField(label='Employee Last Name')
    Employee_DOB  = forms.DateField(label = 'Employee Date of Birth',widget=DateInput)
    Employee_Address= forms.CharField(label='Employee Address')
    Employee_Phone_Number  = forms.CharField(label='Employee Phone Number')
    Classroom = forms.CharField(label='Classroom')
    Hourly_Salary  = forms.IntegerField(label='Employee Salary')
    Facility_Name = forms.CharField(label='Facility Name')


class SearchEmp (forms.Form):
    Employee_First_Name  = forms.CharField()
   