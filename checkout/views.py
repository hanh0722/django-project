from django.contrib.messages.api import error
from django.shortcuts import redirect, render
from django.contrib import messages
from util.isAuthenticated import isAuthenticated
from util.getCartCustomer import getCartOfCustomer
from util.getTotalCart import getTotalCart
# Create your views here.

def index(request):
    isAuth = isAuthenticated(request)
    if not isAuth:
        messages.warning(request, 'You have to login before continue')
        return redirect('/account/login')
    cart_user = getCartOfCustomer(request)
    total = getTotalCart(request)
    return render(request, 'checkout.html', {
        'isAuthenticated': isAuth,
        'cart_user': cart_user,
        'basic_information': request.user,
        'total': total
    })

def success(request):
    isAuth = isAuthenticated(request)
    return render(request, 'success.html', {
        'isAuthenticated': isAuth
    })

def checkout(request):
    isAuth = isAuthenticated(request)
    if not isAuth:
        messages.warning(request, 'The URL is expired, please login again')
        return redirect('/account/login')
    contact = request.POST['contact']
    name = request.POST['name']
    address = request.POST['address']
    city = request.POST['city']
    phone = request.POST['phone']
    code = request.POST['code']
    try:
        name
    except Exception as error:
        print(error)
        redirect('/404')

