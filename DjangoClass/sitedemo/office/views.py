from django.shortcuts import render

# Create your views here.

def index(request):
    mydict ={
        'test1': 'test1',
        'test2': 'test2',
        'test3': 'test3',
        'test4': [1,2,3,4,5,6,7,8,6],
        
    }
    return render(request, 'office/index.html', context=mydict)

