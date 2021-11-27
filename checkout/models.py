from django.db import models
from authorization.models import Customer
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contact = models.CharField(max_length=200)
    name = models
