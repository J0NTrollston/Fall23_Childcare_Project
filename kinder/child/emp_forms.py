from django import forms
##from .models import child 

#from phonenumber_field.modelfields import PhoneNumberField
#from phone_field import PhoneField


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
    #Employee_Phone= PhoneField(blank=True,help_text='Contact phone number')
    #Employee_Phone= (label='Employee Phone')

    

#label='Employee Date of Birth'    


##    c_lname  = forms.CharField(max_length=30)
##    c_class  = forms.CharField(max_length=30)
##    c_addr  = forms.CharField(max_length=30)
##    c_school  = forms.CharField(max_length=30)
##    c_enmail  = forms.CharField(max_length=30)



   