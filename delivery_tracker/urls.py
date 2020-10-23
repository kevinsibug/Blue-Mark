from django.urls import path

from . import views



urlpatterns = [

    path("<int:pk>/", views.customer_detail, name="customer_detail"),

]