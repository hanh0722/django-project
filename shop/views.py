from django.shortcuts import render

# Create your views here.

def shop(request):
    return render(request, 'collection.html')

def productDetail(request, slug_product):
    print(slug_product)
    return render(request, 'product-detail.html')