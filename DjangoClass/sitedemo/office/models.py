from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    #defult showing the message when acess the objects
    def __str__(self):

        return f"{self.first_name},{self.last_name} is {self.age} years old"