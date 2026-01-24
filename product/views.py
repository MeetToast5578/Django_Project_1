from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Product, ProductCategory, ProductColor, ProductSize, ProductTag
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import ReviewForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
# Create your views here.

def compare(request):
    return render(request, 'compare.html')


class ShopListView(ListView):
    template_name = 'shop-left-sidebar.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 3
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        cat_id = self.request.GET.get('category')
        tag_id = self.request.GET.get('tag')
        size_id = self.request.GET.get('size')
        color_id = self.request.GET.get('color')
        if cat_id:
            queryset = queryset.filter(category = cat_id)
        if tag_id:
            queryset = queryset.filter(tags = tag_id)
        if size_id:
            queryset = queryset.filter(size = size_id)
        if color_id:
            queryset =queryset .filter(color = color_id)
        if cat_id and tag_id:
            queryset = queryset.filter(category = cat_id, tags = tag_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        full_queryset = self.get_queryset()
        
        # Add total count of ALL products (unfiltered)
        context['total_products_count'] = Product.objects.all().count()
        
        context['categories'] = ProductCategory.objects.filter(parent = None)
        context['colors'] = ProductColor.objects.filter(
            product__in=full_queryset
        ).values('color_name').annotate(count=Count('color_name')).order_by('color_name')
        context['sizes'] = ProductSize.objects.filter(
            product__in=full_queryset
        ).values('size_name').annotate(count=Count('size_name')).order_by('size_name')
        context['tags'] = ProductTag.objects.all()
        return context
    
    
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

class ShopDetailView(FormMixin, DetailView):
    form_class = ReviewForm
    model = Product # product
    template_name = 'single-product.html'
    success_url = reverse_lazy('home')
    # context_object_name = 'product'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        product = self.get_object()
        if form.is_valid():
            form.instance.user = self.request.user
            form.instance.product = product
            form.save()
        return self.get(request, *args, **kwargs)


def single_product(request, pk):
    product = get_object_or_404(Product, id = pk)

    context = {
        'product' : product
    }
    return render(request, 'single-product.html', context)