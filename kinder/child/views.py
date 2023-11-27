from django.http import HttpResponse
from django.shortcuts import render

from .forms import ChilForm
from .models import child 

from .forms import ChildAttendance
from .models import child_attendance 

from .forms import EmpAttendance
from .models import staff_attendance 

from .forms import ChilForm
from .forms import SearchC

from .emp_forms import EmployeeForm
from .emp_forms import SearchEmp
from .models import employee 

from django.contrib import messages
from django.shortcuts import render,redirect


# Create your views here.
def home_page(request):
    return render(request,"home.html",{})

# Create your views here.
def home(request):
    return render(request,'home.html')

# Create your views here.
def entity(request):
    return render(request,'entity.html')


# Create your views here.
def concent_form(request):
    return render(request,'concent_form.html')


def register(request):
    title="Child Registration"
    if request.method == 'POST':
        form=ChilForm(request.POST)
        if form.is_valid():
            #child information
            child_fname= form.cleaned_data['Child_First_Name']
            child_lname= form.cleaned_data['Child_Last_Name']
            child_dob_Date = form.cleaned_data['Child_DoB']
            child_aler= form.cleaned_data['Child_allergies']
            #parent information
            child_parent_fname = form.cleaned_data['Parent_First_Name']
            child_parent_lname = form.cleaned_data['Parent_Last_Name']
            child_parent_email = form.cleaned_data['Parent_Email']
            child_parent_phone = form.cleaned_data['Parent_Phone']
            child_parent_address = form.cleaned_data['Parent_Address']

            #concent_box = form.cleaned_data['Concent_Box']   , Concent_Box = concent_box
            chi = child.objects.create(Child_First_Name = child_fname, Child_Last_Name = child_lname, Child_DoB = child_dob_Date, Child_allergies=child_aler,Parent_First_Name = child_parent_fname
                                       , Parent_Last_Name = child_parent_lname, Parent_Phone = child_parent_phone, Parent_Address = child_parent_address, Parent_Email = child_parent_email) 

            chi.save()
            return render(request,'ack.html',{'title':"Child Registered Successfully"}) 
    form=ChilForm()
    context={
    'title':title,
    'form':form,
    }

    return render(request,'register.html',context)

#,Child_DBO=child_dbo_Date

def atendance(request):
    title="Child Attendance"
    if request.method == 'POST':
        form=ChildAttendance(request.POST)
        if form.is_valid():
            #child information
            Sign_In_Da= form.cleaned_data['Sign_In_Date']
            Sign_Out_Da= form.cleaned_data['Sign_Out_Date']
            Sign_In_Ti = form.cleaned_data['Sign_In_Time']
            Sign_Out_Ti = form.cleaned_data['Sign_Out_Time']
            Facility_Nam = form.cleaned_data['Facility_Name']
            child_fname= form.cleaned_data['Child_First_Name']
            child_lname= form.cleaned_data['Child_Last_Name']
            
            chi = child_attendance.objects.create(Sign_In_Date = Sign_In_Da, Sign_Out_Date = Sign_Out_Da, Sign_In_Time = Sign_In_Ti,Sign_Out_Time=Sign_Out_Ti,Facility_Name=Facility_Nam,Child_First_Name=child_fname  ,Child_Last_Name=child_lname) 
            #, Child_allergies=child_aler,Parent_First_Name = child_parent_fname, Parent_Last_Name = child_parent_lname, Parent_Phone = child_parent_phone, Parent_Address = child_parent_address

            chi.save()
            return render(request,'ack.html',{'title':"Child Attendance Successfully"}) 
    form=ChildAttendance()
    context={
    'title':title,
    'form':form,
    }

    return render(request,'atendance.html',context)

def emp_atendance(request):
    title="Employee Attendance"
    if request.method == 'POST':
        form=EmpAttendance(request.POST)
        if form.is_valid():
            #child information
            Sign_In_Da= form.cleaned_data['Sign_In_Date']
            Sign_Out_Da= form.cleaned_data['Sign_Out_Date']
            Sign_In_Ti = form.cleaned_data['Sign_In_Time']
            Sign_Out_Ti = form.cleaned_data['Sign_Out_Time']
            Facility_Nam = form.cleaned_data['Facility_Name']
            emp_fname= form.cleaned_data['Teacher_First_Name']
            emp_lname= form.cleaned_data['Teacher_Last_Name']
                        
            chi = staff_attendance.objects.create(Sign_In_Date = Sign_In_Da, Sign_Out_Date = Sign_Out_Da, Sign_In_Time = Sign_In_Ti,Sign_Out_Time=Sign_Out_Ti,Facility_Name=Facility_Nam,Teacher_First_Name=emp_fname  ,Teacher_Last_Name=emp_lname) 
           
            chi.save()
            return render(request,'ack.html',{'title':"Employee Registered Successfully"}) 
    form=EmpAttendance()
    context={
    'title':title,
    'form':form,
    }

    return render(request,'attendance_emp.html',context)


