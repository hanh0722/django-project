from django.urls import path
from .views import shop, productDetail
urlpatterns = [
    path('', shop, name='collection'),
    path('<slug:slug_product>', productDetail, name='item_slug')
]
