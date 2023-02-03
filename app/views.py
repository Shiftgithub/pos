from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer


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


def EditCustomer(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, "app/customer_edit.html", {'customer': customer})


def UpdateCustomer(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "app/customer_edit.html", {'customer': customer})


def destory(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('/customer/lists')
