from django.shortcuts import redirect, render

from shop.models import Item

# Create your views here.
cart={}
def addCart(request): 
    id=request.POST.get('id')
    num=request.POST.get('quantity')

    proDetail = Item.object.get(pro_id=id)

    if not request.user.is_authenticated: 

        return redirect('/account/login')

    if id in cart.key(): 
        itemCart={ 
            'title':proDetail.title,
            'price':proDetail.price,
            'category':proDetail.category,
            'quantity':int(cart[id]['quantity'])+1
        }
    else: 
        itemCart={
            'title':proDetail.title,
            'price':proDetail.price,
            'category':proDetail.category,
            'quantity':num
        }

    cart[id]=itemCart
    request.session['cart']=cart
    
