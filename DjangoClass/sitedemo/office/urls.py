
from django.urls import path

from office import views

app_name = 'office'

urlpatterns=[
    path('home/', views.index, name='firstindex'),
    

]