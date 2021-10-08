from django.urls import path
from .views import *

urlpatterns = [
    path('', Productslisting.as_view(), name='listing_prodcuts'),
]