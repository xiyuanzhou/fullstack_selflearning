from django.shortcuts import render,redirect
from django.urls import reverse
from cars import models

from django.db.models import Q
# Create your views here.


def list(request):
    all_car = models.cars.objects.all()

    context = {'all_car': all_car}

    return render(request, "cars/list.html",context=context)

def add(request):
    #print(request.POST)
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])

        models.cars.objects.create(brand=brand,year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request, "cars/add.html")



def delete(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])

        if models.cars.objects.filter(Q(brand=brand) & Q(year=year)).all():
            temp1 = models.cars.objects.filter(Q(brand=brand) & Q(year=year)).all()[0]
            #print(temp1)
            temp1.delete()
            return redirect(reverse('cars:list'))
    else:
        return render(request, "cars/delete.html")
