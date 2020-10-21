from django.db import models

# Create your models here.

class Customer(models.Model):

    name = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name

class Package(models.Model):

    package_type = models.TextField()
    package_weight= models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.package_type