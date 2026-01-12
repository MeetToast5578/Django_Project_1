from django.urls import path
from .views import cart, checkout, empty_cart

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('empty-cart/', empty_cart, name='empty_cart'),
]