from statistics import mode
from unicodedata import name
from django.db import models
from numpy import number

class category(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    price= models.DecimalField(max_digits=11,decimal_places=2)
    image = models.ImageField()
    catagory_id = models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class cart(models.Model):
    prod = models.DecimalField(max_digits=11,decimal_places=0)
    no = models.DecimalField(max_digits=11,decimal_places=0)





