from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.




class Category(models.Model):
    name_category = models.CharField(max_length=200)

    def __str__(self):
        return self.name_category


class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(blank=False, null=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class ImageProduct(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title

class CartItem(models.Model):
    cart = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.quantity
