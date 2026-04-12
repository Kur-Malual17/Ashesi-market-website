# Migration Guide: PHP to Django

This guide explains the conversion from the PHP version to Django.

## Architecture Changes

### Backend Framework
- **PHP** → **Django (Python)**
- **MySQLi** → **Django ORM**
- **Manual SQL** → **Model-based queries**

### Authentication
- **PHP Sessions + password_hash()** → **Django Auth System**
- **Manual CSRF tokens** → **Django CSRF middleware**
- **Custom session handling** → **Django session framework**

### File Structure

#### PHP Structure
```
ashesi_market/
├── config/          → Database & app config
├── includes/        → Shared functions & partials
├── pages/           → Individual page scripts
└── assets/          → Static files & uploads
```

#### Django Structure
```
ashesi_market_django/
├── ashesi_market/   → Project settings
├── marketplace/     → Main app
│   ├── models.py    → Database models (ORM)
│   ├── views.py     → API views (DRF)
│   ├── web_views.py → Template views
│   ├── serializers.py → API serializers
│   ├── forms.py     → Django forms
│   └── templates/   → HTML templates
├── media/           → User uploads
└── static/          → Static files
```

## Code Conversion Examples

### 1. Database Queries

**PHP (MySQLi):**
```php
$stmt = $conn->prepare('SELECT * FROM products WHERE id = ?');
$stmt->bind_param('i', $id);
$stmt->execute();
$product = $stmt->get_result()->fetch_assoc();
```

**Django (ORM):**
```python
product = Product.objects.get(id=id)
```

### 2. User Authentication

**PHP:**
```php
if (password_verify($password, $user['password_hash'])) {
    $_SESSION['user_id'] = $user['id'];
    session_regenerate_id(true);
}
```

**Django:**
```python
user = authenticate(username=email, password=password)
if user:
    login(request, user)
```

### 3. Form Handling

**PHP:**
```php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    verify_csrf();
    $title = trim($_POST['title'] ?? '');
    // Validation...
}
```

**Django:**
```python
if request.method == 'POST':
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save()
```

### 4. File Uploads

**PHP:**
```php
$ext = pathinfo($file['name'], PATHINFO_EXTENSION);
$name = bin2hex(random_bytes(12)) . '.' . $ext;
move_uploaded_file($file['tmp_name'], UPLOAD_DIR . $name);
```

**Django:**
```python
# Handled automatically by ImageField
class Product(models.Model):
    image = models.ImageField(upload_to='products/')
```

## Database Schema Mapping

| PHP Table | Django Model | Changes |
|-----------|--------------|---------|
| `users` | `User` | Extends AbstractUser, email as username |
| `categories` | `Category` | Same structure |
| `products` | `Product` | Added updated_at field |
| `product_images` | `ProductImage` | Same structure |
| `cart` | `Cart` | Same structure |
| `cart_items` | `CartItem` | Same structure |
| `orders` | `Order` | Added updated_at field |
| `order_items` | `OrderItem` | Same structure |
| `reviews` | `Review` | Same structure |

## API Endpoints

Django provides both REST API and web interface:

### REST API (JSON)
- `POST /api/auth/register/` - Register
- `POST /api/auth/login/` - Login
- `GET /api/products/` - List products
- `POST /api/products/` - Create product
- `GET /api/cart/` - View cart
- `POST /api/checkout/` - Create order

### Web Interface (HTML)
- `GET /` - Homepage
- `GET /products/` - Browse products
- `GET /products/<id>/` - Product detail
- `GET /cart/` - Shopping cart
- `GET /profile/` - User profile

## Security Improvements

1. **SQL Injection**: Django ORM prevents SQL injection by default
2. **XSS**: Django templates auto-escape HTML
3. **CSRF**: Built-in CSRF protection
4. **Password Hashing**: PBKDF2 with salt (more secure than bcrypt)
5. **Session Security**: Secure session handling
6. **File Uploads**: Automatic validation and sanitization

## Features Added

1. **Admin Panel**: Full-featured admin interface at `/admin`
2. **REST API**: Complete API for mobile/frontend apps
3. **Better ORM**: Relationships, migrations, query optimization
4. **Signals**: Automatic cart creation, rating updates
5. **Fixtures**: Easy data seeding
6. **Management Commands**: Custom admin commands

## Migration Steps

1. **Setup Django project** (already done)
2. **Run migrations**: `python manage.py migrate`
3. **Load categories**: `python manage.py loaddata categories`
4. **Copy media files**: Move `assets/uploads/` to `media/`
5. **Migrate users**: Users need to re-register (passwords incompatible)
6. **Test thoroughly**: Verify all features work

## Running Both Systems

You can run both PHP and Django versions simultaneously:

- **PHP**: `http://localhost/ashesi_market`
- **Django**: `http://localhost:8000`

This allows gradual migration and testing.

## Next Steps

1. Copy CSS/JS from `assets/` to `static/`
2. Create Django templates matching PHP pages
3. Test all functionality
4. Deploy to production server
5. Update DNS/URLs to point to Django

## Support

For issues or questions about the migration, refer to:
- Django documentation: https://docs.djangoproject.com
- Django REST Framework: https://www.django-rest-framework.org
