from django.db import models
import datetime

# Create your models here.

class Customer(models.Model):

    name = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=11)
    # customer_type = models.CharField(max_length=11)

    def __str__(self):
        return self.name




class Package(models.Model):
    LETTER = 'LTR'
    PARCEL = 'PAR'
    PACKAGE = 'PCK'
    BOX = 'BOX'
    PACKAGE_TYPE_CHOICES = [
        (LETTER, 'Letter'),
        (PARCEL, 'Parcel'),
        (PACKAGE, 'Package'),
        (BOX, 'Box'),
    ]
    package_type = models.CharField(
        max_length=3,
        choices=PACKAGE_TYPE_CHOICES,
        default=LETTER,
    )

    # package_type = models.TextField()
    package_weight= models.IntegerField()
    # customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id) + " " + self.package_type

class Service(models.Model):

    service_type = models.TextField(primary_key=True)
    delivery_time = models.CharField(max_length=20)

    def __str__(self):
        return self.service_type

class Weight_Cost_Matrix(models.Model):

    base_weight = models.FloatField()
    base_cost = models.FloatField()
    increment_weight = models.FloatField()
    increment_cost = models.FloatField()
    
    

class Route(models.Model):

    route_id = models.TextField(primary_key=True)
    origin_area = models.CharField(max_length=8, default="uncategorized")
    destination_area = models.CharField(max_length=8, default="uncategorized")

    def __str__(self):
        return self.origin_area + " to " + self.destination_area

class Delivery_Receipt(models.Model):
    
    control_number = models.AutoField(primary_key=True)
    date_delivered = models.DateField(default=datetime.date.today)
    consignee_signature = models.ImageField()

class Delivery_Staff(models.Model):

    staff_name = models.TextField()

    def __str__(self):
        return self.staff_name

class Recipient(models.Model):

    name = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name

class Delivery_Request(models.Model):

    control_number = models.AutoField(primary_key=True)    
    request_date = models.DateField()
    # total_cost = models.DecimalField(max_digits=8, decimal_places=2, null=True)    
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, null=False)
    service = models.ForeignKey(Service, on_delete=models.RESTRICT, null=False)
    package = models.ForeignKey(Package, on_delete=models.RESTRICT, null=False)
    route = models.ForeignKey(Route, on_delete=models.RESTRICT, null=False)
    # weight_cost_matrix = models.ForeignKey(Weight_Cost_Matrix, on_delete=models.RESTRICT, null=False)