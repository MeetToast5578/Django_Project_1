from django.urls import path
from product.api.views import (
    categories,
    products,
    product_update,
    ProductListAPIView,
    ProductUpdateDeleteAPIView,
    SubscriberAPIView,
    CategoryListApiView,
    ProductTagListAPIView,
)

urlpatterns = [
    path("categories/", CategoryListApiView.as_view(), name="categories"),
    path("products/", ProductListAPIView.as_view(), name="products"),
    path('tags/', ProductTagListAPIView.as_view(), name = 'tags'),
    path(
        "product/<int:pk>/", ProductUpdateDeleteAPIView.as_view(), name="product_update"
    ),
    path('subscriber/', SubscriberAPIView.as_view(), name = 'subscriber')
]