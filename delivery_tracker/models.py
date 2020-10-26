from django.db import models
import datetime

# Create your models here.

class Customer(models.Model):

    firstname = models.TextField()
    lastname = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.firstname + " " +  self.lastname

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
    )

    package_weight= models.IntegerField(default=0.00)

    def __str__(self):
        return str(self.id) + " " + self.package_type

class Service(models.Model):

    service_type = models.TextField(primary_key=True)
    delivery_time = models.CharField(max_length=20)

    def __str__(self):
        return self.service_type


class Route(models.Model):

    route_id = models.TextField(primary_key=True)

    LUZON = 'Luzon'
    VISAYAS = 'Visayas'
    MINDANAO = 'Mindanao'
    AREA_CHOICES = [
        (LUZON, 'Luzon'),
        (VISAYAS, 'Visayas'),
        (MINDANAO, 'Mindanao'),
    ]
    origin_area = models.CharField(
        max_length=8,
        choices=AREA_CHOICES,
    )
    destination_area = models.CharField(
        max_length=8,
        choices=AREA_CHOICES,
    )
    # origin_area = models.CharField(max_length=8, default="uncategorized")
    # destination_area = models.CharField(max_length=8, default="uncategorized")

    def __str__(self):
        return self.origin_area + " to " + self.destination_area


class Weight_Cost_Matrix(models.Model):
    base_weight = models.FloatField(default=0.00)
    base_cost = models.FloatField(default=0.00)
    increment_weight = models.FloatField(default=0.0)
    increment_cost = models.FloatField(default=0.0)
    service = models.ForeignKey(Service, on_delete=models.RESTRICT, null=False)
    route = models.ForeignKey(Route, on_delete=models.RESTRICT, null=False)
    



class Delivery_Staff(models.Model):

    staff_firstname = models.TextField()
    staff_lastname = models.TextField()

    def __str__(self):
        return self.staff_firstname + " " + self.staff_lastname

class Recipient(models.Model):

    firstname = models.TextField()
    lastname = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.firstname + " " +  self.lastname

class Delivery_Request(models.Model):

    control_number = models.AutoField(primary_key=True)
    request_date = models.DateField()
    total_cost = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, null=False)
    service = models.ForeignKey(Service, on_delete=models.RESTRICT, null=False)
    package = models.ForeignKey(Package, on_delete=models.RESTRICT, null=False)
    route = models.ForeignKey(Route, on_delete=models.RESTRICT, null=False)
    weight_cost_matrix = models.ForeignKey(Weight_Cost_Matrix, on_delete=models.RESTRICT, null=False)
    receiver = models.ForeignKey(Recipient, on_delete=models.RESTRICT, null=False)

    def __str__(self):
        return "[" + str(self.request_date) + "]" + " Package " + str(self.package.id) + " by " + self.customer.firstname + " " + self.customer.lastname



class Delivery_Receipt(models.Model):

    control_number = models.AutoField(primary_key=True)
    date_delivered = models.DateField(default=datetime.date.today)
    consignee_signature = models.ImageField()
    delivery_request = models.ForeignKey(Delivery_Request, on_delete=models.RESTRICT, null=False)
    Delivery_Staff = models.ForeignKey(Delivery_Staff, on_delete=models.RESTRICT, null=False)