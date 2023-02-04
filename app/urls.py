from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('customer/new', views.AddCustomer, name="customer.new"),
    path('customer/edit/<int:id>', views.EditCustomer, name="customer.edit"),
    # path('customer/update/<int:id>', views.UpdateCustomer, name="customer.update"),
    path('customer/delete/<int:id>', views.destory, name="customer.delete"),
    path('customer/lists', views.CustomerList, name="customer.all"),
]
