from my_app import views
from django.urls import path

app_name = 'my_app'


urlpatterns =[
    path('example/', views.example_view, name='example'),

    path('var/', views.variables, name='variables'),

]


