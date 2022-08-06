from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('employee-list/', views.employee_list,name='employee_list'),
    # path('employee-list/', views.employee_list,name='employee_list'),
    path('leave-status/<int:id>/', views.leave_status,name='leave_status'),
]
