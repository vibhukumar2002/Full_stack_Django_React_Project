from rest_framework import serializers
from .models import department,employee

class departmentserializer(serializers.ModelSerializer):
    class Meta:
        model=department
        fields='__all__'

class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields='__all__'