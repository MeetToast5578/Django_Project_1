from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.forms import ContactForm
from django.contrib import messages
from core.tasks import export
from product.models import Product, ProductCategory, WishList, BestSeller
from order.models import Basket
from blog.models import BLog
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _
# Create your views here.




def export_view(request):
    export.delay()
    return HttpResponse('Export Done!')

def homepage(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user = request.user, is_active = True).first()
        wishlist = WishList.objects.filter(user = request.user).first()
    else:
        basket = None
        wishlist = None
    products = Product.objects.all() # Django ORM 
    categories = ProductCategory.objects.filter(parent = None)
    blogs = BLog.objects.all()[:3]
    bestsellers = BestSeller.objects.all()[:4]
    
    context = {
        'products' : products,
        'categories' : categories,
        'basket' : basket,
        'wishlist' : wishlist,
        'blogs' : blogs,
        'bestsellers' : bestsellers
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    # context_object_name = 'form'
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.WARNING, _("Successfully Sent!"))
        return super().form_valid(form)
    

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