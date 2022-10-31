from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    heartrate = models.IntegerField(default=70,validators=[MinValueValidator(60), MaxValueValidator(150)])

    #defult showing the message when acess the objects
    def __str__(self):

        return f"{self.first_name},{self.last_name} is {self.age} years old; heartrate:{self.heartrate}"