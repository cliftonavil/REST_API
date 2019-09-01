from django.db import models
# Signals
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete


class Employee(models.Model):
    name = models.CharField(max_length=20, name='name')
    city = models.CharField(max_length=20, name='city')
    state = models.CharField(max_length=20, name='state')
    company = models.CharField(max_length=20, name='company')

    def __str__(self):
        return self.name


def post_save_employee(sender, instance, **kwargs):
    print("post save employee")


def pre_save_employee(sender, instance, **kwargs):
    print("pre save employee")


def pre_delete_employee(sender, instance, **kwargs):
    print("pre delete employee")


def post_delete_employee(sender, instance, **kwargs):
    print("post delete employee")


pre_save.connect(pre_save_employee, sender=Employee)
post_save.connect(post_save_employee, sender=Employee)
post_delete.connect(post_delete_employee, sender=Employee)
pre_delete.connect(pre_delete_employee, sender=Employee)

