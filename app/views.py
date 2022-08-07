from django.contrib import messages
from django.shortcuts import render,redirect
from . models import Employee


# Create your views here.
def home(request):
    total_employee = Employee.objects.all().count()
    on_leave = Employee.objects.filter(on_leave=True).count()
    context = {
        'total_employee':total_employee,
        'on_leave':on_leave
    }
    return render(request,'dashboard.html',context)

def create_employee(request):
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        doj = request.POST['doj']
        department= request.POST['department']
        post = request.POST['post']
        address = request.POST['address']

        employee = Employee.objects.create(name=name,
                                    dob=dob,doj=doj,
                                    department=department,
                                    post=post,
                                    address=address)
        messages.success(request,'Employee Added successfully')          
        return redirect('employee_list')                  
    return render(request,'create_employee.html')

def edit_employee(request,id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        doj = request.POST['doj']
        department= request.POST['department']
        post = request.POST['post']
        address = request.POST['address']

        employee = Employee.objects.filter(id=id).update(name=name,
                                    dob=dob,doj=doj,
                                    department=department,
                                    post=post,
                                    address=address)
        messages.success(request,'Employee Updated successfully')          
        return redirect('employee_list')                  
    context = {
        'employee':employee,
    }
    return render(request,'edit_employee.html',context)

def delete_employee(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.success(request,"Employee Deleted successfully")
    return redirect('employee_list')

def employee_list(request):
    employee_list = Employee.objects.all()
    context = {
        'employee_list':employee_list,
    }
    return render(request,'employee_list.html',context)

def leave_status(request,id):
    employee_id = Employee.objects.get(id=id)

    if employee_id.on_leave:
        employee_id.on_leave = False
    else:
        employee_id.leave_count = employee_id.leave_count + 1
        employee_id.on_leave = True

    employee_id.save()
    messages.success(request,"Employee leave status Changed successfully.")
    return redirect('employee_list')
