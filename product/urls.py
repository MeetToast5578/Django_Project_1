from django.urls import path
from .views import compare, shop_left_sidebar, single_product

urlpatterns = [
    path('compare/', compare, name='compare'),
    path('shop-left-sidebar/', shop_left_sidebar, name='shop_left_sidebar'),
    path('single-product/<int:pk>/', single_product, name='single_product'),
]
