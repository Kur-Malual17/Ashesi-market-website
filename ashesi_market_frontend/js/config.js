// API Configuration
// Use environment variable if available, otherwise use Railway production URL
const API_BASE_URL = window.ENV?.API_BASE_URL || 'ashesi-market-website-production.up.railway.app';

// For local development, uncomment the line below:
// const API_BASE_URL = 'http://localhost:8000/api';

// API Endpoints
const API_ENDPOINTS = {
    // CSRF
    csrf: `${API_BASE_URL}/csrf/`,
    
    // Auth
    register: `${API_BASE_URL}/auth/register/`,
    login: `${API_BASE_URL}/auth/login/`,
    logout: `${API_BASE_URL}/auth/logout/`,
    currentUser: `${API_BASE_URL}/auth/user/`,
    
    // Products
    products: `${API_BASE_URL}/products/`,
    productDetail: (id) => `${API_BASE_URL}/products/${id}/`,
    productUploadImage: (id) => `${API_BASE_URL}/products/${id}/upload_image/`,
    
    // Categories
    categories: `${API_BASE_URL}/categories/`,
    
    // Cart
    cart: `${API_BASE_URL}/cart/`,
    cartAdd: `${API_BASE_URL}/cart/add/`,
    cartUpdate: (id) => `${API_BASE_URL}/cart/update/${id}/`,
    cartRemove: (id) => `${API_BASE_URL}/cart/remove/${id}/`,
    
    // Orders
    orders: `${API_BASE_URL}/orders/`,
    checkout: `${API_BASE_URL}/checkout/`,
    orderDetail: (id) => `${API_BASE_URL}/orders/${id}/`,
    orderUpdateStatus: (id) => `${API_BASE_URL}/orders/${id}/update_status/`,
    orderRemove: (id) => `${API_BASE_URL}/orders/${id}/remove_order/`,
    
    // Reviews
    reviews: `${API_BASE_URL}/reviews/`,
    
    // Profile
    profile: `${API_BASE_URL}/profile/`,
    userProfile: (id) => `${API_BASE_URL}/users/${id}/`,
};

// App Configuration
const APP_CONFIG = {
    appName: 'Ashesi Market',
    itemsPerPage: 20,
    maxImageSize: 3 * 1024 * 1024, // 3MB
    allowedImageTypes: ['image/jpeg', 'image/png', 'image/webp'],
};
