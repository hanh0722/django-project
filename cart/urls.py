from django.urls import path
from .views import addItemToCart, removeCompletelyItem, removeItemInCart

urlpatterns = [
    path('add/<int:product_id>', addItemToCart, name='add-to-cart'),
    path('remove/<int:product_id>', removeItemInCart, name='remove-item'),
    path('delete/<int:product_id>', removeCompletelyItem, name='delete-item')
]
