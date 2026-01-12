from django.shortcuts import render

# Create your views here.

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def empty_cart(request):
    return render(request, 'empty-cart.html')