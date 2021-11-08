from django.contrib import admin
from django.contrib.auth.models import User
from .models import CartCustomer, Customer
# Register your models here.


admin.site.register(Customer)
admin.site.register(CartCustomer)