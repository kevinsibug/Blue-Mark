from django.urls import path

from . import views


urlpatterns = [

    path('', views.home, name="home"),
    path('addcustomer/', views.add_customer, name='add_customer'),
    path('addcustomer/customerconfirmation/', views.customer_confirmation, name='customerconfirmation'),
    path('viewcustomers/', views.view_customers, name='view_customers'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('trackpackages/', views.packages_list, name='packages_list'),
    path('reports/', views.reports_page, name='reports_page')
]
