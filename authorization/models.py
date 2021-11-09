from django.db import models
from django.contrib.auth.models import User
from shop.models import Item
# from shop.models import CartItem
# Create your models here.

# class Item(models.Model):
#     title = models.CharField(max_length=200)
#     price = models.FloatField(max_length=200)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     slug = models.SlugField(blank=False, null=False, unique=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to='images')
    
#     def __str__(self):
#         return self.title

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart_user = models.ManyToManyField(Item, through='CartCustomer')
    def __str__(self):
        return f'username: {self.user.username} - id: {self.user.id}'
    # item is get automatically from cartCustomer model table 
    
class CartCustomer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.customer.user.username} - {self.item.title} - quantity: {self.quantity}'