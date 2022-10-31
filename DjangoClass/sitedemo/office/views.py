from django.shortcuts import render
from office import models
# Create your views here.

def index(request):

    mydict ={
        'test1': 'test1',
        'test2': 'test2',
        'test3': 'test3',
        'test4': [1,2,3,4,5,6,7,8,6],
        
    }
    return render(request, 'office/index.html', context=mydict)

def allmodels(request):

    all_patient = models.Patient.objects.all()
    
    context = {'patient': all_patient}

    return render(request, 'office/datalist.html', context=context)

