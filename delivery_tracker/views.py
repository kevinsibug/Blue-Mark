from django.shortcuts import render

from delivery_tracker.models import *

from datetime import date

# Create your views here.

def home(request):
    return render(request, "home.html")

def add_customer(request):
    return render(request, "add_customer.html")

def customer_confirmation(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    address = request.POST['address']
    originarea = request.POST['originarea']
    phonenum = request.POST['phonenum']

    recipientfirstname = request.POST['recipientfirstname']
    recipientlastname = request.POST['recipientlastname']
    recipientaddress = request.POST['recipientaddress']
    recipientphone = request.POST['recipientphone']

    destinationarea = request.POST['destinationarea']
    servicetype = request.POST['servicetype']
    packagetype = request.POST['packagetype']
    packageweight = request.POST['packageweight']


    deliverystaff = Delivery_Staff(staff_firstname="Juan", staff_lastname="Dela Cruz")
    deliverystaff.save()

    customer = Customer(firstname=firstname, lastname=lastname, address=address, phone=phonenum)
    customer.save()

    recipient = Recipient(firstname=recipientfirstname, lastname=recipientlastname, address=recipientaddress, phone=recipientphone)
    recipient.save()

    service = Service(service_type=servicetype)
    service.save()

    if service.service_type == 'Express':
        service = Service(service_type=servicetype, delivery_time='Next Day')
        service.save()
    elif service.service_type == 'Ordinary':
        service = Service(service_type=servicetype, delivery_time='3 to 4 Days')
        service.save()

    route = Route(origin_area=originarea, destination_area=destinationarea)
    route.save()

    package = Package(package_type=packagetype, package_weight=packageweight)
    package.save()

    if service.service_type == 'Express' and route.origin_area == 'Luzon' and route.destination_area == 'Luzon' :
        if package.package_type == 'LTR':
            if int(packageweight) > 0 and int(packageweight) < 100:
                weightcostmatrix = Weight_Cost_Matrix(
                base_weight=int(packageweight),
                base_cost=70.00,
                increment_weight=0,
                increment_cost=0,
                service=service,
                route=route
                )
                weightcostmatrix.save()

                deliveryrequest = Delivery_Request(
                request_date=date.today(),
                total_cost=(weightcostmatrix.base_cost + weightcostmatrix.increment_cost),
                customer=customer,
                service=service,
                package=package,
                route=route,
                weight_cost_matrix=weightcostmatrix,
                receiver=recipient
                )
                deliveryrequest.save()

            elif int(packageweight) >= 100 and int(packageweight) < 200:
                weightcostmatrix = Weight_Cost_Matrix(
                base_weight=100,
                base_cost=70.00,
                increment_weight=int(packageweight) -100,
                increment_cost=35.00,
                service=service,
                route=route
                )
                weightcostmatrix.save()

                deliveryrequest = Delivery_Request(
                request_date=date.today(),
                total_cost=(weightcostmatrix.base_cost + weightcostmatrix.increment_cost),
                customer=customer,
                service=service,
                package=package,
                route=route,
                weight_cost_matrix=weightcostmatrix,
                receiver=recipient
                )
                deliveryrequest.save()

        elif package.package_type == 'PCK':
            if int(packageweight) >= 200 and int(packageweight) < 500:
                weightcostmatrix = Weight_Cost_Matrix(
                base_weight=int(packageweight),
                base_cost=90.00,
                increment_weight=0,
                increment_cost=0,
                service=service,
                route=route
                )
                weightcostmatrix.save()

                deliveryrequest = Delivery_Request(
                request_date=date.today(),
                total_cost=(weightcostmatrix.base_cost + weightcostmatrix.increment_cost),
                customer=customer,
                service=service,
                package=package,
                route=route,
                weight_cost_matrix=weightcostmatrix,
                receiver=recipient
                )
                deliveryrequest.save()

            elif int(packageweight) >= 500 and int(packageweight) < 1000:
                weightcostmatrix = Weight_Cost_Matrix(
                base_weight=500,
                base_cost=90.00,
                increment_weight=int(packageweight)-500,
                increment_cost=45.00,
                service=service,
                route=route
                )
                weightcostmatrix.save()

                deliveryrequest = Delivery_Request(
                request_date=date.today(),
                total_cost=(weightcostmatrix.base_cost + weightcostmatrix.increment_cost),
                customer=customer,
                service=service,
                package=package,
                route=route,
                weight_cost_matrix=weightcostmatrix,
                receiver=recipient
                )
                deliveryrequest.save()

        elif package.package_type == 'PAR':
            if int(packageweight) >= 1000 and int(packageweight) < 1500:
                weightcostmatrix = Weight_Cost_Matrix(
                base_weight=int(packageweight),
                base_cost=150.00,
                increment_weight=0,
                increment_cost=0,
                service=service,
                route=route
                )
                weightcostmatrix.save()

                deliveryrequest = Delivery_Request(
                request_date=date.today(),
                total_cost=(weightcostmatrix.base_cost + weightcostmatrix.increment_cost),
                customer=customer,
                service=service,
                package=package,
                route=route,
                weight_cost_matrix=weightcostmatrix,
                receiver=recipient
                )
                deliveryrequest.save()

            elif int(packageweight) >= 1500 and int(packageweight) < 2000:
                weightcostmatrix = Weight_Cost_Matrix(
                base_weight=1500,
                base_cost=150.00,
                increment_weight=int(packageweight)-1500,
                increment_cost=75.00,
                service=service,
                route=route
                )
                weightcostmatrix.save()

                deliveryrequest = Delivery_Request(
                request_date=date.today(),
                total_cost=(weightcostmatrix.base_cost + weightcostmatrix.increment_cost),
                customer=customer,
                service=service,
                package=package,
                route=route,
                weight_cost_matrix=weightcostmatrix,
                receiver=recipient
                )
                deliveryrequest.save()


        elif package.package_type == 'BOX':
            if int(packageweight) >= 2000 and int(packageweight) < 2500:
                weightcostmatrix = Weight_Cost_Matrix(
                base_weight=int(packageweight),
                base_cost=170.00,
                increment_weight=0,
                increment_cost=0,
                service=service,
                route=route
                )
                weightcostmatrix.save()

                deliveryrequest = Delivery_Request(
                request_date=date.today(),
                total_cost=(weightcostmatrix.base_cost + weightcostmatrix.increment_cost),
                customer=customer,
                service=service,
                package=package,
                route=route,
                weight_cost_matrix=weightcostmatrix,
                receiver=recipient
                )
                deliveryrequest.save()

            elif int(packageweight) >= 2500 and int(packageweight) < 3000:
                weightcostmatrix = Weight_Cost_Matrix(
                base_weight=1500,
                base_cost=170.00,
                increment_weight=int(packageweight)-2500,
                increment_cost=85.00,
                service=service,
                route=route
                )
                weightcostmatrix.save()

                deliveryrequest = Delivery_Request(
                request_date=date.today(),
                total_cost=(weightcostmatrix.base_cost + weightcostmatrix.increment_cost),
                customer=customer,
                service=service,
                package=package,
                route=route,
                weight_cost_matrix=weightcostmatrix,
                receiver=recipient
                )
                deliveryrequest.save()


    return render(request,'customerconfirmation.html',
        {'requestdate': request.POST.get('requestdate'),
        'firstname': request.POST.get('firstname'),
        'lastname': request.POST.get('lastname'),
        'address': request.POST.get('address'),
        'originarea': request.POST.get('originarea'),
        'phonenum': request.POST.get('phonenum'),
        'recipientfirstname': request.POST.get('recipientfirstname'),
        'recipientlastname': request.POST.get('recipientlastname'),
        'destinationarea': request.POST.get('destinationarea'),
        'recipientaddress': request.POST.get('recipientaddress'),
        'recipientphone': request.POST.get('recipientphone'),
        'servicetype': request.POST.get('servicetype'),
        'packagetype': request.POST.get('packagetype'),
        'packageweight': request.POST.get('packageweight'),
        'totalcost': deliveryrequest.total_cost,
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
