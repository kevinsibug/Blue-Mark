from django.shortcuts import render

from delivery_tracker.models import *

# Create your views here.

def home(request):
    return render(request, "home.html")

def add_customer(request):
    return render(request, "add_customer.html")

def customer_confirmation(request):
    # firstname = request.POST['firstname']
    # lastname = request.POST['lastname']
    # address = request.POST['address']
    originarea = request.POST['originarea']
    # phonenum = request.POST['phonenum']
    #
    # recipientfirstname = request.POST['recipientfirstname']
    # recipientlastname = request.POST['recipientlastname']
    # recipientaddress = request.POST['recipientaddress']
    # recipientphone = request.POST['recipientphone']

    destinationarea = request.POST['destinationarea']
    servicetype = request.POST['servicetype']
    packagetype = request.POST['packagetype']
    packagebweight = request.POST['packagebweight']
    packagesweight = request.POST['packagesweight']

    deliverystaff = Delivery_Staff(staff_firstname="Juan", staff_lastname="Dela Cruz")
    deliverystaff.save()

    # customer = Customer(firstname=firstname, lastname=lastname, address=address, phone=phonenum)
    # customer.save()

    service = Service(service_type=servicetype)
    service.save()

    route = Route(origin_area=originarea, destination_area=destinationarea)
    route.save()

    # recipient = Recipient(firstname=recipientfirstname, lastname=recipientlastname, address=recipientaddress, phone=recipientphone)
    # recipient.save()

    package = Package(package_type=packagetype, package_weight=packagebweight)
    package.save()

    weightcostmatrix = Weight_Cost_Matrix(base_weight=packagebweight, increment_weight=packagesweight, service=service, route=route)
    weightcostmatrix.save()

    return render(request,'customerconfirmation.html',
        # {'firstname': request.POST.get('firstname'),
        # 'lastname': request.POST.get('lastname'),
        # 'address': request.POST.get('address'),
        {'originarea': request.POST.get('originarea'),
        # 'phonenum': request.POST.get('phonenum'),
        # 'recipientfirstname': request.POST.get('recipientfirstname'),
        # 'recipientlastname': request.POST.get('recipientlastname'),
        'destinationarea': request.POST.get('destinationarea'),
        # 'recipientaddress': request.POST.get('recipientaddress'),
        # 'recipientphone': request.POST.get('recipientphone'),
        'servicetype': request.POST.get('servicetype'),
        'packagetype': request.POST.get('packagetype'),
        'packagebweight': request.POST.get('packagebweight'),
        'packagesweight': request.POST.get('packagesweight')
        })

def view_customers(request):

    customer_objs  = Customer.objects.all()

    context = {
        "customers": customer_objs
    }
    return render(request, "view_customers.html", context)

def customer_detail(request, pk):

    customer_obj = Customer.objects.get(pk=pk)


    request_objs = Delivery_Request.objects.filter(customer_id=customer_obj.id)


    context = {

        "customers": customer_obj,

        "requests": request_objs,

    }
    return render(request, "customer_detail.html", context)

def packages_list(request):
    request_objs = Delivery_Request.objects.all()

    context = {
        "requests": request_objs,
    }
    return render(request, "packages_list.html", context)

def reports_page(request):
    request_objs = Delivery_Request.objects.all()

    context = {
        "requests": request_objs,
    }
    return render(request, "reports_page.html", context)

def reports(request):
    origin = request.GET['origin']
    destination = request.GET['destination']

    request_objs = Delivery_Request.objects.filter(route__origin_area=origin).filter(route__destination_area=destination)

    context = {
        "origin": origin,
        "destination": destination,
        "requests": request_objs
    }

    return render(request, "reports.html", context)
