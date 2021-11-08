from django.shortcuts import redirect, render
from util.checkIsValidation import isValidation
from shop.models import Item
from authorization.models import Customer, CartCustomer, Item
# Create your views here.
def addItemToCart(request, product_id):
    isValidation(request, '/account/login', 'Please login before shopping!')
    customer = Customer.objects.get(user_id=request.user.id)
    item = Item.objects.get(id=product_id)
    productIsExisted = CartCustomer.objects.filter(item__id=product_id).first()
    try:
        if not productIsExisted:
            add_item_to_cart = CartCustomer(customer=customer, item=item, quantity=1)
            add_item_to_cart.save()
            return redirect('/')
            # save if we dont have
        else:
            quantity_product = productIsExisted.quantity
            CartCustomer.objects.filter(item__id=product_id).update(quantity= quantity_product + 1)
            # update quantity
            return redirect('/')
    except Exception as error:
        print(error)
        return redirect('/404')


