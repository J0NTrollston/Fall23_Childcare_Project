##import uuid
from django.db import models
from django.db.models import Model

# Create your models here.

class child(models.Model):
    #Child_id = models.UUIDField(primary_key = True, editable = False)
    Child_First_Name  = models.CharField(max_length=200,null=False,blank=False)
    Child_Last_Name  = models.CharField(max_length=200,null=False,blank=False)
    Child_DoB  = models.DateField(max_length=9,null=False,blank=False)
    Child_allergies  = models.CharField(max_length=200,null=False,blank=False)

    Parent_First_Name = models.CharField(max_length=200,null=False,blank=False)
    Parent_Last_Name = models.CharField(max_length=200,null=False,blank=False)
    Parent_Phone = models.CharField(max_length=10,null=False,blank=False)
    Parent_Address = models.CharField(max_length=200,null=False,blank=False)
    Consent_Box = models.CharField(max_length=200,null=False,blank=False)
    
    ##geeks_field = models.CharField(max_length = 200)
##    c_lname  = models.CharField(max_length=30)
##    c_class  = models.CharField(max_length=30)
##    c_addr  = models.CharField(max_length=30)
##    c_school  = models.CharField(max_length=30)
##    c_enmail  = models.CharField(max_length=30)


class parent(models.Model):
    Parent_id = models.UUIDField(primary_key = True, editable = False)
    Parent_First_Name  = models.CharField(max_length=200,null=False,blank=False)
    Parent_Last_Name  = models.CharField(max_length=200,null=False,blank=False)
    Parent_Phone = models.CharField(max_length=200,null=False,blank=False)
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
    #employee_id = models.UUIDField(primary_key = True, editable = False)
    Employee_First_Name = models.CharField(max_length=200,null=False,blank=False)
    Employee_Last_Name  = models.CharField(max_length=200,null=False,blank=False)
    Employee_DOB  = models.DateField(max_length=9,null=False,blank=False)
    Employee_Address = models.CharField(max_length=200,null=False,blank=False)
    Employee_Phone_Number  = models.CharField(max_length=200,null=False,blank=False)
    Classroom = models.CharField(max_length=200)
    Hourly_Salary = models.IntegerField()
    Facility_Name = models.CharField(max_length=200,null=False,blank=False)

class enrollments(models.Model):
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
    Hours_Worked = models.IntegerField()
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

