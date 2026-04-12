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
        'frontend': 'http://localhost:8080',
        'admin': '/admin/',
        'api_endpoints': {
            'auth': '/api/auth/',
            'products': '/api/products/',
            'categories': '/api/categories/',
            'cart': '/api/cart/',
            'orders': '/api/orders/',
            'reviews': '/api/reviews/',
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
