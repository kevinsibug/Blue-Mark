from django.shortcuts import render

from delivery_tracker.models import *

from datetime import date

# Create your views here.

def home(request):
    return render(request, "home.html")

def create_delivery_request(request):
    return render(request, "create_delivery_request.html")

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

    customer_objs = Customer.objects.filter(firstname=firstname).filter(lastname=lastname)
    if (customer_objs):
        pass
    else:
        customer = Customer(firstname=firstname, lastname=lastname, address=address, phone=phonenum)
        customer.save()


    recipient_objs = Recipient.objects.filter(firstname=recipientfirstname).filter(lastname=recipientlastname)
    if (recipient_objs):
        pass
    else:
        recipient = Recipient(firstname=recipientfirstname, lastname=recipientlastname, address=recipientaddress, phone=recipientphone)
        recipient.save()


    package = Package(package_type=packagetype, package_weight=packageweight)
    package.save()


    customer_obj = Customer.objects.get(firstname = firstname, lastname = lastname)
    recipient_obj = Recipient.objects.get(firstname = recipientfirstname, lastname = recipientlastname)
    service_obj = Service.objects.get(service_type = servicetype)
    route_obj = Route.objects.get(origin_area = originarea, destination_area = destinationarea)
    weightcostmatrix_obj = Weight_Cost_Matrix.objects.get(service = service_obj, route = route_obj, package_type = packagetype)

    cost = 0
    weight = float(packageweight)
    if (weight < weightcostmatrix_obj.base_weight):
            cost = weightcostmatrix_obj.base_cost
    else:
        cost += weightcostmatrix_obj.base_cost
        weight -= weightcostmatrix_obj.base_weight
        normal_division = weight / weightcostmatrix_obj.increment_weight
        count = int(normal_division)
        cost += int(normal_division) * weightcostmatrix_obj.increment_cost
        if (normal_division - count) != 0:
            cost += weightcostmatrix_obj.increment_cost
    deliveryrequest = Delivery_Request(
        request_date=date.today(),
        total_cost=cost,
        customer=customer_obj,
        service=service_obj,
        package=package,
        route=route_obj,
        weight_cost_matrix=weightcostmatrix_obj,
        receiver=recipient_obj)

    deliveryrequest.save()

    return render(request,'customerconfirmation.html',

        {'requestdate': date.today(),
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

    for r in request_objs:
        try:
            receipt = Delivery_Receipt.objects.get(delivery_request = r)
        except Delivery_Receipt.DoesNotExist:
            receipt = False

        normal_division = str(r.package.package_weight / r.weight_cost_matrix.base_weight)
        modulo_division = str(r.package.package_weight % r.weight_cost_matrix.base_weight)
        weight = r.package.package_weight
        cost = 0

        if (r.package.package_weight < r.weight_cost_matrix.base_weight):
            cost = r.weight_cost_matrix.base_cost
        else:
            cost += r.weight_cost_matrix.base_cost
            weight -= r.weight_cost_matrix.base_weight
            normal_division = weight / r.weight_cost_matrix.increment_weight
            count = int(normal_division)
            cost += int(normal_division) * r.weight_cost_matrix.increment_cost

            if (normal_division - count) != 0:
                cost += r.weight_cost_matrix.increment_cost
        r.total_cost = cost
        r.save(update_fields=["total_cost"])


        if (receipt):
            r.delivered = "Delivered"
        else:
            r.delivered = "Not Delivered"
    context = {

        "customers": customer_obj,

        "requests": request_objs,

    }
    return render(request, "customer_detail.html", context)

def packages_list(request):
    request_objs = Delivery_Request.objects.all()

    for r in request_objs:
        try:
            receipt = Delivery_Receipt.objects.get(delivery_request = r)
        except Delivery_Receipt.DoesNotExist:
            receipt = False

        if (receipt):
            r.delivered = "Delivered"
        else:
            r.delivered = "Not Delivered"

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


    for r in request_objs:
        try:
            receipt = Delivery_Receipt.objects.get(delivery_request = r)
        except Delivery_Receipt.DoesNotExist:
            receipt = False

        if (receipt):
            r.delivered = "Delivered"
        else:
            r.delivered = "Not Delivered"
    context = {
        "origin": origin,
        "destination": destination,
        "requests": request_objs
    }

    return render(request, "reports.html", context)
