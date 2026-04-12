"""
Django REST Framework views for API endpoints
"""
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, Category, Product, ProductImage, Cart, CartItem, Order, OrderItem, Review
from .serializers import (
    UserSerializer, UserProfileSerializer, CategorySerializer,
    ProductListSerializer, ProductDetailSerializer, ProductImageSerializer,
    CartSerializer, CartItemSerializer, OrderSerializer, ReviewSerializer
)


# Helper function to generate JWT tokens
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# CSRF Token View (kept for backward compatibility)
@api_view(['GET'])
@permission_classes([AllowAny])
def csrf_token_view(request):
    """Get CSRF token - not needed for JWT but kept for compatibility"""
    return Response({'detail': 'CSRF cookie set'})


# Authentication Views
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """User registration with JWT tokens"""
    print(f"Registration attempt with data: {request.data}")  # Debug
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            user = serializer.save()
            print(f"User created successfully: {user.email}")  # Debug
            tokens = get_tokens_for_user(user)
            print(f"Tokens generated for user: {user.email}")  # Debug
            return Response({
                'user': UserProfileSerializer(user).data,
                'tokens': tokens,
                'message': 'Registration successful'
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error creating user: {str(e)}")  # Debug
            return Response({
                'error': f'Registration failed: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    print(f"Validation errors: {serializer.errors}")  # Debug
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """User login with JWT tokens"""
    email = request.data.get('email', '').lower()
    password = request.data.get('password', '')
    
    user = authenticate(request, username=email, password=password)
    
    if user:
        tokens = get_tokens_for_user(user)
        return Response({
            'user': UserProfileSerializer(user).data,
            'tokens': tokens,
            'message': 'Login successful'
        })
    
    return Response({
        'error': 'Invalid credentials'
    }, status=status.HTTP_401_UNAUTHORIZED)
    
    print(f"Login attempt for: {email}")  # Debug
    
    user = authenticate(request, username=email, password=password)
    
    if user:
        login(request, user)
        print(f"Login successful for: {email}")  # Debug
        print(f"Session key: {request.session.session_key}")  # Debug
        
        # Force session save
        request.session.save()
        
        response = Response({
            'user': UserProfileSerializer(user).data,
            'message': 'Login successful'
        })
        
        # Explicitly set session cookie in response
        response.set_cookie(
            'sessionid',
            request.session.session_key,
            max_age=1209600,  # 2 weeks
            httponly=False,
            samesite=None,
            secure=False
        )
        
        print(f"Response cookies: {response.cookies}")  # Debug
        return response
    
    print(f"Login failed for: {email}")  # Debug
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """User logout - with JWT, client just deletes the token"""
    # For JWT, logout is handled client-side by deleting the token
    # But we can blacklist the refresh token if needed
    return Response({'message': 'Logout successful'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_view(request):
    """Get current user info"""
    return Response(UserProfileSerializer(request.user).data)



# Category ViewSet
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """List and retrieve categories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    pagination_class = None  # Disable pagination for categories


# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    """CRUD operations for products"""
    queryset = Product.objects.filter(is_available=True).select_related('category', 'seller')
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'condition', 'seller']
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductDetailSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def perform_create(self, serializer):
        print(f"Creating product for user: {self.request.user}")
        print(f"Request data: {self.request.data}")
        try:
            serializer.save(seller=self.request.user)
            print("Product created successfully")
        except Exception as e:
            print(f"Error creating product: {e}")
            raise
    
    def perform_update(self, serializer):
        # Only allow seller to update their own products
        if serializer.instance.seller != self.request.user:
            raise PermissionError("You can only edit your own products")
        serializer.save()
    
    def perform_destroy(self, instance):
        # Only allow seller to delete their own products
        if instance.seller != self.request.user:
            raise PermissionError("You can only delete your own products")
        instance.delete()
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def upload_image(self, request, pk=None):
        """Upload product image"""
        product = self.get_object()
        
        if product.seller != request.user:
            return Response({'error': 'Not authorized'}, status=status.HTTP_403_FORBIDDEN)
        
        if product.images.count() >= 5:
            return Response({'error': 'Maximum 5 images allowed'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Cart Views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@ensure_csrf_cookie
def cart_view(request):
    """Get user's cart"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    """Add item to cart"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))
    
    try:
        product = Product.objects.get(id=product_id, is_available=True)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Prevent buying own products
    if product.seller == request.user:
        return Response({'error': 'Cannot buy your own products'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Check stock
    if quantity > product.quantity:
        return Response({'error': 'Insufficient stock'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Add or update cart item
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )
    
    if not created:
        cart_item.quantity += quantity
        if cart_item.quantity > product.quantity:
            return Response({'error': 'Insufficient stock'}, status=status.HTTP_400_BAD_REQUEST)
        cart_item.save()
    
    return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_cart_item(request, item_id):
    """Update cart item quantity"""
    try:
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
    except CartItem.DoesNotExist:
        return Response({'error': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)
    
    quantity = int(request.data.get('quantity', 1))
    
    if quantity > cart_item.product.quantity:
        return Response({'error': 'Insufficient stock'}, status=status.HTTP_400_BAD_REQUEST)
    
    if quantity <= 0:
        cart_item.delete()
        return Response({'message': 'Item removed from cart'})
    
    cart_item.quantity = quantity
    cart_item.save()
    
    return Response(CartItemSerializer(cart_item).data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, item_id):
    """Remove item from cart"""
    try:
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
        cart_item.delete()
        return Response({'message': 'Item removed from cart'})
    except CartItem.DoesNotExist:
        return Response({'error': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)



# Order Views
class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    """View orders"""
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        # Show orders where user is buyer or seller
        return Order.objects.filter(
            Q(buyer=user) | Q(items__seller=user)
        ).distinct().prefetch_related('items__product', 'items__seller')
    
    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        """Update order status (seller only)"""
        order = self.get_object()
        new_status = request.data.get('status')
        
        if new_status not in ['confirmed', 'completed', 'cancelled']:
            return Response(
                {'error': 'Invalid status. Must be: confirmed, completed, or cancelled'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if user is a seller for any items in this order
        is_seller = order.items.filter(seller=request.user).exists()
        
        if not is_seller:
            return Response(
                {'error': 'Only sellers can update order status'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        order.status = new_status
        order.save()
        
        serializer = self.get_serializer(order)
        return Response(serializer.data)
    
    @action(detail=True, methods=['delete'])
    def remove_order(self, request, pk=None):
        """Remove/archive order (buyer or seller, completed/cancelled orders only)"""
        order = self.get_object()
        
        # Check if user is buyer or seller for this order
        is_buyer = order.buyer == request.user
        is_seller = order.items.filter(seller=request.user).exists()
        
        if not (is_buyer or is_seller):
            return Response(
                {'error': 'You do not have permission to remove this order'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Only allow removing completed or cancelled orders
        if order.status not in ['completed', 'cancelled']:
            return Response(
                {'error': 'Only completed or cancelled orders can be removed'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Delete the order
        order.delete()
        
        return Response(
            {'message': 'Order removed successfully'},
            status=status.HTTP_200_OK
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout(request):
    """Create order from cart"""
    cart = Cart.objects.get(user=request.user)
    
    if not cart.items.exists():
        return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Calculate total and validate stock
    total = 0
    order_items_data = []
    
    for cart_item in cart.items.all():
        product = cart_item.product
        
        # Check if product is still available
        if not product.is_available:
            return Response({
                'error': f'Product "{product.title}" is no longer available'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Check stock
        if cart_item.quantity > product.quantity:
            return Response({
                'error': f'Insufficient stock for "{product.title}"'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Prevent buying own products
        if product.seller == request.user:
            return Response({
                'error': f'Cannot buy your own product "{product.title}"'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        total += cart_item.subtotal
        order_items_data.append({
            'product': product,
            'seller': product.seller,
            'quantity': cart_item.quantity,
            'unit_price': product.price
        })
    
    # Create order
    order = Order.objects.create(
        buyer=request.user,
        total_amount=total,
        status='pending'
    )
    
    # Create order items and update stock
    for item_data in order_items_data:
        OrderItem.objects.create(order=order, **item_data)
        
        # Reduce product quantity
        product = item_data['product']
        product.quantity -= item_data['quantity']
        if product.quantity == 0:
            product.is_available = False
        product.save()
    
    # Clear cart
    cart.items.all().delete()
    
    return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


# Review Views
class ReviewViewSet(viewsets.ModelViewSet):
    """CRUD for reviews"""
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Review.objects.all()
        seller_id = self.request.query_params.get('seller_id')
        if seller_id:
            queryset = queryset.filter(seller_id=seller_id)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save()


# User Profile View
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    """Get or update user profile"""
    if request.method == 'GET':
        return Response(UserProfileSerializer(request.user).data)
    
    elif request.method == 'PUT':
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def user_profile_public(request, user_id):
    """Get public user profile"""
    try:
        user = User.objects.get(id=user_id)
        return Response(UserProfileSerializer(user).data)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
