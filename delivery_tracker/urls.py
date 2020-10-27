from django.urls import path

from . import views


urlpatterns = [

    path('', views.home, name="home"),
    path('createdeliveryrequest/', views.create_delivery_request, name='create_delivery_request'),
    path('createdeliveryrequest/customerconfirmation/', views.customer_confirmation, name='customerconfirmation'),
    path('viewcustomers/', views.view_customers, name='view_customers'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('trackpackages/', views.packages_list, name='packages_list'),
    path('reports/', views.reports_page, name='reports_page'),
    path('reportsarea/', views.reports, name='reports')
]
