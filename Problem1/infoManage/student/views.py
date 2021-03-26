from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import StudentData
def index (request):
    studentList=StudentData.objects.all()
    context={'studentList':studentList}
    return render(request,'student/index.html',context)
    # return HttpResponse("Hello, world!")

def deleteData(request,roll):
    # ent=StudentData.objects.get(roll=roll)
    StudentData.objects.filter(roll=roll).delete()
    # StudentData.save()
    return redirect('/')

def editData(request,roll):
    try:
        ent = StudentData.objects.get(roll=roll)
    except:
        return HttpResponse("Roll Number not valid")

    context={
        'name':ent.name,
        'roll':ent.roll,
        'hostel':ent.hostel,
        'department': ent.department
    }
    return render(request,'student/edit.html', context)

def addData(request):
    context={'ErrorMessage':''}
    return render(request,'student/add.html',context)
    # return index(request)


def saveData(request):
    sname=request.POST['name']
    sroll=request.POST['roll']
    sdept=request.POST['department']
    shostel=request.POST['hostel']
    a=StudentData(name=sname,roll=sroll,department=sdept,hostel=shostel)
    try:
        if sname=='' or sroll=='' or sdept=='' or shostel=='' :
            context = {'ErrorMessage': 'Data not valid'}
            return render(request, 'student/add.html', context)
        a.save()
        return redirect('/')
    except:
        context = {'ErrorMessage': 'Data not valid'}
        return render(request, 'student/add.html', context)


def editField(request,roll):
    try:
        ent=StudentData.objects.get(roll=roll)
    except:
        return HttpResponse("Roll Number not valid")
    ent.name=request.POST['name']
    ent.department=request.POST['department']
    ent.hostel=request.POST['hostel']
    ent.save()
    return redirect('/')