from django.contrib import admin

from .models import Customer, Package, Service, Route, Delivery_Staff, Recipient, Weight_Cost_Matrix, Delivery_Receipt, Delivery_Request

# Register your models here.
admin.site.register(Customer)
admin.site.register(Package)
admin.site.register(Service)
admin.site.register(Route)
admin.site.register(Delivery_Staff)
admin.site.register(Recipient)
admin.site.register(Delivery_Receipt)
admin.site.register(Weight_Cost_Matrix)
admin.site.register(Delivery_Request)
