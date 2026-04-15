# Ashesi Market

A modern, full-featured online marketplace platform built specifically for the Ashesi University community. Students can buy and sell products, leave reviews, and connect with each other through a secure and user-friendly interface.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [User Roles](#user-roles)
- [Key Workflows](#key-workflows)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Ashesi Market is a student-to-student marketplace that enables the Ashesi University community to:
- List products for sale
- Browse and purchase items from fellow students
- Leave reviews on products and sellers
- Manage orders and track sales
- Communicate via WhatsApp integration

The platform consists of a Django REST API backend and a vanilla JavaScript frontend, deployed separately for scalability and flexibility.

---

## Features

### For Buyers
- **Browse Products**: Search and filter products by category, condition, and price
- **Product Reviews**: Read reviews from verified buyers before purchasing
- **Shopping Cart**: Add multiple items and checkout seamlessly
- **Order Management**: Track purchases and order status
- **Cancel Orders**: Cancel pending orders before seller approval
- **Leave Reviews**: Rate and review products after purchase
- **Seller Profiles**: View seller information and their other listings

### For Sellers
- **List Products**: Create product listings with images, descriptions, and pricing
- **Edit/Delete Products**: Full control over product listings
- **Order Management**: Approve, confirm, or cancel orders
- **Sales Dashboard**: Track earnings and order status
- **Review Insights**: See product reviews to identify popular items
- **WhatsApp Integration**: Contact buyers directly through WhatsApp

### Platform Features
- **JWT Authentication**: Secure token-based authentication
- **Image Storage**: Cloudflare R2 integration for fast, reliable image hosting
- **Responsive Design**: Mobile-friendly interface with hamburger menu
- **Real-time Updates**: Dynamic UI updates without page reloads
- **Role-based Access**: Buyer, Seller, or Both roles with appropriate permissions
- **Review System**: Product-specific reviews tied to verified purchases

---

## Technology Stack

### Backend
- **Framework**: Django 4.2+ with Django REST Framework
- **Database**: PostgreSQL (Railway) / SQLite (local development)
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Image Storage**: Cloudflare R2 (S3-compatible)
- **Server**: Gunicorn
- **Deployment**: Railway

### Frontend
- **Languages**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with responsive design
- **API Communication**: Fetch API with JWT tokens
- **Deployment**: Vercel

### Additional Tools
- **CORS**: django-cors-headers for cross-origin requests
- **Image Processing**: Pillow for image handling
- **Environment Variables**: python-decouple for configuration

---

## Project Structure

```
ashesi-market/
├── ashesi_market_django/          # Backend (Django)
│   ├── ashesi_market/             # Project settings
│   │   ├── settings.py            # Configuration
│   │   ├── urls.py                # URL routing
│   │   └── wsgi.py                # WSGI application
│   ├── marketplace/               # Main app
│   │   ├── models.py              # Database models
│   │   ├── views.py               # API endpoints
│   │   ├── serializers.py         # Data serialization
│   │   ├── urls.py                # App URLs
│   │   ├── admin.py               # Admin interface
│   │   └── migrations/            # Database migrations
│   ├── media/                     # Local media files (dev)
│   ├── static/                    # Static files
│   ├── requirements.txt           # Python dependencies
│   ├── Procfile                   # Railway deployment
│   └── manage.py                  # Django management
│
├── ashesi_market_frontend/        # Frontend (Vanilla JS)
│   ├── css/
│   │   └── style.css              # Main stylesheet
│   ├── js/
│   │   ├── config.js              # API configuration
│   │   ├── auth.js                # Authentication logic
│   │   ├── api.js                 # API helper functions
│   │   └── mobile-menu.js         # Mobile navigation
│   ├── index.html                 # Homepage
│   ├── login.html                 # Login page
│   ├── register.html              # Registration page
│   ├── products.html              # Product listing
│   ├── product.html               # Product detail
│   ├── sell.html                  # Create product
│   ├── edit-product.html          # Edit product
│   ├── cart.html                  # Shopping cart
│   ├── orders.html                # Order management
│   ├── profile.html               # User profile
│   └── profile-edit.html          # Edit profile
│
└── README.md                      # This file
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js (for local development server)
- PostgreSQL (for production) or SQLite (for development)
- Git

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ashesi-market/ashesi_market_django
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in `ashesi_market_django/`:
   

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Load initial data (optional)**
   ```bash
   python manage.py loaddata marketplace/fixtures/categories.json
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

   Backend will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd ashesi_market_frontend
   ```

2. **Update API configuration**
   
   Edit `js/config.js`:
   ```javascript
   const API_BASE_URL = 'http://localhost:8000/api';
   ```

3. **Start local server**
   
   Using Python:
   ```bash
   python -m http.server 5500
   ```
   
   Or using Node.js:
   ```bash
   npx http-server -p 5500
   ```

   Frontend will be available at `http://localhost:5500`

---

## Configuration

### Backend Configuration

Key settings in `ashesi_market/settings.py`:

- **ALLOWED_HOSTS**: Add your domain names
- **CORS_ALLOWED_ORIGINS**: Add frontend URLs
- **CSRF_TRUSTED_ORIGINS**: Add frontend URLs
- **DATABASE_URL**: PostgreSQL connection string
- **R2 Settings**: Cloudflare R2 credentials

### Frontend Configuration

Update `js/config.js`:

```javascript
const API_BASE_URL = 'https://your-backend-url.railway.app/api';
```

---

## Deployment

### Backend Deployment (Railway)

1. **Create Railway project**
   - Connect GitHub repository
   - Add PostgreSQL database


3. **Deploy**
   - Railway auto-deploys on git push
   - Run migrations via Railway CLI or admin panel

### Frontend Deployment (Vercel)

1. **Create Vercel project**
   - Import from GitHub
   - Set root directory to `ashesi_market_frontend`

2. **Configure build settings**
   - Framework Preset: Other
   - Build Command: (leave empty)
   - Output Directory: (leave empty)

3. **Set environment variables**
   ```
   API_BASE_URL=https://your-backend.railway.app/api
   ```

4. **Deploy**
   - Vercel auto-deploys on git push

---

## User Roles

### Buyer
- Browse and search products
- Add items to cart
- Place orders
- Leave reviews on purchased items
- View order history

### Seller
- List products for sale
- Edit/delete listings
- Manage orders (approve, confirm, complete)
- View sales dashboard
- See product reviews

### Both
- All buyer and seller capabilities
- Switch between buying and selling seamlessly

---

## Key Workflows

### Product Purchase Flow

1. **Browse Products**
   - User visits homepage or products page
   - Filters by category, condition, or search

2. **View Product Details**
   - Click on product to see full details
   - Read product reviews
   - View seller profile

3. **Add to Cart**
   - Select quantity
   - Click "Add to Cart"

4. **Checkout**
   - Review cart items
   - Click "Checkout"
   - Order created with status "pending"

5. **Order Processing**
   - Seller receives order notification
   - Seller approves order (status: "confirmed")
   - Seller marks as completed (status: "completed")

6. **Review**
   - Buyer leaves review and rating
   - Review appears on product page

### Product Listing Flow

1. **Create Listing**
   - Seller clicks "+ Sell"
   - Fills in product details
   - Uploads images (up to 5)
   - Submits listing

2. **Manage Listing**
   - View on profile page
   - Edit details or images
   - Delete if no longer available

3. **Receive Orders**
   - View in "My Sales" tab
   - Approve or reject orders
   - Contact buyer via WhatsApp

4. **Complete Sale**
   - Mark order as completed
   - View buyer's review
   - Track earnings

---

## API Documentation

### Authentication Endpoints




## Database Schema

### Key Models

**User**
- Custom user model extending Django's AbstractUser
- Fields: email, name, phone, year_group, bio, role, avg_rating
- Roles: buyer, seller, both

**Product**
- Fields: title, description, price, quantity, condition, location
- Relations: seller (User), category (Category)
- Properties: avg_rating, review_count

**Order**
- Fields: buyer, total_amount, status, created_at
- Status: pending, confirmed, completed, cancelled
- Relations: items (OrderItem)

**OrderItem**
- Fields: product, seller, quantity, unit_price
- Relations: order (Order), review (Review)

**Review**
- Fields: rating (1-5), comment, created_at
- Relations: order_item, reviewer, seller
- One review per order item (verified purchases only)

---

## Security Features

- JWT token authentication
- Password hashing with Django's built-in system
- CSRF protection for admin panel
- CORS configuration for cross-origin requests
- Permission-based access control
- Verified purchase reviews only
- Secure file upload validation

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Coding Standards

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Write docstrings for functions and classes
- Test thoroughly before submitting PR

---

## Troubleshooting

### Common Issues

**Backend won't start**
- Check Python version (3.8+)
- Verify all dependencies installed
- Check DATABASE_URL is correct
- Run migrations: `python manage.py migrate`

**Frontend can't connect to backend**
- Verify API_BASE_URL in config.js
- Check CORS settings in Django
- Ensure backend is running
- Check browser console for errors

**Images not uploading**
- Verify R2 credentials in environment variables
- Check R2 bucket permissions
- Ensure CORS policy configured on R2
- Check file size limits (3MB max)

**Authentication errors**
- Clear localStorage and try logging in again
- Check JWT token expiration (60 minutes)
- Verify credentials are correct

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Acknowledgments

- Built for the Ashesi University community
- Inspired by modern e-commerce platforms
- Uses open-source technologies and frameworks

---

## Contact

For questions, issues, or contributions, please open an issue on GitHub or contact the development team.

---

## Roadmap

### Planned Features

- Email notifications for orders
- Advanced search with filters
- Product categories with icons
- Wishlist functionality
- Seller verification system
- Payment integration
- Mobile app (React Native)
- Admin analytics dashboard
- Bulk product upload
- Product recommendations

---

**Happy Trading!**
