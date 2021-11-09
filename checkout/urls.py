from django.urls import path
from .views import checkout, index, success
urlpatterns = [
    path('', index, name='checkout'),
    path('success', success, name='success-checkout'),
    path('submit', checkout, name='submit')
]