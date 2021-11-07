from django.db import models
from shop.models import Item
from django.contrib.auth.models import User
# Create your models here.

# class CartItem(models.Model):
#     cart = models.ForeignKey(Item, on_delete=models.CASCADE)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=0)

