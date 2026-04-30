"""
URL configuration for ashesi_market project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.views.generic import RedirectView

def api_root(request):
    """API root endpoint"""
    return JsonResponse({
        'message': 'Ashesi Market API',
        'version': '1.0',
        'status': 'running',
        'frontend': 'https://ashesi-market-website.vercel.app',
        'admin': '/admin/',
        'documentation': {
            'postman_collection': 'See README.md for Postman testing guide',
            'endpoints': 'See /api/ for available endpoints'
        },
        'api_endpoints': {
            'auth': {
                'register': '/api/auth/register/',
                'login': '/api/auth/login/',
                'current_user': '/api/auth/user/',
                'token_refresh': '/api/auth/token/refresh/',
            },
            'products': {
                'list': '/api/products/',
                'detail': '/api/products/{id}/',
                'create': '/api/products/ (POST)',
                'update': '/api/products/{id}/ (PUT)',
                'delete': '/api/products/{id}/ (DELETE)',
            },
            'categories': '/api/categories/',
            'cart': {
                'view': '/api/cart/',
                'add': '/api/cart/add/',
                'remove': '/api/cart/remove/{id}/',
            },
            'orders': {
                'list': '/api/orders/',
                'checkout': '/api/checkout/',
                'detail': '/api/orders/{id}/',
                'update_status': '/api/orders/{id}/update_status/',
            },
            'reviews': {
                'list': '/api/reviews/',
                'create': '/api/reviews/',
                'by_product': '/api/reviews/?product_id={id}',
            },
        }
    })

urlpatterns = [
    path('', api_root, name='api-root'),  # Root shows API info
    path('admin/', admin.site.urls),
    path('api/', include('marketplace.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin site customization
admin.site.site_header = 'Ashesi Market Admin'
admin.site.site_title = 'Ashesi Market'
admin.site.index_title = 'Welcome to Ashesi Market Administration'
