// Main JavaScript for Homepage

document.addEventListener('DOMContentLoaded', async function() {
    await loadCategories();
    await loadLatestProducts();
    updateHeroButton();
});

// Load categories
async function loadCategories() {
    try {
        const categories = await apiGet(API_ENDPOINTS.categories);
        const container = document.getElementById('categories-container');
        
        if (categories && categories.length > 0) {
            container.innerHTML = categories.map(cat => `
                <a href="products.html?category=${cat.id}" class="pill pill-category" style="font-size:.85rem;padding:6px 14px;">
                    ${cat.name}
                </a>
            `).join('');
        }
    } catch (error) {
        console.error('Error loading categories:', error);
    }
}

// Load latest products
async function loadLatestProducts() {
    try {
        const response = await apiGet(API_ENDPOINTS.products + '?page_size=20');
        const products = response.results || response;
        const container = document.getElementById('products-container');
        
        if (products && products.length > 0) {
            container.innerHTML = '<div class="product-grid">' + 
                products.map(product => createProductCard(product)).join('') +
                '</div>';
        } else {
            container.innerHTML = `
                <div class="empty-state">
                    <div class="icon">🛒</div>
                    <p>No products yet. Be the first to list something!</p>
                </div>
            `;
        }
    } catch (error) {
        console.error('Error loading products:', error);
        document.getElementById('products-container').innerHTML = `
            <div class="alert alert-error">
                Failed to load products. Please try again later.
            </div>
        `;
    }
}

// Create product card HTML
function createProductCard(product) {
    const imageUrl = product.primary_image || '';
    const imageHtml = imageUrl 
        ? `<img src="${imageUrl}" alt="${escapeHtml(product.title)}" loading="lazy">`
        : `<div class="no-img">📦</div>`;
    
    const condition = product.condition ? product.condition.replace('_', ' ') : 'good';
    
    return `
        <a href="product.html?id=${product.id}" class="card product-card" style="text-decoration:none;color:inherit;">
            <div class="thumb">
                ${imageHtml}
            </div>
            <div class="card-body">
                <div class="flex gap-2" style="flex-wrap:wrap;">
                    <span class="pill pill-category">${escapeHtml(product.category_name || 'Other')}</span>
                    <span class="pill pill-condition">${escapeHtml(condition)}</span>
                </div>
                <div class="card-title">${escapeHtml(product.title)}</div>
                <div class="card-meta">
                    ${escapeHtml(product.seller_name || 'Unknown')}
                    ${product.location ? ' · ' + escapeHtml(product.location) : ''}
                </div>
                <div class="card-price">GH₵ ${formatPrice(product.price)}</div>
            </div>
        </a>
    `;
}

// Update hero button based on login status
function updateHeroButton() {
    const heroTitle = document.getElementById('hero-title');
    const heroSubtitle = document.getElementById('hero-subtitle');
    const heroBtn = document.getElementById('hero-btn-1');
    const heroActions = document.getElementById('hero-actions');
    
    if (!isLoggedIn()) {
        // Not logged in - show default
        if (heroTitle) heroTitle.textContent = 'Buy & Sell on Campus 🎓';
        if (heroSubtitle) heroSubtitle.textContent = "Ashesi's student marketplace — discover products from your fellow students, or start selling today.";
        if (heroBtn) {
            heroBtn.href = 'register.html';
            heroBtn.textContent = 'Get Started';
        }
        return;
    }
    
    const user = getCurrentUser();
    if (!user) return;
    
    // Customize based on role
    if (user.role === 'buyer') {
        // BUYER ONLY - Focus on shopping
        if (heroTitle) heroTitle.textContent = 'Shop on Campus 🛍️';
        if (heroSubtitle) heroSubtitle.textContent = "Discover great deals from your fellow Ashesi students. Browse products, add to cart, and checkout easily.";
        if (heroActions) {
            heroActions.innerHTML = `
                <a href="products.html" class="btn btn-hero-primary">Browse Products</a>
                <a href="cart.html" class="btn btn-hero-outline">View Cart</a>
            `;
        }
    } else if (user.role === 'seller') {
        // SELLER ONLY - Focus on selling
        if (heroTitle) heroTitle.textContent = 'Sell on Campus 📦';
        if (heroSubtitle) heroSubtitle.textContent = "List your products and reach Ashesi students. Manage your inventory and track your sales easily.";
        if (heroActions) {
            heroActions.innerHTML = `
                <a href="sell.html" class="btn btn-hero-primary">+ List a Product</a>
                <a href="orders.html" class="btn btn-hero-outline">My Sales</a>
            `;
        }
    } else if (user.role === 'both') {
        // BOTH - Full marketplace
        if (heroTitle) heroTitle.textContent = 'Buy & Sell on Campus 🎓';
        if (heroSubtitle) heroSubtitle.textContent = "Ashesi's student marketplace — discover products from your fellow students, or start selling today.";
        if (heroActions) {
            heroActions.innerHTML = `
                <a href="sell.html" class="btn btn-hero-primary">+ List a Product</a>
                <a href="products.html" class="btn btn-hero-outline">Browse Products</a>
            `;
        }
    }
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Format price
function formatPrice(price) {
    return parseFloat(price).toFixed(2);
}
