from my_app import views
from django.urls import path

urlpatterns =[
    path('example/', views.example_view),

    path('var/', views.variables),
    
]


