from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100,null=True)
    dob = models.DateField(null=True,blank=True)
    doj = models.DateField(null=True,blank=True)
    department = models.CharField(max_length=100,null=True)
    post = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    active = models.BooleanField(default=True)
    leave_count = models.IntegerField(null=True,blank=True,default=0)
    on_leave = models.BooleanField(default=False)


    def __str__(self):
        return self.name

