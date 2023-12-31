from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import department,employee
from .serializers import departmentserializer,employeeserializer
from django.core.files.storage  import default_storage

# Create your views here.

@csrf_exempt
def departmentlist(request):
    if request.method == 'GET':
        depts=department.objects.all()
        depts_x=departmentserializer(depts,many=True)
        return JsonResponse(depts_x.data,safe=False)
    elif request.method=='POST':
        POST_data=JSONParser().parse(request)
        dept_x=departmentserializer(data=POST_data)
        if dept_x.is_valid():
            dept_x.save()
            return JsonResponse("Added Succesfully",safe=False)
        else:
             return JsonResponse("unable to add to database",safe=False)
        
    elif request.method =='PUT':
        PUT_data=JSONParser().parse(request)
        dept=department.objects.get(departmentid=PUT_data['departmentid'])
        department_x=departmentserializer(instance=dept,data=PUT_data)
        if department_x.is_valid():
             department_x.save()
             return JsonResponse("Updated Succesfully",safe=False)
        else:
             return JsonResponse("unable to Update",safe=False)
        
    # elif request.method== 'DELETE':
    #     dept=department.objects.get(departmentid=id)
    #     dept.delete()
    #     return JsonResponse("deleted succesfully" ,safe=False)
        
@csrf_exempt
def deletedept(request,id):
    if request.method=='DELETE':
        dept=department.objects.get(departmentid=id)
        dept.delete()
        return JsonResponse("Succesfully Deleted",safe=False)

@csrf_exempt
def employeeview(request):
    if request.method== 'GET':
        list=employee.objects.all()
        list_x=employeeserializer(list,many=True)
        return JsonResponse(list_x.data,safe=False)
    
    if request.method=='POST':
        POST_data=JSONParser().parse(request)
        POST_data_x=employeeserializer(data=POST_data)
        if POST_data_x.is_valid():
            POST_data_x.save()
            return JsonResponse("Added Succesfully" ,safe=False)
        else:
            return JsonResponse("Failed to add",safe=False)
        
    
    if request.method=='PUT':
        PUT_data=JSONParser().parse(request)
        reqobj=employee.objects.get(employeeid=PUT_data['employeeid'])
        PUT_data_x=employeeserializer(instance=reqobj,data=PUT_data)
        if PUT_data_x.is_valid():
            PUT_data_x.save()
            return JsonResponse("Updated succesfully",safe=False)
        else:
            return JsonResponse("Failed to update",safe=False)

@csrf_exempt
def deleteemployee(request,id):
    reqobj=employee.objects.get(employeeid=id)
    if (reqobj):
        reqobj.delete()
        return JsonResponse("deleted succesfully",safe=False)
    else:
        return JsonResponse("failed to delete",safe=False)
    
@csrf_exempt
def savefile(request):
    reqdata=request.FILES['uploadedfile']
    reqdata_x=default_storage.save(reqdata.name,reqdata)
    return JsonResponse(reqdata_x,safe=False)

