from django.urls import path
from .views import cart, checkout, empty_cart, update_item

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('empty-cart/', empty_cart, name='empty_cart'),
    path('update-item/', update_item, name = 'update-item'),
]