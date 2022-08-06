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
