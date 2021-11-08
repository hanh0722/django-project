from collections import namedtuple

from django.db.models.expressions import F
from .isAuthenticated import isAuthenticated
from authorization.models import Customer, CartCustomer
from shop.models import Item


def listOfDictToObject(dictionary: dict):
    item = namedtuple('Item', dictionary.keys())
    return item


def getCartOfCustomer(request):
    if not isAuthenticated(request):
        return []

    customer = Customer.objects.get(user_id=request.user.id)
    list__items__filter = CartCustomer.objects.filter(customer_id=customer.id).select_related('item')
    # innerJoin command SQL
    print(list__items__filter.first().__dict__)
    return list__items__filter
