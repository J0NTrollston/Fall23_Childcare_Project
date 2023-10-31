from django.http import HttpResponse
from django.shortcuts import render
from .forms import ChilForm
from .models import child  

from .forms import ChilForm
from .forms import SearchC

from .emp_forms import EmployeeForm
from .models import employee 


# Create your views here.
def home_page(request):
    return render(request,"home.html",{})

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    title="Child Registration"
    if request.method == 'POST':
        form=ChilForm(request.POST)
        if form.is_valid():
            child_fname= form.cleaned_data['Child_First_Name']
            child_lname= form.cleaned_data['Child_Last_Name']
            #child_dbo_Date= form.cleaned_data['Child_DBO']
            child_aler= form.cleaned_data['Child_allergies']
            child_parent_name= form.cleaned_data['Parent_FullName']
            chi = child.objects.create(Child_First_Name = child_fname, Child_Last_Name = child_lname,Child_allergies=child_aler,Parent_FullName=child_parent_name ) 

            chi.save()
            return render(request,'ack.html',{'title':"Child Registered Successfully"}) 
    form=ChilForm()
    context={
    'title':title,
    'form':form,
    }

    return render(request,'register.html',context)

#,Child_DBO=child_dbo_Date



def reg_employee(request):
    title="Employee Registration"
    if request.method == 'POST':
        emp_form=EmployeeForm(request.POST)
        if emp_form.is_valid():
            emp_fname= emp_form.cleaned_data['Employee_First_Name']
            emp_lname= emp_form.cleaned_data['Employee_Last_Name']
            emp_dbo= emp_form.cleaned_data['Employee_DBO']
            emp_add= emp_form.cleaned_data['Employee_Address']

            emp = employee.objects.create(Employee_First_Name = emp_fname,
                                          Employee_Last_Name = emp_lname,
                                          Employee_DBO= emp_dbo,
                                            Employee_Address= emp_add ) 

            emp.save()
            return render(request,'ack.html',{'title':"Employee Registered Successfully"}) 
    emp_form=EmployeeForm()
    context={
    'title':title,
    'emp_form':emp_form,
    }

    return render(request,'reg_employee.html',context)
#{'emp_form':emp_form}

def existing_child(request):
    title="Total Registered Children"
    queryset = child.objects.all()

    context={
        "title":title,
        "queryset":queryset,
    }
    return render (request,'existing_child.html',context )




def search(request):
    title="Search child"
    form= SearchC(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['Child_First_Name']
        queryset=child.objects.filter(Child_First_Name=name)
        if len(queryset)==0:
            return render(request,'ack.html',{'title':'Child Not Found'})
        context={
        'title':title,
        'queryset':queryset,
        }
        return render(request,'existing_child.html',context)


    context={
    'title':title,
    'form':form,
    }
    return render(request,'search.html',context)




def dropout(request):
    title="Drop Out child"
    form= SearchC(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['Child_First_Name']
        queryset=child.objects.filter(Child_First_Name=name)
        if len(queryset)==0:
            return render(request,'ack.html',{'title':'Child Not Found'})
        else:
            queryset=child.objects.filter(Child_First_Name=name).delete()
        return render(request,'ack.html',{'title':"Child has been  dropout from the child care system"})


    context={
    'title':title,
    'form':form,
    }
    return render(request,'search.html',context)







