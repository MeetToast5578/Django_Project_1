from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.forms import RegisterForm, LoginForm, ProfileForm, AddressForm
from account.models import Address
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from account.tokens import account_activation_token
from django.utils.encoding import force_bytes


from product.models import Product, WishList, WishListItem
from order.models import Basket
from django.http import JsonResponse
import json

from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.http import urlsafe_base64_decode
# Create your views here.

def login(request):
    form1 = RegisterForm()
    form2 = LoginForm()
    
    if request.method == 'POST':
        if 'register' in request.POST:
            form1 = RegisterForm(data = request.POST, files=request.FILES)
            if form1.is_valid():
                user = form1.save(commit=False)
                user.set_password(form1.cleaned_data['password'])
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                subject = 'Activate Your MySite Account'
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                user.email_user(subject, message)
        elif 'login' in request.POST:
            next = request.GET.get('next', reverse_lazy('home'))
            form2 = LoginForm(data = request.POST)
            print(request.POST)
            
            print('post')
            if form2.is_valid():
                print('valid')
                user = authenticate(request, username = form2.cleaned_data['username'], password = form2.cleaned_data['password'])
                django_login(request, user)
                if not user:
                    pass
                else:
                    return redirect(next)
            
    context = {
        'form': form1,
        'form2': form2
    } 
    return render(request, 'login.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        django_login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')
    
    
@login_required(login_url='login')
def my_account(request):
    # Ensure user has an address object
    address, _ = Address.objects.get_or_create(user=request.user)

    form = ProfileForm(instance=request.user)
    address_form = AddressForm(instance=address)

    # Wishlist preview
    wishlist = WishList.objects.filter(user=request.user).prefetch_related('items__product').first()
    recent_wishlist_items = []
    if wishlist:
        recent_wishlist_items = wishlist.items.select_related('product').order_by('-created_at')[:4]

    # Active basket summary
    basket = Basket.objects.filter(user=request.user, is_active=True).prefetch_related('items__product').first()

    if request.method == 'POST':
        # Determine which form was submitted
        if 'profile_submit' in request.POST:
            form = ProfileForm(request.POST, request.FILES, instance=request.user)
            address_form = AddressForm(instance=address)
            if form.is_valid():
                form.save()
        elif 'address_submit' in request.POST:
            form = ProfileForm(instance=request.user)
            address_form = AddressForm(request.POST, instance=address)
            if address_form.is_valid():
                address_form.save()

    # Profile completion progress
    user = request.user
    profile_fields = {
        'First name': bool(user.first_name),
        'Last name': bool(user.last_name),
        'Email': bool(user.email),
        'Phone': bool(user.phone),
        'Profile image': bool(user.profile_image),
        'Street address': bool(address.street),
        'City': bool(address.city),
        'State': bool(address.state),
        'ZIP': bool(address.zip_code),
        'Country': bool(address.country),
    }
    total_fields = len(profile_fields)
    completed_fields = sum(1 for v in profile_fields.values() if v)
    profile_completion = int((completed_fields / total_fields) * 100) if total_fields else 0
    missing_profile_fields = [name for name, ok in profile_fields.items() if not ok]
    context = {
        'form': form,
        'address_form': address_form,
        'address': address,
        'wishlist': wishlist,
        'recent_wishlist_items': recent_wishlist_items,
        'basket': basket,
        'profile_completion': profile_completion,
        'missing_profile_fields': missing_profile_fields,
    }
    return render(request, 'my-account.html', context)



def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(productId)
    print(action)

    product = Product.objects.get(id = productId)

    wishlist, created = WishList.objects.get_or_create(user = request.user)
    print(wishlist)
    wishlistItem, created = WishListItem.objects.get_or_create(wishlist = wishlist, product = product)

    if action == 'add':
        if created:
            wishlistItem.quantity = 1
        else:
            wishlistItem.quantity += 1

    if action == 'remove' and wishlistItem.quantity > 1:
        wishlistItem.quantity -= 1

    wishlistItem.save()

    if action == 'delete':
        wishlistItem.delete()

    return JsonResponse('Item was updated!', safe=False)

@login_required(login_url='login')
def wishlist(request):
    if request.user.is_authenticated:
        wishlist = WishList.objects.filter(user = request.user).first()
    else:
        wishlist = None
    context = {
        'wishlist' : wishlist
    }
    return render(request, 'wishlist.html', context)


def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('login'))