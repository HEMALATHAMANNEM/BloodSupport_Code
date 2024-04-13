#from statistics import mode
from django.db import models

class Donor(models.Model):
    firstname=models.CharField(max_length=25,null=True)
    lastname=models.CharField(max_length=25,null=True)
    email=models.EmailField(max_length=60,null=True,unique=True)
    phone = models.IntegerField(null=True, unique=True)
    bloodgroup=models.CharField(max_length=5,null=True)
    address=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=50,null=True,unique=True)
    password=models.CharField(max_length=12,null=True)

    def __str__(self) :
        return self.firstname+" "+self.lastname
    

