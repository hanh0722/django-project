from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def signIn(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    return render(request, 'form.html', {
        'signIn': True,
    })

def register(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    return render(request, 'form.html', {
        'signIn': False
    })


def registerUser(request):
    try:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        userIsExisted = User.objects.filter(email = email).first()
        if userIsExisted is not None:
            messages.warning(request, 'Email is existed')
            return redirect('/account/register')
        user = User.objects.create_user(username = email, email = email, password = password, last_name = name)
        customer = Customer(user=user)
        customer.save()
        return render(request, 'form.html', {
            'signIn': True,
            'message': 'Register Successfully',
            'code': 200
        })
    except Exception as error:
        messages.warning(request, 'Something went wrong, try again')
        print(error)
        return redirect('/account/register')

def signInUser(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        checkEmailIsValid = User.objects.filter(username = email).first()
        if checkEmailIsValid is None:
            messages.warning(request, 'User is not existed')
            return redirect('/account/login')
        validateUser = authenticate(username = email, password = password)
        if validateUser is None:
            messages.warning(request, 'Email or password is wrong')
            return redirect('/account/login')
        login(request, validateUser)
        return redirect('/')
    except Exception as error:
        messages.warning(request, 'Something went wrong, try again')
        return redirect('/account/login')