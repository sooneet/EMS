from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('employee-list/', views.employee_list,name='employee_list'),
    # path('employee-list/', views.employee_list,name='employee_list'),
    path('leave-status/<int:id>/', views.leave_status,name='leave_status'),
    path('edit-employee/<int:id>/', views.edit_employee,name='edit_employee'),
    path('delete-employee/<int:id>/', views.delete_employee,name='delete_employee'),
    path('create-employee/', views.create_employee,name='create_employee'),
]   
