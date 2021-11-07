from django.db import models
from django.contrib.auth.models import User
# from shop.models import CartItem
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
