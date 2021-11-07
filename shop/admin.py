from django.contrib import admin
from .models import Item, Category, ImageProduct
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category',)
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(ImageProduct)