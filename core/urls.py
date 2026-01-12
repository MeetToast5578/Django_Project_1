from django.urls import path
from .views import error_404_view, faq, homepage, about, contact

urlpatterns = [
    path('', homepage, name = 'home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('404/', error_404_view, name='404'),
]