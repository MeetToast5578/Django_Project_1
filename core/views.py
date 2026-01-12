from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.forms import ContactForm
from django.contrib import messages
from product.models import Product, ProductCategory
# Create your views here.


def homepage(request):
    products = Product.objects.all() # Django ORM 
    categories = ProductCategory.objects.filter(parent = None)
    
    context = {
        'products' : products,
        'categories' : categories
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.WARNING, "Successfully Sent!")
            return redirect(reverse_lazy('contact'))
    context = {
        'form' : form
    }
    return render(request, 'contact.html', context)

def faq(request):
    return render(request, 'faq.html')

def error_404_view(request, exception = None):
    return render(request, '404.html', status=404)