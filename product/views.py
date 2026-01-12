from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Product, ProductCategory, ProductColor, ProductSize
# Create your views here.

def compare(request):
    return render(request, 'compare.html')

def shop_left_sidebar(request):
    products = Product.objects.all() # Django ORM 
    categories = ProductCategory.objects.filter(parent = None)
    colors = ProductColor.objects.values('color_name').annotate(count=Count('color_name')).order_by('color_name')
    sizes = ProductSize.objects.values('size_name').annotate(count=Count('size_name')).order_by('size_name')

    context = {
        'products' : products,
        'categories' : categories,
        'colors' : colors,
        'sizes' : sizes
    }
    return render(request, 'shop-left-sidebar.html', context)

def single_product(request, pk):
    product = get_object_or_404(Product, id = pk)

    context = {
        'product' : product
    }
    return render(request, 'single-product.html', context)