from django.urls import path
from .views import signIn, register, registerUser, signInUser
urlpatterns = [
    path('login', signIn, name='sign-in'),
    path('register', register, name='register'),
    path('register/create-user', registerUser, name='create-user'),
    path('signin', signInUser, name='login')
]