from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('addcustomer/', views.add_customer, name='add_customer'),
    path('viewcustomers/', views.view_customers, name='view_customers'),
    path('<int:pk>/', views.customer_detail, name="customer_detail"),
    path('trackpackages/', views.packages_list, name='packages_list'),
]
