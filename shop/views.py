from django.shortcuts import render
from .models import Item
import math
from django.core.paginator import Paginator
from util.isAuthenticated import isAuthenticated
# Create your views here.

def shop(request):
    page = request.GET.get('page')
    page = page or 1
    items_in_store = Item.objects.all().order_by('id').reverse()
    PER_PAGE = 4
    item_render = Paginator(items_in_store, PER_PAGE)
    page_product = item_render.get_page(page)
    total_item = item_render.count
    page_range = item_render.page_range
    return render(request, 'collection.html', {
        'products': page_product,
        'range_pagination': page_range,
        'total_record': total_item,
        'has_previous_page': page_product.has_previous(),
        'has_next_page': page_product.has_next(),
        'next_page': int(page) + 1,
        'current_page': int(page),
        'isAuthenticated': isAuthenticated(request)
    })

def productDetail(request, slug_product):
    item_data = Item.objects.get(slug=slug_product)
    return render(request, 'product-detail.html', {
        'product': item_data,
        'isAuthenticated': isAuthenticated(request)
    })