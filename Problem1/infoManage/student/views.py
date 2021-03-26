from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentData
def index (request):
    studentList=StudentData.objects.all()
    context={'studentList':studentList}
    return render(request,'student/index.html',context)
    # return HttpResponse("Hello, world!")

def deleteData(request,roll):
    ...
    return index(request)

def editData(request,roll):
    ...
    return index(request)

def addData(request):
    return index(request)
