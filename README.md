# 🛍️ Ashesi Market

![Backend CI](https://github.com/Kur-Malual17/Ashesi-market-website/workflows/Backend%20CI%2FCD/badge.svg)
![Frontend CI](https://github.com/Kur-Malual17/Ashesi-market-website/workflows/Frontend%20CI%2FCD/badge.svg)
![Full Stack CI](https://github.com/Kur-Malual17/Ashesi-market-website/workflows/Full%20Stack%20CI%2FCD/badge.svg)

**A modern student-to-student marketplace platform built for the Ashesi University community.**

Ashesi Market connects students who want to buy and sell products within the university community. Whether you're looking to sell textbooks, electronics, or other items, or searching for great deals from fellow students, Ashesi Market makes it easy and secure.

---

## 🌐 Live Application

- **Website**: [https://ashesi-market-website.vercel.app](https://ashesi-market-website.vercel.app)
- **API Backend**: [https://ashesi-market-website-production.up.railway.app](https://ashesi-market-website-production.up.railway.app)

---

## ✨ Key Features

### For Buyers
- **Browse & Search** - Find products by category, condition, or search terms
- **Shopping Cart** - Add multiple items and checkout seamlessly
- **Order Tracking** - Monitor your purchases from pending to completed
- **Reviews** - Rate and review products after purchase
- **WhatsApp Integration** - Contact sellers directly via WhatsApp

### For Sellers
- **List Products** - Create listings with images, descriptions, and pricing
- **Sales Dashboard** - Manage orders and track earnings
- **Order Management** - Approve, confirm, or cancel orders
- **Buyer Communication** - Connect with buyers via WhatsApp
- **Image Upload** - Add up to 5 images per product

### For Everyone
- **Secure Authentication** - JWT-based login system
- **User Profiles** - Manage your account and view ratings
- **Flexible Roles** - Be a buyer, seller, or both
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Real-time Updates** - Get instant feedback on actions

---

## Getting Started

### 1. Create an Account

Visit [ashesi-market-website.vercel.app/register.html](https://ashesi-market-website.vercel.app/register.html) and sign up with:
- Your Ashesi email address
- Full name
- Password (minimum 8 characters)
- Choose your role: Buyer, Seller, or Both

### 2. Complete Your Profile

After registration:
- Add your WhatsApp number for easy communication
- Upload an ID image for verification
- Add your year group and bio (optional)

### 3. Start Using the Platform

**As a Buyer:**
1. Browse products on the homepage or products page
2. Click on any product to view details
3. Add items to your cart
4. Proceed to checkout
5. Wait for seller approval
6. Complete the transaction
7. Leave a review

**As a Seller:**
1. Click "Sell" or "+ Sell" button
2. Fill in product details (title, description, price, etc.)
3. Upload product images (up to 5)
4. Submit your listing
5. Manage orders from the "My Sales" section
6. Approve orders and communicate with buyers
7. Mark orders as completed

---

## 📱 User Roles Explained

### 🛒 Buyer
- **Can**: Browse products, make purchases, leave reviews
- **Cannot**: List products for sale
- **Best for**: Students looking to buy items

### 💼 Seller
- **Can**: List products, manage sales, view earnings
- **Cannot**: Make purchases or add items to cart
- **Best for**: Students who only want to sell

### 🔄 Both
- **Can**: Everything! Buy and sell products
- **Full access** to all platform features
- **Best for**: Active marketplace participants

---

## 🎯 How to Use Key Features

### Searching for Products
1. Use the search bar in the navigation
2. Filter by category (Electronics, Books, Clothing, etc.)
3. Filter by condition (New, Like New, Good, Fair)
4. Sort by price or date listed

### Making a Purchase
1. Add items to cart
2. Review cart contents
3. Click "Checkout"
4. Wait for seller approval (status: Pending)
5. Once approved (status: Confirmed), arrange pickup
6. After receiving item, mark as completed
7. Leave a review to help other buyers

### Selling a Product
1. Click "+ Sell" button
2. Enter product details:
   - **Title**: Clear, descriptive name
   - **Description**: Detailed information about the item
   - **Price**: In Ghana Cedis (GH₵)
   - **Category**: Select appropriate category
   - **Condition**: Be honest about item condition
   - **Quantity**: Number of items available
3. Upload images (first image becomes the main image)
4. Submit listing
5. Manage orders from "My Sales" tab

### Managing Orders (Sellers)
1. Go to Orders → My Sales
2. View pending orders
3. Click "WhatsApp Buyer" to discuss details
4. Click "Approve Order" to confirm
5. After buyer receives item, click "Mark as Completed"
6. View your earnings for each order

### Leaving Reviews (Buyers)
1. Go to Orders → My Purchases
2. Find completed orders
3. Click "Leave Review" button
4. Rate 1-5 stars
5. Add optional comment
6. Submit review

---

## 🔒 Security & Privacy

- **Secure Authentication**: Passwords are hashed and never stored in plain text
- **JWT Tokens**: Secure session management
- **HTTPS**: All data transmitted over secure connections
- **Email Verification**: Ashesi email addresses only
- **ID Verification**: Optional ID upload for trust
- **No Payment Processing**: All transactions happen offline for safety

---

## 💡 Tips for Success

### For Buyers
- Check seller ratings and reviews before purchasing
- Read product descriptions carefully
- Contact seller via WhatsApp to ask questions
- Inspect items before completing the transaction
- Leave honest reviews to help the community

### For Sellers
- Take clear, well-lit photos of your items
- Write detailed, honest descriptions
- Price items competitively
- Respond quickly to buyer inquiries
- Be honest about item condition
- Arrange safe meeting locations on campus

---

## Technology Stack

### Frontend
- **HTML5, CSS3, JavaScript** - Modern web technologies
- **Responsive Design** - Works on all devices
- **Deployed on**: Vercel

### Backend
- **Django 4.2** - Python web framework
- **Django REST Framework** - API development
- **PostgreSQL** - Production database
- **JWT Authentication** - Secure token-based auth
- **Cloudflare R2** - Image storage
- **Deployed on**: Railway

### CI/CD
- **GitHub Actions** - Automated testing and deployment
- **Automated Tests** - Backend tests with PostgreSQL
- **Code Quality** - Linting and formatting checks

---

## Order Status Guide

| Status | Meaning | Next Steps |
|--------|---------|------------|
| **Pending** | Order placed, awaiting seller approval | Seller should review and approve/reject |
| **Confirmed** | Seller approved, ready for pickup | Arrange meeting via WhatsApp |
| **Completed** | Transaction finished successfully | Buyer can leave a review |
| **Cancelled** | Order was cancelled | No further action needed |

---

## 🤝 Support & Contact

### Need Help?
- **Technical Issues**: Check browser console (F12) for errors
- **Account Issues**: Contact via WhatsApp (see seller/buyer profile)
- **Feature Requests**: Open an issue on GitHub

### Common Issues

**Can't log in?**
- Ensure you're using your registered email
- Check password (case-sensitive)
- Clear browser cache and try again

**Images not uploading?**
- Maximum file size: 3MB per image
- Supported formats: JPG, PNG, WebP
- Maximum 5 images per product

**Orders not showing?**
- Refresh the page
- Check your user role (buyers see purchases, sellers see sales)
- Ensure you're logged in

---

## Project Statistics

- **Built for**: Ashesi University Community
- **User Roles**: 3 (Buyer, Seller, Both)
- **Product Categories**: 10+
- **Maximum Images per Product**: 5
- **Maximum File Size**: 3MB per image
- **Supported Payment**: Offline (cash, mobile money)

---

## 🎓 About Ashesi University

Ashesi Market is built specifically for the Ashesi University community. Ashesi University is a private, not-for-profit university in Ghana that educates ethical, entrepreneurial leaders in Africa.

---

## 📝 License

This project is built for educational purposes as part of the Ashesi University curriculum.

---

## Acknowledgments

- **Ashesi University** - For providing the educational environment
- **Django Community** - For the excellent web framework
- **Vercel & Railway** - For hosting services
- **All Contributors** - For making this project possible

---

## 🔗 Quick Links

- [Live Website](https://ashesi-market-website.vercel.app)
- [API Documentation](https://ashesi-market-website-production.up.railway.app/api/)
- [GitHub Repository](https://github.com/Kur-Malual17/Ashesi-market-website)
- [Report an Issue](https://github.com/Kur-Malual17/Ashesi-market-website/issues)

---

**Made for the Ashesi University Community**

*Last Updated: April 2026*
