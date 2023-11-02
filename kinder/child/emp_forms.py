from django import forms
##from .models import child 




from .models import employee 

class EmployeeForm(forms.Form):
    Employee_First_Name  = forms.CharField(label='Employee First Name')
    Employee_Last_Name  = forms.CharField(label='Employee Last Name')
    Employee_DBO  = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type':"date"
            }

        ),label='Employee Date of Birth' 
    )
    Employee_Address= forms.CharField(label='Employee Address')
    Employee_Phone_Number  = forms.CharField(label='Employee Phone Number')
    Employee_Salary  = forms.DecimalField(label='Employee Salary')
    Employee_Class_Num= forms.CharField(label='Employee Class Number')


class SearchEmp (forms.Form):
    Employee_First_Name  = forms.CharField()


    

  






   