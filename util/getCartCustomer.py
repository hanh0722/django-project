from collections import namedtuple
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
    cart_customer = CartCustomer.objects.filter(
        customer_id=customer.id).values()
    turn_cart_to_list = list(cart_customer)
    array_id_item = []
    quantity_item = []
    for value in turn_cart_to_list:
        item_id = value['item_id']
        array_id_item.append(item_id)
        quantity_item.append(value['quantity'])

    list_item_cart = Item.objects.filter(id__in=array_id_item).values()
    list_object = []
    for index in range(len(list_item_cart)):
        list_item_cart[index]['quantity'] = quantity_item[index]
        list_item_cart[index]['total'] = quantity_item[index] * list_item_cart[index]['price']
    
    turnObject = list(map(listOfDictToObject, list_item_cart))
    print(turnObject)
    return list_item_cart
