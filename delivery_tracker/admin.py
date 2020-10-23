from django.contrib import admin

from .models import Customer, Package, Service, Route, Delivery_Staff, Recipient

# Register your models here.
admin.site.register(Customer)
admin.site.register(Package)
admin.site.register(Service)
admin.site.register(Route)
admin.site.register(Delivery_Staff)
admin.site.register(Recipient)
