from django.shortcuts import render

from delivery_tracker.models import *


# Create your views here.
def package_detail(request, pk):

    customer_obj = Driver.objects.get(pk=pk)

    car_objs = Car.objects.filter(owner_id=owner_obj.id)

    context = {

        "vehicles": car_objs,

        "drivers": owner_obj,

    }

    return render(request, "car_detail.html", context)