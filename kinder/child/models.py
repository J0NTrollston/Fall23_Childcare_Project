import random
from django.http import HttpResponse
from django.db import models
from django.db.models import Model

from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

from creditcards import types

assert types.get_type('4444333322221111') == types.CC_TYPE_VISA
assert types.get_type('343434343434343') == types.CC_TYPE_AMEX
assert types.get_type('0000000000000000') == types.CC_TYPE_GENERIC

# Create your models here.
class child(models.Model):
    Child_First_Name  = models.CharField(max_length=200,null=False,blank=False)
    Child_Last_Name  = models.CharField(max_length=200,null=False,blank=False)
    Child_DOB  = models.DateField(max_length=9,null=False,blank=False)
    Child_allergies  = models.CharField(max_length=200,null=False,blank=False)
    Parent_First_Name = models.CharField(max_length=200,null=False,blank=False)
    Parent_Last_Name = models.CharField(max_length=200,null=False,blank=False)
    Parent_Email = models.CharField(max_length=200,null=False,blank=False)
    Password  = models.CharField(max_length=200)
    Parent_Phone = models.CharField(max_length=10,null=False,blank=False)
    Parent_Address = models.CharField(max_length=200,null=False,blank=False)
    Balance = models.IntegerField(null=True,blank=True)
    Consent_Box = models.CharField(max_length=200,null=False,blank=False)

class parent(models.Model):
    Parent_First_Name  = models.CharField(max_length=200,null=False,blank=False)
    Parent_Last_Name  = models.CharField(max_length=200,null=False,blank=False)
    Parent_Phone = models.CharField(max_length=200,null=False,blank=False)
    Parent_Email =  models.CharField(max_length=200,null=False,blank=False)
    Child_First_Name  = models.CharField(max_length=200,null=False,blank=False)
    Child_Last_Name  = models.CharField(max_length=200,null=False,blank=False)
    Child_DOB  = models.DateField()
    Child_Allergies  = models.CharField(max_length=200,null=False,blank=False)
    Child_Address = models.CharField(max_length=200,null=False,blank=False)
    Sign_In_Date = models.DateField()
    Sign_Out_Date = models.DateField()
    Sign_In_Time = models.TimeField()
    Sign_Out_Time = models.TimeField()
    Facility_Name = models.CharField(max_length=200,null=False,blank=False)

class employee(models.Model):
    Employee_First_Name = models.CharField(max_length=200,null=False,blank=False)
    Employee_Last_Name  = models.CharField(max_length=200,null=False,blank=False)
    Employee_Email = models.CharField(max_length=200,null=False,blank=False)
    Password  = models.CharField(max_length=200)
    Employee_DOB  = models.DateField(max_length=9,null=False,blank=False)
    Employee_Address = models.CharField(max_length=200,null=False,blank=False)
    Employee_Phone_Number  = models.CharField(max_length=200,null=False,blank=False)
    Classroom = models.CharField(max_length=200)
    Hourly_Salary = models.IntegerField()
    Facility_Name = models.CharField(max_length=200,null=False,blank=False)

class enrollments(models.Model):
    startDate = models.DateField()
    Child_First_Name  = models.CharField(max_length=200,null=False,blank=False)
    Child_Last_Name  = models.CharField(max_length=200,null=False,blank=False)
    Classroom = models.CharField (max_length=200)   
    Tuition_Fee = models.IntegerField ()
    Teacher_First_Name = models.CharField(max_length=200,null=False,blank=False)
    Teacher_Last_Name = models.CharField(max_length=200,null=False,blank=False)
    Facility_Name = models.CharField(max_length=200,null=False,blank=False)

class child_attendance(models.Model):
    Sign_In_Date = models.DateField(max_length=9,null=False,blank=False)
    Sign_Out_Date = models.DateField(max_length=9,null=False,blank=False)
    Sign_In_Time = models.TimeField(max_length=30,null=False,blank=False)
    Sign_Out_Time = models.TimeField(max_length=30,null=False,blank=False)
    Facility_Name = models.CharField(max_length=200,null=False,blank=False)
    Child_First_Name  = models.CharField(max_length=200,null=False,blank=False)
    Child_Last_Name  = models.CharField(max_length=200,null=False,blank=False)

class staff_attendance(models.Model):
    Sign_In_Date = models.DateField(max_length=9,null=False,blank=False)
    Sign_Out_Date = models.DateField(max_length=9,null=False,blank=False)
    Sign_In_Time = models.TimeField(max_length=30,null=False,blank=False)
    Sign_Out_Time = models.TimeField(max_length=30,null=False,blank=False)
    Facility_Name = models.CharField(max_length=200,null=False,blank=False)
    Teacher_First_Name  = models.CharField(max_length=200,null=False,blank=False)
    Teacher_Last_Name  = models.CharField(max_length=200,null=False,blank=False)
    Hours_Worked = models.IntegerField(null=True)
    Salary_Earned = models.IntegerField()

class facility(models.Model):
    Facility_Name = models.CharField(max_length=200,null=False,blank=False)
    Facility_Address = models.CharField(max_length=200,null=False,blank=False)
    Facility_Phone = models.IntegerField()
    License_Number = models.IntegerField()
    Admin_Name = models.CharField(max_length=200,null=False,blank=False)
    Admin_Email = models.CharField(max_length=200,null=False,blank=False)
    Admin_Phone = models.IntegerField()


class admin_user(models.Model):
    Admin_Name = models.CharField(max_length=200,null=False,blank=False)
    Admin_Email = models.CharField(max_length=200,null=False,blank=False)
    Admin_Phone = models.IntegerField()
    Facility_Name = models.CharField(max_length=200,null=False,blank=False)
    Facility_Address = models.CharField(max_length=200,null=False,blank=False)
    Facility_Phone = models.IntegerField()


class payment(models.Model):
    transactionID = models.AutoField(max_length=10, null=False,blank=False)
    price = models.IntegerField()
    cardNum = models.IntegerField()
    cvvNum = models.IntegerField()
    expMonth = models.IntegerField()
    expYear = models.IntegerField()
    Classroom = models.CharField (max_length=200)
    secret = models.CharField(max_length=1000, default="", blank=True)
    paid = models.BooleanField(default=False)
    checkout_url = models.CharField(max_length=1000, default="", blank=True)

    def Price(Classroom):
        if Classroom == 'Infant':
            price = 300

        elif Classroom == 'Toddler':
            price = 275

        elif Classroom == 'Twadler' :
            price = 250

        elif Classroom == '3 Years Old':
            price = 225

        elif Classroom == '4 Years Old':
            price = 200

        else:
            print('Not a valid classroom')

        return price
    
    def generate_secret(self):
        self.secret = str(random.randint(10000, 99999))
    
    def confirm(request, transactionID: int, payment_secret: str):
        payment = payment.objects.get(pk=transactionID)
        if payment.secret == payment_secret:
            payment.paid = True
            payment.save()
        return HttpResponse("OK")  
