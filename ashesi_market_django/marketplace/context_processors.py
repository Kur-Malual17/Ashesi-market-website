"""
Context processors for templates
"""
from django.conf import settings
from .models import Cart


def app_settings(request):
    """Add app settings to template context"""
    return {
        'APP_NAME': settings.APP_NAME,
        'BASE_URL': settings.BASE_URL,
    }


def cart_count(request):
    """Add cart item count to template context"""
    count = 0
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            count = cart.total_items
        except Cart.DoesNotExist:
            pass
    
    return {'cart_count': count}
