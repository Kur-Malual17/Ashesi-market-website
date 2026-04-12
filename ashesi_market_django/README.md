# Ashesi Market — Django Backend

A campus e-commerce web app for Ashesi University students to buy and sell.

**Converted from PHP to Django** - Complete backend rewrite with REST API, admin panel, and enhanced security.

---

## 🚀 Quick Start

```bash
# Run automated setup
./setup.sh        # Linux/Mac
setup.bat         # Windows

# Or manual setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your database credentials
python manage.py migrate
python manage.py loaddata categories
python manage.py createsuperuser
python manage.py runserver
```

Visit: **http://localhost:8000**

📚 **New to Django?** See [QUICKSTART.md](QUICKSTART.md) for detailed setup instructions.

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| [QUICKSTART.md](QUICKSTART.md) | Get started in 5 minutes |
| [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) | PHP to Django migration details |
| [PHP_TO_PYTHON_REFERENCE.md](PHP_TO_PYTHON_REFERENCE.md) | Code conversion examples |
| [FILE_MAPPING.md](FILE_MAPPING.md) | PHP files → Django files mapping |
| [DEPLOYMENT.md](DEPLOYMENT.md) | Production deployment guide |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | Complete project overview |

---

## ✨ Features

### Core Functionality
- ✅ User registration and authentication
- ✅ Product listing and management
- ✅ Shopping cart
- ✅ Order processing
- ✅ Review and rating system
- ✅ Image uploads (multiple per product)
- ✅ WhatsApp integration for buyer-seller contact
- ✅ Category-based browsing
- ✅ Search and filtering

### New in Django Version
- 🆕 **REST API** - Full API for mobile/frontend apps
- 🆕 **Admin Panel** - Built-in admin interface
- 🆕 **Better Security** - Django's security features
- 🆕 **ORM** - No more raw SQL queries
- 🆕 **Migrations** - Database version control
- 🆕 **Unit Tests** - Testable codebase
- 🆕 **Signals** - Automatic operations

---

## 🏗️ Tech Stack

- **Backend:** Django 4.2+ with Django REST Framework
- **Database:** MySQL 8.0+
- **Authentication:** Django Auth System
- **API:** Django REST Framework
- **File Uploads:** Pillow (PIL)
- **Environment:** python-decouple
- **CORS:** django-cors-headers

---

## 📁 Project Structure

```
ashesi_market_django/
├── ashesi_market/              # Django project settings
│   ├── settings.py             # Configuration
│   ├── urls.py                 # Main URL routing
│   └── wsgi.py                 # WSGI application
│
├── marketplace/                # Main Django app
│   ├── models.py               # Database models (9 models)
│   ├── views.py                # API views (REST)
│   ├── web_views.py            # Template views (HTML)
│   ├── serializers.py          # DRF serializers
│   ├── forms.py                # Django forms
│   ├── admin.py                # Admin interface
│   ├── signals.py              # Auto-operations
│   ├── utils.py                # Helper functions
│   ├── urls.py                 # API routing
│   ├── web_urls.py             # Web routing
│   ├── tests.py                # Unit tests
│   └── fixtures/               # Initial data
│
├── media/                      # User uploads
│   ├── products/               # Product images
│   └── id_images/              # ID verification
│
├── static/                     # Static files
│   ├── css/                    # Stylesheets
│   └── js/                     # JavaScript
│
├── requirements.txt            # Python dependencies
├── .env.example                # Environment template
├── manage.py                   # Django CLI
├── setup.sh                    # Linux/Mac setup
└── setup.bat                   # Windows setup
```

---

## 🔌 API Endpoints

### Authentication
```
POST   /api/auth/register/      Register new user
POST   /api/auth/login/         User login
POST   /api/auth/logout/        User logout
GET    /api/auth/user/          Current user info
```

### Products
```
GET    /api/products/           List products (with filters)
POST   /api/products/           Create product
GET    /api/products/{id}/      Product detail
PUT    /api/products/{id}/      Update product
DELETE /api/products/{id}/      Delete product
POST   /api/products/{id}/upload_image/  Upload image
```

### Cart
```
GET    /api/cart/               View cart
POST   /api/cart/add/           Add to cart
PUT    /api/cart/update/{id}/   Update quantity
DELETE /api/cart/remove/{id}/   Remove item
```

### Orders
```
GET    /api/orders/             List orders
POST   /api/checkout/           Create order from cart
GET    /api/orders/{id}/        Order detail
```

### Reviews
```
POST   /api/reviews/            Submit review
GET    /api/reviews/?seller_id={id}  Seller reviews
```

### Categories
```
GET    /api/categories/         List categories
```

---

## 🌐 Web Interface

Traditional web pages (HTML templates):

```
GET    /                        Homepage
GET    /products/               Browse products
GET    /products/{id}/          Product detail
GET    /products/new/           Create product
GET    /cart/                   Shopping cart
GET    /profile/                User profile
GET    /register/               User registration
GET    /login/                  User login
```

---

## 🛡️ Security Features

- ✅ Django's built-in CSRF protection
- ✅ Password hashing with PBKDF2 (more secure than bcrypt)
- ✅ SQL injection prevention via ORM
- ✅ XSS protection (auto-escaping templates)
- ✅ File upload validation (type, size)
- ✅ Session security
- ✅ Clickjacking protection
- ✅ Secure password validators
- ✅ HTTPS enforcement (production)

---

## 👨‍💼 Admin Panel

Access at: **http://localhost:8000/admin**

Features:
- User management
- Product moderation
- Order tracking
- Review management
- Category management
- Statistics and reports
- Search and filtering
- Bulk operations

---

## 🧪 Testing

Run tests:
```bash
python manage.py test
```

Run with coverage:
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📊 Database Models

| Model | Description |
|-------|-------------|
| `User` | Custom user with profile fields |
| `Category` | Product categories |
| `Product` | Product listings |
| `ProductImage` | Multiple images per product |
| `Cart` | Shopping cart (one per user) |
| `CartItem` | Items in cart |
| `Order` | Order header |
| `OrderItem` | Order line items |
| `Review` | Product/seller reviews |

---

## 🔄 Migration from PHP

This project is a complete conversion of the PHP version:

| Aspect | PHP Version | Django Version |
|--------|-------------|----------------|
| Framework | PHP 8+ | Django 4.2+ |
| Database | MySQLi | Django ORM |
| Auth | Custom sessions | Django Auth |
| Security | Manual CSRF | Built-in |
| API | None | REST API |
| Admin | None | Full admin panel |
| Tests | None | Unit tests |

See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for detailed conversion information.

---

## 🚀 Deployment

The application is production-ready. Deploy to:
- Traditional servers (Ubuntu + Nginx + Gunicorn)
- Docker containers
- Platform as a Service (Heroku, Railway, etc.)
- Cloud platforms (AWS, Google Cloud, Azure)

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

---

## 📝 Common Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver

# Django shell
python manage.py shell

# Run tests
python manage.py test

# Load initial data
python manage.py loaddata categories
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

---

## 📄 License

Same as original PHP project.

---

## 🆘 Support

- **Issues?** Check [QUICKSTART.md](QUICKSTART.md) for troubleshooting
- **Migration questions?** See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)
- **Code conversion?** See [PHP_TO_PYTHON_REFERENCE.md](PHP_TO_PYTHON_REFERENCE.md)
- **Deployment help?** See [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Best Practices](https://django-best-practices.readthedocs.io/)

---

**Built with ❤️ for Ashesi University students**
