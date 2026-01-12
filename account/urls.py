from django.urls import path, re_path
from .views import login, my_account, wishlist, activate

urlpatterns = [
    path('login/', login, name='login'),
    path('my-account/', my_account, name='my_account'),
    path('wishlist/', wishlist, name='wishlist'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        activate, name='activate'),
]