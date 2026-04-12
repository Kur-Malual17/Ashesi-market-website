"""
Django template-based views for web interface
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, User, Cart, Order, Review
from .forms import UserRegistrationForm, LoginForm, ProductForm, ProfileForm


def home_view(request):
    """Homepage with latest products"""
    products = Product.objects.filter(is_available=True).select_related(
        'category', 'seller'
    ).prefetch_related('images')[:20]
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'marketplace/home.html', context)


def product_list_view(request):
    """Browse/search products"""
    products = Product.objects.filter(is_available=True).select_related('category', 'seller')
    
    # Filters
    category_id = request.GET.get('category')
    condition = request.GET.get('condition')
    search = request.GET.get('q')
    
    if category_id:
        products = products.filter(category_id=category_id)
    if condition:
        products = products.filter(condition=condition)
    if search:
        products = products.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': category_id,
        'selected_condition': condition,
        'search_query': search,
    }
    return render(request, 'marketplace/product_list.html', context)


def product_detail_view(request, pk):
    """Product detail page"""
    product = get_object_or_404(
        Product.objects.select_related('seller', 'category').prefetch_related('images'),
        pk=pk
    )
    
    context = {
        'product': product,
    }
    return render(request, 'marketplace/product_detail.html', context)


@login_required
def product_create_view(request):
    """Create new product"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            messages.success(request, 'Product listed successfully!')
            return redirect('product-detail', pk=product.pk)
    else:
        form = ProductForm()
    
    return render(request, 'marketplace/product_form.html', {'form': form})


def register_view_web(request):
    """User registration"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'marketplace/register.html', {'form': form})


def login_view_web(request):
    """User login"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            
            if user:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect(request.GET.get('next', 'home'))
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()
    
    return render(request, 'marketplace/login.html', {'form': form})


@login_required
def logout_view_web(request):
    """User logout"""
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')


@login_required
def cart_view_web(request):
    """Shopping cart"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    context = {
        'cart': cart,
    }
    return render(request, 'marketplace/cart.html', context)


@login_required
def profile_view_web(request):
    """User profile"""
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    
    # Get user's products and orders
    products = Product.objects.filter(seller=request.user)
    orders = Order.objects.filter(buyer=request.user)
    
    context = {
        'form': form,
        'products': products,
        'orders': orders,
    }
    return render(request, 'marketplace/profile.html', context)
