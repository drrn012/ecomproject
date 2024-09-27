from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


'''
class Person(models.Models):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max=100)
    is_happy= models.BooleanField()

    def __str__(self):
        return self.name 
'''

