from django.contrib import messages
from django.shortcuts import redirect
from util.checkIsValidation import isValidation
from shop.models import Item
from authorization.models import Customer, CartCustomer, Item
# Create your views here.


def deleteProduct(productId):
    CartCustomer.objects.filter(item__id=productId).delete()


def addItemToCart(request, product_id):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user_id=request.user.id)
        item = Item.objects.get(id=product_id)
        productIsExisted = CartCustomer.objects.filter(item__id=product_id, customer__user__id=request.user.id).first()
        try:
            if not productIsExisted:
                add_item_to_cart = CartCustomer(
                    customer=customer, item=item, quantity=1)
                add_item_to_cart.save()
                return redirect('/checkout')
                # save if we dont have
            else:
                quantity_product = productIsExisted.quantity
                CartCustomer.objects.filter(item__id=product_id).update(
                    quantity=quantity_product + 1)
                # update quantity
                return redirect('/checkout')
        except Exception as error:
            print(error)
            return redirect('/404')
    else:
        messages.warning(request, 'Please login before shopping!')
        return redirect('/account/login')


def removeItemInCart(request, product_id):
    isValidation(request, '/account/login',
                 'You have to login before continue')
    try:
        productFilter = CartCustomer.objects.filter(item__id=product_id)
        productIsExisted = productFilter.first()
        quantity_product = productIsExisted.quantity
        if quantity_product == 1:
            deleteProduct(product_id)
        else:
            productFilter.update(quantity=quantity_product - 1)
        return redirect('/checkout')
    except Exception as error:
        print(error)
        redirect('/404')

def removeCompletelyItem(request, product_id):
    isValidation(request, '/account/login', 'You have to login before continue')
    try:
        deleteProduct(product_id)
        return redirect('/')
    except Exception as error:
        print(error)
        redirect('/404')