from django.shortcuts import render

from delivery_tracker.models import *


# Create your views here.
def customer_detail(request, pk):

    customer_obj = Customer.objects.get(pk=pk)

    package_objs = Package.objects.filter(customer_id=customer_obj.id)

    context = {

        "packages": package_objs,

        "customers": customer_obj,

    }

    return render(request, "customer_detail.html", context)