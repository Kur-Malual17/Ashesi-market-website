// Authentication Management

// Initialize CSRF token
async function initCSRF() {
    try {
        await fetch(API_ENDPOINTS.csrf, {
            method: 'GET',
            credentials: 'include',
        });
    } catch (error) {
        console.error('Error initializing CSRF:', error);
    }
}

// Check if user is logged in
function isLoggedIn() {
    return localStorage.getItem('user') !== null;
}

// Get current user
function getCurrentUser() {
    const userStr = localStorage.getItem('user');
    return userStr ? JSON.parse(userStr) : null;
}

// Save user to localStorage
function saveUser(user) {
    localStorage.setItem('user', JSON.stringify(user));
}

// Remove user from localStorage
function removeUser() {
    localStorage.removeItem('user');
}

// Update navigation based on auth status
function updateNavigation() {
    const loggedIn = isLoggedIn();
    const user = getCurrentUser();
    
    // Elements that might not exist on all pages
    const navLogin = document.getElementById('nav-login');
    const navRegister = document.getElementById('nav-register');
    const navLogout = document.getElementById('nav-logout');
    const navCart = document.getElementById('nav-cart');
    const navOrders = document.getElementById('nav-orders');
    const navProfile = document.getElementById('nav-profile');
    const navSell = document.getElementById('nav-sell');
    const navSearch = document.querySelector('.nav-search');
    
    // Show/hide nav items
    if (navLogin) navLogin.style.display = loggedIn ? 'none' : 'block';
    if (navRegister) navRegister.style.display = loggedIn ? 'none' : 'block';
    if (navLogout) navLogout.style.display = loggedIn ? 'block' : 'none';
    if (navProfile) navProfile.style.display = loggedIn ? 'block' : 'none';
    
    if (loggedIn && user) {
        // Role-specific navigation
        if (user.role === 'buyer') {
            // BUYER: Show cart, hide sell button, show search
            if (navCart) navCart.style.display = 'block';
            if (navSell) navSell.style.display = 'none';
            if (navOrders) {
                navOrders.style.display = 'block';
                navOrders.textContent = 'My Purchases';
            }
            if (navSearch) navSearch.style.display = 'flex';
        } else if (user.role === 'seller') {
            // SELLER: Hide cart, show sell button, hide search (optional)
            if (navCart) navCart.style.display = 'none';
            if (navSell) navSell.style.display = 'block';
            if (navOrders) {
                navOrders.style.display = 'block';
                navOrders.textContent = 'My Sales';
            }
            // Keep search visible for sellers to see what's on the marketplace
            if (navSearch) navSearch.style.display = 'flex';
        } else if (user.role === 'both') {
            // BOTH: Show everything
            if (navCart) navCart.style.display = 'block';
            if (navSell) navSell.style.display = 'block';
            if (navOrders) {
                navOrders.style.display = 'block';
                navOrders.textContent = 'Orders';
            }
            if (navSearch) navSearch.style.display = 'flex';
        }
    } else {
        // Not logged in
        if (navCart) navCart.style.display = 'none';
        if (navSell) navSell.style.display = 'none';
        if (navOrders) navOrders.style.display = 'none';
    }
    
    // Update hero button
    const heroBtn = document.getElementById('hero-sell-btn');
    if (heroBtn) {
        if (loggedIn && user && (user.role === 'seller' || user.role === 'both')) {
            heroBtn.href = 'sell.html';
            heroBtn.textContent = 'List a Product';
        } else if (loggedIn) {
            // For buyer-only users, change to browse products
            heroBtn.href = 'products.html';
            heroBtn.textContent = 'Browse Products';
        }
    }
}

// Logout function
async function logout() {
    try {
        await apiPost(API_ENDPOINTS.logout, {});
    } catch (error) {
        console.error('Logout error:', error);
    }
    
    removeUser();
    window.location.href = 'index.html';
}

// Require authentication
function requireAuth() {
    if (!isLoggedIn()) {
        window.location.href = 'login.html?redirect=' + encodeURIComponent(window.location.pathname);
        return false;
    }
    return true;
}

// Initialize auth on page load
document.addEventListener('DOMContentLoaded', async function() {
    // Initialize CSRF token first
    await initCSRF();
    
    updateNavigation();
    
    // Update cart badge if logged in
    if (isLoggedIn()) {
        updateCartBadge();
    }
});

// Update cart badge
async function updateCartBadge() {
    if (!isLoggedIn()) return;
    
    try {
        const cart = await apiGet(API_ENDPOINTS.cart);
        const badge = document.getElementById('cart-badge');
        if (badge && cart.total_items > 0) {
            badge.textContent = cart.total_items;
            badge.style.display = 'inline-block';
        } else if (badge) {
            badge.style.display = 'none';
        }
    } catch (error) {
        console.error('Error updating cart badge:', error);
        // If we get a 403, the session might be invalid
        if (error.message.includes('403') || error.message.includes('Forbidden')) {
            console.warn('Session invalid, clearing local storage');
            removeUser();
            updateNavigation();
        }
    }
}
