from django.shortcuts import render
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