def reg_employee(request):
    title="Employee Registration"
    if request.method == 'POST':
        emp_form=EmployeeForm(request.POST)
        if emp_form.is_valid():
            emp_fname= emp_form.cleaned_data['Employee_First_Name']
            emp_lname= emp_form.cleaned_data['Employee_Last_Name']
            emp_email = emp_form.cleaned_data['Employee_Email']
            emp_dbo= emp_form.cleaned_data['Employee_DOB']
            emp_add= emp_form.cleaned_data['Employee_Address']
            emp_phone= emp_form.cleaned_data['Employee_Phone_Number']
            emp_class_num= emp_form.cleaned_data['Classroom']
            emp_salary= emp_form.cleaned_data['Hourly_Salary']
            emp_Facility_Name= emp_form.cleaned_data['Facility_Name']
           

            emp = employee.objects.create(Employee_First_Name = emp_fname,
                                          Employee_Last_Name = emp_lname,
                                          Employee_DOB= emp_dbo,
                                            Employee_Address= emp_add,
                                            Employee_Phone_Number= emp_phone,
                                            Classroom= emp_class_num, 
                                             Hourly_Salary= emp_salary,
                                             Facility_Name= emp_Facility_Name,
                                             Employee_Email= emp_email
                                               )   

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

def reports(request):
    title="All Attendance"
    queryset = child_attendance.objects.all()

    context={
        "title":title,
        "queryset":queryset,
    }
    return render (request,'Attendance_reports.html',context )


def balance_report(request):
    title="Total Registered Children"
    queryset = child.objects.all()

    context={
        "title":title,
        "queryset":queryset,
    }
    return render (request,'balance_reports.html',context )


def emp_report(request):
    title="Total Registered Employee"
    queryset = staff_attendance.objects.all()

    context={
        "title":title,
        "queryset":queryset,
    }
    return render (request,'emp_report.html',context )

def updateData(request,id):
    if request.method=="POST":
        name=request.POST['Child_First_Name']
        lname=request.POST['Child_Last_Name']
        caler=request.POST['Child_allergies']
        pfirstname=request.POST['Parent_First_Name']
        plastname=request.POST['Parent_Last_Name']
        pemail=request.POST['Parent_Email']
        pphone=request.POST['Parent_Phone']
        paddress=request.POST['Parent_Address']
        balance_child=request.POST['Balance']

        #Balance

        edit=child.objects.get(id=id)
        edit.Child_First_Name=name
        edit.Child_Last_Name=lname
        edit.Child_allergies=caler
        edit.Parent_First_Name=pfirstname
        edit.Parent_Last_Name=plastname
        edit.Parent_Email=pemail
        edit.Parent_Phone=pphone
        edit.Parent_Address=paddress
        edit.Balance=balance_child

        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return render(request,'ack.html',{'title':"Data Updated Successfully"})
        #return redirect("/")

    d=child.objects.get(id=id) 
    context={"d":d}
    return render(request,"edit.html",context)



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
        #return render(request,'atendance.html',context)

    context={
    'title':title,
    'form':form,
    }
    return render(request,'search.html',context)

def showatten(request,id):
    title="Search child"
    form= SearchC(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['Child_First_Name']
        queryset=child_attendance.objects.filter(Child_First_Name=name) 
        if len(queryset)==0:
            return render(request,'ack.html',{'title':'Child Not Found'})
        context={
        'title':title,
        'queryset':queryset,
        }
        return render(request,'attendance_child.html',context)
        #return render(request,'atendance.html',context)

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



def dropout_Emp(request):
    title="Terminate Employee"
    form= SearchEmp(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['Employee_First_Name']
        queryset=employee.objects.filter(Employee_First_Name=name)
        if len(queryset)==0:
            return render(request,'ack.html',{'title':'Employee Not Found'})
        else:
            queryset=employee.objects.filter(Employee_First_Name=name).delete()
        return render(request,'ack.html',{'title':"Employee has been terminate from the child care system"})


    context={
    'title':title,
    'form':form,
    }
    return render(request,'search.html',context)







