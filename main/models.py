from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    mood = models.CharField(max_length=255, blank=True, null=True)  # Mood field added
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Change 1 to the actual User ID

    def __str__(self):
        return self.name


'''
import uuid
class Project(models.Model):
    id = models.UUIDField(primary_key=true,default=uuid. uuid4)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    department = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project, related_name='employees')
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
'''