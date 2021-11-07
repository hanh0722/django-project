from django.shortcuts import render
from shop.models import Item
import random
# Create your views here.

def index(request):
    items = Item.objects.all().order_by('id').reverse()
    randoms_item = list((random.choice(items), random.choice(items)))
    return render(request, 'index.html', {
        'products': items[:5],
        'item_everyday': randoms_item,
        'isAuth': request.user.is_authenticated
    })
