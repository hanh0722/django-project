from django.shortcuts import render

# Create your views here.

def signIn(request):
    return render(request, 'form.html', {
        'signIn': True
    })

def register(request):
    return render(request, 'form.html', {
        'signIn': False
    })