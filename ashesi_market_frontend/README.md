# Ashesi Market Frontend

Beautiful, responsive frontend matching the original PHP design - built with vanilla HTML, CSS, and JavaScript.

## ✨ Design Features

- **Original Design** - Exact replica of the PHP version's beautiful UI
- **Custom CSS** - No Bootstrap, pure custom styling
- **Google Fonts** - DM Sans & Syne for elegant typography
- **Smooth Animations** - Hover effects, transitions
- **Responsive** - Works perfectly on all devices
- **Clean Code** - Vanilla JavaScript, no frameworks

## 🎨 Design System

### Colors
- **Background**: `#FAF8F5` - Warm off-white
- **Surface**: `#FFFFFF` - Pure white cards
- **Border**: `#E8E4DC` - Subtle borders
- **Text**: `#1A1A2E` - Dark text
- **Muted**: `#6B6B7B` - Secondary text
- **Accent**: `#0F7B6C` - Teal primary
- **Accent 2**: `#E8593C` - Coral secondary

### Typography
- **Body**: DM Sans (400, 500, 600)
- **Headings**: Syne (700)

## 🚀 Quick Start

### 1. Start Django Backend

```bash
cd ashesi_market_django
python manage.py runserver
```

Backend must be running at `http://localhost:8000`

### 2. Open Frontend

**Option A: VS Code Live Server (Recommended)**
1. Install "Live Server" extension
2. Right-click `index.html`
3. Select "Open with Live Server"

**Option B: Python HTTP Server**
```bash
cd ashesi_market_frontend
python -m http.server 8080
```

**Option C: Double-click**
Just open `index.html` in your browser

### 3. Test It!

1. Visit homepage
2. Register an account
3. Login
4. Browse products
5. Enjoy the beautiful UI!

## 📁 Project Structure

```
ashesi_market_frontend/
├── index.html          # Homepage
├── login.html          # Login page
├── register.html       # Registration
├── products.html       # Product listing
│
├── css/
│   └── style.css       # Original design CSS
│
└── js/
    ├── config.js       # API configuration
    ├── auth.js         # Authentication
    ├── api.js          # API helpers
    └── main.js         # Homepage logic
```

## 🎯 Pages

### ✅ Completed
- **index.html** - Homepage with hero, categories, latest products
- **login.html** - Beautiful login form
- **register.html** - Registration with all fields
- **products.html** - Browse with filters sidebar

### ⏳ To Be Created
- **product.html** - Product detail page
- **cart.html** - Shopping cart
- **checkout.html** - Checkout process
- **orders.html** - Order history
- **profile.html** - User profile
- **sell.html** - Create product listing

## 🎨 Design Elements

### Navigation
- Sticky navbar with search
- Brand logo with emoji
- Dynamic user menu
- Cart badge counter

### Hero Section
- Gradient background (teal)
- Large heading with emoji
- Call-to-action buttons
- Responsive layout

### Product Cards
- 4:3 aspect ratio images
- Hover animations
- Category & condition pills
- Price in GH₵
- Seller info

### Forms
- Clean input styling
- Focus states
- Validation
- Error messages
- Loading states

### Buttons
- Primary (coral)
- Secondary (teal)
- Outline
- Small variants
- Hover effects

## 🔌 API Integration

### Endpoints Used
```javascript
// Products
GET  /api/products/              // List products
GET  /api/products/?search=...   // Search
GET  /api/products/?category=... // Filter

// Categories
GET  /api/categories/            // List categories

// Auth
POST /api/auth/register/         // Register
POST /api/auth/login/            // Login
POST /api/auth/logout/           // Logout
```

### Making API Calls

```javascript
// GET request
const products = await apiGet(API_ENDPOINTS.products);

// POST request
const response = await apiPost(API_ENDPOINTS.login, {
    email: 'user@example.com',
    password: 'password123'
});
```

## 🎨 Styling Guide

### Using CSS Variables

```css
/* Colors */
var(--c-bg)       /* Background */
var(--c-surface)  /* Cards */
var(--c-border)   /* Borders */
var(--c-text)     /* Text */
var(--c-muted)    /* Secondary text */
var(--c-accent)   /* Primary color */
var(--c-accent2)  /* Secondary color */

/* Spacing */
var(--radius)     /* 10px */
var(--radius-lg)  /* 16px */
var(--shadow)     /* Box shadow */
```

### Common Classes

```html
<!-- Layout -->
<div class="container">...</div>
<div class="card">...</div>

<!-- Buttons -->
<button class="btn btn-primary">Primary</button>
<button class="btn btn-outline">Outline</button>
<button class="btn btn-sm">Small</button>

<!-- Pills -->
<span class="pill pill-category">Electronics</span>
<span class="pill pill-condition">New</span>

<!-- Alerts -->
<div class="alert alert-success">Success!</div>
<div class="alert alert-error">Error!</div>

<!-- Utility -->
<div class="text-center">Centered</div>
<div class="text-muted">Muted text</div>
<div class="flex gap-2">Flex with gap</div>
```

## 🛠️ Development

### Adding a New Page

1. Create HTML file
2. Include fonts:
```html
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Syne:wght@700&display=swap" rel="stylesheet">
```

3. Include CSS:
```html
<link rel="stylesheet" href="css/style.css">
```

4. Include scripts:
```html
<script src="js/config.js"></script>
<script src="js/auth.js"></script>
<script src="js/api.js"></script>
```

5. Use the navbar and footer from existing pages

### Customizing Colors

Edit `css/style.css`:

```css
:root {
  --c-accent:   #YOUR_COLOR;  /* Primary */
  --c-accent2:  #YOUR_COLOR;  /* Secondary */
}
```

## 📱 Responsive Design

- **Desktop** (>768px) - Full layout
- **Mobile** (<768px) - Stacked layout, hidden search

Breakpoints handled automatically with CSS Grid and Flexbox.

## 🐛 Troubleshooting

### CORS Errors
Make sure Django has:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:5500",
]
```

### Images Not Loading
Check Django MEDIA_URL and CORS for media files.

### Fonts Not Loading
Check internet connection (Google Fonts CDN).

## 🎉 What Makes This Special

1. **Exact Design Match** - Pixel-perfect replica of PHP version
2. **No Framework** - Pure vanilla JavaScript
3. **Beautiful UI** - Custom design system
4. **Smooth Animations** - Professional feel
5. **Clean Code** - Easy to understand and modify
6. **Fast Loading** - No heavy frameworks

## 📚 Technologies

- **HTML5** - Semantic markup
- **CSS3** - Custom properties, Grid, Flexbox
- **JavaScript ES6+** - Async/await, modules
- **Google Fonts** - DM Sans & Syne
- **Fetch API** - HTTP requests

## 🚀 Next Steps

1. Complete remaining pages (product detail, cart, etc.)
2. Add image upload functionality
3. Implement cart operations
4. Add order management
5. Create user profile page
6. Build product creation form

## 💡 Tips

- Use browser DevTools to inspect the design
- Check `js/api.js` for helper functions
- All colors are in CSS variables
- Forms use the same styling pattern
- Product cards are reusable

## 📝 License

Same as backend project.

---

**Beautiful design, clean code, perfect match! 🎨**
