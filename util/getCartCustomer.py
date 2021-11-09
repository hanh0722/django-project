from collections import namedtuple

from django.db.models.expressions import F
from .isAuthenticated import isAuthenticated
from authorization.models import Customer, CartCustomer
from shop.models import Item


def listOfDictToObject(dictionary: dict):
    item = namedtuple('Item', dictionary.keys())
    return item


def getCartOfCustomer(request):
    # if request.user.is_superuser:
    #     return None
    if not isAuthenticated(request):
        return None

    customer = Customer.objects.get(user_id=request.user.id)
    userId = customer.user_id
    list__items__filter = CartCustomer.objects.filter(customer__user__id=userId).select_related('item')
    # innerJoin command SQL
    return list__items__filter

# def removeCartOfUser():
