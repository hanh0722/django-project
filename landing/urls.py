from django.urls import path
from .views import NotFound, index
urlpatterns = [
    path('', index, name='home_page'),
    path('404', NotFound, name='not_found')
]
