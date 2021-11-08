from django.urls import path
from .views import addItemToCart

urlpatterns = [
    path('add-cart/<int:product_id>', addItemToCart)
]
