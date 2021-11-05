from django.urls import path
from .views import signIn, register
urlpatterns = [
    path('login', signIn, name='sign-in'),
    path('register', register, name='register')
]