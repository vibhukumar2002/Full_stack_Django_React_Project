from django.db import models

# Create your models here.

class department(models.Model):
    departmentid=models.AutoField(primary_key=True)
    departmentname=models.CharField(max_length=100)
    

class employee(models.Model):
    employeeid=models.AutoField(primary_key=True)
    employeename=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    dateofjoining=models.DateField()
    photo=models.CharField(max_length=150)
