from django.db.models.expressions import F
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from shop.models import Item
import random
from authorization.models import CartCustomer, Customer
from util.isAuthenticated import isAuthenticated
from util.getCartCustomer import getCartOfCustomer
# Create your views here.


def index(request):
    userIsAuthenticated = isAuthenticated(request)
    cart_user = getCartOfCustomer(request)
    # if userIsAuthenticated:
    #     userId = request.user.id
    #     customer = Customer.objects.get(user_id=userId)
    #     cart_customer = CartCustomer.objects.filter(customer_id=customer.id).values()
    #     turn_cart_to_list = list(cart_customer)
    #     array_id_item = []
    #     quantity_item = []
    #     for value in turn_cart_to_list:
    #         item_id = value['item_id']
    #         array_id_item.append(item_id)
    #         quantity_item.append(value['quantity'])

        

    #     list_item_cart = Item.objects.filter(id__in=array_id_item).values()
    #     for index in range(len(list_item_cart)):
    #         list_item_cart[index]['quantity'] = quantity_item[index]
    #         list_item_cart[index]['total'] = quantity_item[index] * list_item_cart[index]['price']
        

    items = Item.objects.all().order_by('id').reverse()
    randoms_item = list((random.choice(items), random.choice(items)))
    return render(request, 'index.html', {
        'products': items[:5],
        'item_everyday': randoms_item,
        'isAuth': request.user.is_authenticated,
        'isAuthenticated': userIsAuthenticated,
        'cart_user': cart_user
    })

def NotFound(request):
    cart_user = getCartOfCustomer(request)
    return render(request, '404.html', {
        'isAuthenticated': request.user.is_authenticated,
        'cart_user': cart_user
    })

def Logout(request):
    logout(request)
    return redirect('/account/login')