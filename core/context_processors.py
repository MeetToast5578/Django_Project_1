from order.models import Basket


def basket_context(request):
    """Add basket to context for all templates"""
    basket = None
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user, is_active=True).first()
    else:
        basket = None
    
    return {
        'basket': basket
    }
