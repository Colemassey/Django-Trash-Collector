from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps

from .models import Employee
from django.contrib.auth.decorators import login_required
# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')


# @login_required
# def edit_profile(request):
#     logged_in_user = request.user
#     logged_in_employee = Employee.objects.get(user=logged_in_user)
#     if request.method == "POST":
#         name_from_form = request.POST.get('name')
#         address_from_form = request.POST.get('address')
#         zip_from_form = request.POST.get('zip_code')
#         todays_pickups = Customer.weekly_pickup
#         logged_in_employee.name = name_from_form
#         logged_in_employee.address = address_from_form
#         logged_in_employee.zip_code = zip_from_form
#         logged_in_employee.weekly_pickup = weekly_pickup_from_form
#         logged_in_employee.save()
#         return HttpResponseRedirect(reverse('employee:index'))
#     else:
#         context = {
#             'logged_in_employee': logged_in_employee
#         }
#         return render(request, 'employees/edit_profile.html', context)