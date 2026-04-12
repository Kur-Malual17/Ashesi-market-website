"""
Web interface URL routing
"""
from django.urls import path
from . import web_views

urlpatterns = [
    path('', web_views.home_view, name='home'),
    path('products/', web_views.product_list_view, name='product-list'),
    path('products/<int:pk>/', web_views.product_detail_view, name='product-detail'),
    path('products/new/', web_views.product_create_view, name='product-create'),
    
    path('register/', web_views.register_view_web, name='register-web'),
    path('login/', web_views.login_view_web, name='login-web'),
    path('logout/', web_views.logout_view_web, name='logout-web'),
    
    path('cart/', web_views.cart_view_web, name='cart-web'),
    path('profile/', web_views.profile_view_web, name='profile-web'),
]
