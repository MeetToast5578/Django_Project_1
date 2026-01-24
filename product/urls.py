from django.urls import path
from .views import ShopDetailView, compare, shop_left_sidebar, single_product, ShopListView

urlpatterns = [
    path('compare/', compare, name='compare'),
    path('shop-left-sidebar/', ShopListView.as_view(), name='shop_left_sidebar'),
    path('single-product/<str:slug>/', ShopDetailView.as_view(), name='single_product'),
]
