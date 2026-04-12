"""
Tests for Ashesi Market
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Category, Product, Cart, Order, Review

User = get_user_model()


class UserModelTest(TestCase):
    """Test User model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@ashesi.edu.gh',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
    
    def test_user_creation(self):
        """Test user is created correctly"""
        self.assertEqual(self.user.email, 'test@ashesi.edu.gh')
        self.assertTrue(self.user.check_password('testpass123'))
    
    def test_cart_auto_creation(self):
        """Test cart is automatically created for new user"""
        self.assertTrue(hasattr(self.user, 'cart'))


class ProductModelTest(TestCase):
    """Test Product model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='seller',
            email='seller@ashesi.edu.gh',
            password='pass123'
        )
        self.category = Category.objects.create(name='Electronics', slug='electronics')
        self.product = Product.objects.create(
            seller=self.user,
            category=self.category,
            title='Test Product',
            description='Test description',
            price=100.00,
            quantity=5
        )
    
    def test_product_creation(self):
        """Test product is created correctly"""
        self.assertEqual(self.product.title, 'Test Product')
        self.assertEqual(self.product.price, 100.00)
        self.assertTrue(self.product.is_available)


class APITest(TestCase):
    """Test API endpoints"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='apiuser',
            email='api@ashesi.edu.gh',
            password='apipass123'
        )
        self.category = Category.objects.create(name='Books', slug='books')
    
    def test_register_endpoint(self):
        """Test user registration"""
        response = self.client.post('/api/auth/register/', {
            'email': 'newuser@ashesi.edu.gh',
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'password': 'newpass123',
            'confirm_password': 'newpass123'
        })
        self.assertEqual(response.status_code, 201)
    
    def test_login_endpoint(self):
        """Test user login"""
        response = self.client.post('/api/auth/login/', {
            'email': 'api@ashesi.edu.gh',
            'password': 'apipass123'
        })
        self.assertEqual(response.status_code, 200)
    
    def test_product_list(self):
        """Test product listing"""
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)
