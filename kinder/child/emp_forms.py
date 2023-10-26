from django import forms
##from .models import child 


from .models import employee 

class EmployeeForm(forms.Form):
    Employee_First_Name  = forms.CharField()

    
    


##    c_lname  = forms.CharField(max_length=30)
##    c_class  = forms.CharField(max_length=30)
##    c_addr  = forms.CharField(max_length=30)
##    c_school  = forms.CharField(max_length=30)
##    c_enmail  = forms.CharField(max_length=30)



   