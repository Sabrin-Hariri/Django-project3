from django.db import models

# Create your models here.


class Patient(models.Model): 
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    age=models.IntegerField()
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=500)


    def __str__(self):
        return f"{self.fname}-{self.fname}-{self.lname} with age : {self.age} -  the disease: {self.title}-{self.description}"
