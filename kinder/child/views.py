from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .forms import ChilForm
from .models import child  
from .models import payment

from .forms import ChilForm
from .forms import SearchC

from .emp_forms import EmployeeForm
from .emp_forms import SearchEmp
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
            #child information
            child_fname= form.cleaned_data['Child_First_Name']
            child_lname= form.cleaned_data['Child_Last_Name']
            child_dob_Date = form.cleaned_data['Child_DoB']
            child_aler= form.cleaned_data['Child_allergies']
            #parent information
            child_parent_fname = form.cleaned_data['Parent_First_Name']
            child_parent_lname = form.cleaned_data['Parent_Last_Name']
            child_parent_phone = form.cleaned_data['Parent_Phone']
            child_parent_address = form.cleaned_data['Parent_Address']

            #concent_box = form.cleaned_data['Concent_Box']   , Concent_Box = concent_box
            chi = child.objects.create(Child_First_Name = child_fname, Child_Last_Name = child_lname, Child_DoB = child_dob_Date, Child_allergies=child_aler,Parent_First_Name = child_parent_fname, Parent_Last_Name = child_parent_lname, Parent_Phone = child_parent_phone, Parent_Address = child_parent_address) 

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
            emp_phone= emp_form.cleaned_data['Employee_Phone_Number']
            emp_salary= emp_form.cleaned_data['Employee_Salary']
            emp_class_num= emp_form.cleaned_data['Employee_Class_Num']

            emp = employee.objects.create(Employee_First_Name = emp_fname,
                                          Employee_Last_Name = emp_lname,
                                          Employee_DBO= emp_dbo,
                                            Employee_Address= emp_add,
                                            Employee_Phone_Number= emp_phone, 
                                             Employee_Salary= emp_salary,
                                             Employee_Class_Num= emp_class_num  )   

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

def processPayment(request):
    # Generate an order
    payment = payment.objects.create(
        #amount=1000,  # enter amount here
    )

    payment.generate_secret()
    payment.save()

    # Payment data
    data = {
        "amount": payment.price,
        "success_url": f"https://website.com/confirm/{payment.transactionID}/{payment.secret}",
        "back_url": f"https://website.com/orders/{payment.transactionID}",
    }
    
    url="https://stage-api.ioka.kz/v2/orders"
    response = request.post(url, headers={
        "API-KEY": TEST_API_KEY,  
        "Content-Type": "application/json"
    }, data = JsonResponse.dumps(data))
    payment.checkout_url = response['payment']["checkout_url"]
    payment.save()
    return HttpResponse.redirect(payment.checkout_url)


