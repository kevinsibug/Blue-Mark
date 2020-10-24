from django.shortcuts import render

from delivery_tracker.models import *

# Create your views here.

def home(request):
    return render(request, "home.html")

def add_customer(request):
    return render(request, "add_customer.html")

def customer_confirmation(request, *args, **kwargs):
    return render(request,'customerconfirmation.html', {
        'firstname': request.POST.get('firstname')
    })

def view_customers(request):
    return render(request, "view_customers.html")

def customer_detail(request, pk):

    customer_obj = Customer.objects.get(pk=pk)

    # package_objs = Package.objects.filter(customer_id=customer_obj.id)

    # Trial

    request_objs = Delivery_Request.objects.filter(customer_id=customer_obj.id)

    context = {

        # "packages": package_objs,

        "customers": customer_obj,

        "requests": request_objs,

    }
    return render(request, "customer_detail.html", context)

def packages_list(request):
    return render(request, "packages_list.html")
