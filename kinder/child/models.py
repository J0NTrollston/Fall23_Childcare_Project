##import uuid
from django.db import models


from django.db import models
from django.db.models import Model

# Create your models here.
class child(models.Model):
    ##id = models.UUIDField(primary_key = True,default = uuid.uuid4, editable = False)
    ##child_id = models.AutoField(primary_key = True, editable = False)
    Child_First_Name  = models.CharField(max_length=200,null=False,blank=False)
    Child_Last_Name  = models.CharField(max_length=200,null=False,blank=False)
    #Child_DBO  = models.DateField()
    Child_allergies  = models.CharField(max_length=200,null=False,blank=False)
    Parent_FullName  = models.CharField(max_length=200,null=False,blank=False)
    ##geeks_field = models.CharField(max_length = 200)
##    c_lname  = models.CharField(max_length=30)
##    c_class  = models.CharField(max_length=30)
##    c_addr  = models.CharField(max_length=30)
##    c_school  = models.CharField(max_length=30)
##    c_enmail  = models.CharField(max_length=30)



# Create your models here.
class employee(models.Model):
    ##id = models.UUIDField(primary_key = True,default = uuid.uuid4, editable = False)
    ##child_id = models.AutoField(primary_key = True, editable = False)
    Employee_First_Name  = models.CharField(max_length=200,null=False,blank=False)
    ##geeks_field = models.CharField(max_length = 200)
##    c_lname  = models.CharField(max_length=30)
##    c_class  = models.CharField(max_length=30)
##    c_addr  = models.CharField(max_length=30)
##    c_school  = models.CharField(max_length=30)
##    c_enmail  = models.CharField(max_length=30)
