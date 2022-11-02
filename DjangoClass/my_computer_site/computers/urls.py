from django.urls import path
from computers import views

app_name = 'computers'

urlpatterns = [
    path('cominfo/', views.computer_info, name='info'),
    path('thankyou/', views.thank_you, name='thank_you'),

]
