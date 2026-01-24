from django.urls import path
from .views import blog_single, blog, blog_create

urlpatterns = [
    path('blog-single/<str:slug>/', blog_single, name='blog_single'),
    path('blog/', blog, name='blog'),
    path('blog-create/', blog_create, name='blog_create'),
]