from django.db import models
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
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.title






