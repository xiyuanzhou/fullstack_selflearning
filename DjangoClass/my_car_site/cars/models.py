from django.db import models

# Create your models here.
class cars(models.Model):
    #pk
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    

    def __str__(self):

        return f"car brand:{self.brand}; {self.year}"