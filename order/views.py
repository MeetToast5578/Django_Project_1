from django.shortcuts import render
from order.models import Basket, BasketItem
from product.models import Product
from django.http import JsonResponse
import json
from product.models import WishList, WishListItem

# Create your views here.


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(productId)
    print(action)

    product = Product.objects.get(id = productId)

    basket, created = Basket.objects.get_or_create(user = request.user, is_active = True)
    basketItem, created = BasketItem.objects.get_or_create(basket = basket, product = product)
    # wishListItem, created = WishListItem.objects.get_or_create(wishlist__user=request.user, product=product)

    if action == 'add':
        if created:
            basketItem.quantity = 1
        else:
            basketItem.quantity += 1
    
    if action == 'add-full':
        product_quantity = WishListItem.objects.filter(wishlist__user=request.user, product=product).first().quantity
        
        if created:
            basketItem.quantity = product_quantity
        else:
            basketItem.quantity += product_quantity
            
        # wishListItem.delete()

    if action == 'remove' and basketItem.quantity > 1:
        basketItem.quantity -= 1

    basketItem.save()

    if action == 'delete':
        basketItem.delete()

    return JsonResponse('Item was updated!', safe=False)


def cart(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user = request.user, is_active = True).first()
    else:
        basket = None
    context = {
        'basket' : basket
    }
    return render(request, 'cart.html', context)

def checkout(request):
    return render(request, 'checkout.html')

def empty_cart(request):
    return render(request, 'empty-cart.html')