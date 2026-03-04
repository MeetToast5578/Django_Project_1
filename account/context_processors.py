from product.models import WishList


def wishlist_context(request):
    """Add wishlist to context for all templates"""
    wishlist = None
    if request.user.is_authenticated:
        wishlist = WishList.objects.filter(user=request.user).first()
    else:
        wishlist = None
    
    return {
        'wishlist': wishlist
    }
