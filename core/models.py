from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20,name='name')
    city=models.CharField(max_length=20,name='city')
    state=models.CharField(max_length=20,name='state')
    company=models.CharField(max_length=20,name='company')

    def __str__(self):
        return self.name