from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.apps import apps
from .employee_helpers import date_checker
from django.db.models import Q
from .models import Employee
from django.contrib.auth.decorators import login_required
from datetime import date
# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Employee model from the other app, it can now be used to query the db for Customers
    logged_in_user = request.user
    try:
        logged_in_employee = Employee.objects.get(user=logged_in_user)
        
        today = date.today().weekday()

        todays_date = date.today()

        weekday = date_checker(today)

        Customer = apps.get_model('customers.Customer')

        my_customers = Customer.objects.filter(zip_code=logged_in_employee.zip_code)

        my_pickups = my_customers.filter(Q(weekly_pickup=weekday) | Q(one_time_pickup=todays_date))

        non_suspended_pickups = my_pickups.exclude(suspend_start__lte=todays_date, suspend_end__gte=todays_date)
        
        final_pickups = non_suspended_pickups.exclude(date_of_last_pickup=todays_date)

        data_visualization = [item for item in final_pickups]

        context = {
                'logged_in_employee': logged_in_employee,
                'final_pickups': final_pickups,
                'today': today

        }

        return render(request, 'employees/index.html', context)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('employees:create'))

@login_required
def create(request):
    logged_in_user = request.user
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        address_from_form = request.POST.get('address')
        zip_from_form = request.POST.get('zip_code')
        new_employee = Employee(name=name_from_form, user=logged_in_user, address=address_from_form, zip_code=zip_from_form)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')

@login_required
def edit_profile(request):
    logged_in_user = request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        address_from_form = request.POST.get('address')
        zip_from_form = request.POST.get('zip_code')
        logged_in_employee.name = name_from_form
        logged_in_employee.address = address_from_form
        logged_in_employee.zip_code = zip_from_form
        logged_in_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        context = {
            'logged_in_employee': logged_in_employee
        }
        return render(request, 'employees/edit_profile.html', context)

def confirm_pickup(request, customer_id):
    Customer = apps.get_model('customers.Customer')
    single_customer = Customer.objects.get(id=customer_id)
    if request.method == 'POST':
        last_pickup_from_form = request.POST.get('date')
        single_customer.date_of_last_pickup = last_pickup_from_form
        single_customer.balance -= 20
        single_customer.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        context = {
            'single_customer': single_customer,
            'customer_id': customer_id
        }
        return render(request, 'employees/confirm_pickup.html', context)


def weekly_pickup_filter(request, weekday=''):
    if request.method == 'POST':
        filter_value = request.POST.get('weekday_selection')
        Customer = apps.get_model('customers.Customer')
        list_of_todays_pickups = Customer.objects.filter(weekly_pickup=filter_value)
        data_visualization = [item for item in list_of_todays_pickups]
        context = {
            'list_of_todays_pickups': list_of_todays_pickups
        }
        return render(request, 'employees/weekly_pickup_filter.html', context)
    else:
        return render(request, 'employees/weekly_pickup_filter.html')