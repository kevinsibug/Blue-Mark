from django.db import models

# Create your models here.

class Customer(models.Model):

    name = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=11)

class Package(models.Model):

    Package_type = models.TextField()
    Package_weight= models.IntegerField()