from util.getCartCustomer import getCartOfCustomer
def getTotalCart(request):
    cart_user = getCartOfCustomer(request)
    value = 0
    for item in cart_user:
        quantity = item.quantity
        price = item.item.price
        value = value + quantity * price
    
    return value