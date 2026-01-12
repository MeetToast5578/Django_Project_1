from django.urls import path
from .views import blog_single

urlpatterns = [
    path('blog-single/', blog_single, name='blog_single'),
]