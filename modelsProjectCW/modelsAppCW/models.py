from django.db import models

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    color = models.CharField(max_length=10)
    gender = models.CharField(max_length=7)

class Account(models.Model):
    username = models.CharField(max_length=20)
    realName = models.CharField(max_length=30)
    accountNumber = models.IntegerField()
    balance = models.DecimalField(decimal_places=2, max_digits=6)