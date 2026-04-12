"""
Django REST Framework serializers
"""
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Category, Product, ProductImage, Cart, CartItem, Order, OrderItem, Review


class UserSerializer(serializers.ModelSerializer):
    """User serializer for registration and profile"""
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password', 
                  'confirm_password', 'phone_whatsapp', 'year_group', 'bio', 'role', 
                  'id_image', 'is_verified', 'profile_complete', 'avg_rating', 'review_count']
        read_only_fields = ['id', 'is_verified', 'avg_rating', 'review_count']
    
    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Passwords do not match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """Simplified user profile for public display"""
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'name', 'first_name', 'last_name', 'email', 'phone_whatsapp', 
                  'year_group', 'bio', 'role', 'avg_rating', 'review_count']
    
    def get_name(self, obj):
        return obj.get_full_name()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_primary']



class ProductListSerializer(serializers.ModelSerializer):
    """Product list view with minimal data"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    seller_name = serializers.SerializerMethodField()
    primary_image = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'condition', 'location', 'category_name', 
                  'seller_name', 'primary_image', 'created_at']
    
    def get_seller_name(self, obj):
        return obj.seller.get_full_name()
    
    def get_primary_image(self, obj):
        img = obj.primary_image
        if img:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(img.image.url)
        return None


class ProductDetailSerializer(serializers.ModelSerializer):
    """Detailed product view"""
    category = CategorySerializer(read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    seller = UserProfileSerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'quantity', 'condition', 
                  'location', 'is_available', 'category', 'category_name', 'category_id', 'seller', 
                  'images', 'created_at', 'updated_at']
        read_only_fields = ['id', 'seller', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        validated_data['seller'] = self.context['request'].user
        return super().create(validated_data)


class CartItemSerializer(serializers.ModelSerializer):
    """Cart item with product details"""
    product = ProductListSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity', 'subtotal']


class CartSerializer(serializers.ModelSerializer):
    """Shopping cart with items"""
    items = CartItemSerializer(many=True, read_only=True)
    total_items = serializers.IntegerField(read_only=True)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_items', 'total_amount']


class OrderItemSerializer(serializers.ModelSerializer):
    """Order item details"""
    product = ProductListSerializer(read_only=True)
    seller = UserProfileSerializer(read_only=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'seller', 'quantity', 'unit_price', 'subtotal']


class OrderSerializer(serializers.ModelSerializer):
    """Order with items"""
    items = OrderItemSerializer(many=True, read_only=True)
    buyer = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'buyer', 'total_amount', 'status', 'items', 'created_at', 'updated_at']
        read_only_fields = ['id', 'buyer', 'total_amount', 'created_at', 'updated_at']


class ReviewSerializer(serializers.ModelSerializer):
    """Review serializer"""
    reviewer = UserProfileSerializer(read_only=True)
    seller = UserProfileSerializer(read_only=True)
    order_item_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'order_item_id', 'reviewer', 'seller', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'reviewer', 'seller', 'created_at']
    
    def validate_rating(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("Rating must be between 1 and 5")
        return value
    
    def create(self, validated_data):
        order_item_id = validated_data.pop('order_item_id')
        order_item = OrderItem.objects.get(id=order_item_id)
        
        # Validate reviewer is the buyer
        if order_item.order.buyer != self.context['request'].user:
            raise serializers.ValidationError("You can only review items you purchased")
        
        # Validate not reviewing own product
        if order_item.seller == self.context['request'].user:
            raise serializers.ValidationError("You cannot review your own products")
        
        validated_data['order_item'] = order_item
        validated_data['reviewer'] = self.context['request'].user
        validated_data['seller'] = order_item.seller
        
        return super().create(validated_data)
