from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import CustomerForm
from .models import Customer
from django.http import JsonResponse
from django.core import serializers


def dashboard(request):
    return render(request, "app/dashboard.html", {})


def AddCustomer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/customer/new')
            except:
                pass
    else:
        form = CustomerForm()
    return render(request, "app/customer_add.html", {'form': form})


def CustomerList(request):
    customers = Customer.objects.all()
    return render(request, "app/customer_list.html", {'customers': customers})
    # serialized_obj = serializers.serialize('json', [customers, ])
    # return JsonResponse(serialized_obj)


def EditCustomer(request, id):
    if request.method == "POST":
        UpdateCustomer(request, id)

    names = Customer.objects.all()
    customer = Customer.objects.get(id=id)
    return render(request, "app/customer_edit.html", {'customer': customer, 'names': names})


def UpdateCustomer(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST, instance=customer)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.path_info)
    return render(request, "app/customer_edit.html", {'customer': customer})


def destory(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('/customer/lists')
