from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from account.tokens import account_activation_token
from django.utils.encoding import force_bytes

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
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'my-account.html', context)

@login_required(login_url='login')
def wishlist(request):
    return render(request, 'wishlist.html')


def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('login'))