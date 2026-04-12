// API Helper Functions

// Get access token from localStorage
function getAccessToken() {
    return localStorage.getItem('access_token');
}

// Generic API request function with JWT
async function apiRequest(url, options = {}) {
    const defaultOptions = {
        headers: {
            'Content-Type': 'application/json',
        }
    };
    
    const config = { ...defaultOptions, ...options };
    
    // Add JWT token if available
    const token = getAccessToken();
    if (token) {
        config.headers['Authorization'] = `Bearer ${token}`;
    }
    
    // Merge headers
    if (options.headers) {
        config.headers = { ...defaultOptions.headers, ...options.headers };
    }
    
    try {
        const response = await fetch(url, config);
        
        // Handle different response types
        const contentType = response.headers.get('content-type');
        let data;
        
        if (contentType && contentType.includes('application/json')) {
            data = await response.json();
        } else {
            data = await response.text();
        }
        
        if (!response.ok) {
            // Handle 401 Unauthorized - token expired or invalid
            if (response.status === 401) {
                // Clear invalid tokens
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                localStorage.removeItem('user');
                
                // If this was an authenticated request, redirect to login
                if (token && window.location.pathname !== '/login.html' && window.location.pathname !== '/register.html') {
                    // Only redirect if user was trying to access protected content
                    const protectedPaths = ['/profile.html', '/orders.html', '/sell.html', '/cart.html', '/profile-edit.html'];
                    if (protectedPaths.some(path => window.location.pathname.includes(path))) {
                        window.location.href = '/login.html?redirect=' + encodeURIComponent(window.location.pathname);
                        return;
                    }
                }
            }
            
            // Create detailed error message
            let errorMessage = 'Request failed';
            
            if (typeof data === 'object') {
                // Django validation errors
                if (data.error) {
                    errorMessage = data.error;
                } else if (data.detail) {
                    errorMessage = data.detail;
                } else {
                    // Field-specific errors
                    const errors = [];
                    for (const [field, messages] of Object.entries(data)) {
                        if (Array.isArray(messages)) {
                            errors.push(`${field}: ${messages.join(', ')}`);
                        } else {
                            errors.push(`${field}: ${messages}`);
                        }
                    }
                    if (errors.length > 0) {
                        errorMessage = errors.join('; ');
                    }
                }
            } else if (typeof data === 'string') {
                errorMessage = data;
            }
            
            console.error('API Error Response:', data);
            throw new Error(errorMessage);
        }
        
        return data;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// GET request
async function apiGet(url) {
    return apiRequest(url, { method: 'GET' });
}

// POST request
async function apiPost(url, data) {
    return apiRequest(url, {
        method: 'POST',
        body: JSON.stringify(data)
    });
}

// PUT request
async function apiPut(url, data) {
    return apiRequest(url, {
        method: 'PUT',
        body: JSON.stringify(data)
    });
}

// DELETE request
async function apiDelete(url) {
    return apiRequest(url, { method: 'DELETE' });
}

// POST with FormData (for file uploads)
async function apiPostFormData(url, formData) {
    const token = getAccessToken();
    const headers = {};
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }
    
    return apiRequest(url, {
        method: 'POST',
        body: formData,
        headers: headers // Let browser set Content-Type for FormData
    });
}

// Show loading spinner
function showLoading() {
    const spinner = document.createElement('div');
    spinner.id = 'loading-spinner';
    spinner.className = 'spinner-overlay';
    spinner.innerHTML = `
        <div class="spinner-border text-light" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    `;
    document.body.appendChild(spinner);
}

// Hide loading spinner
function hideLoading() {
    const spinner = document.getElementById('loading-spinner');
    if (spinner) {
        spinner.remove();
    }
}

// Show alert message
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show alert-floating`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(alertDiv);
    
    // Auto dismiss after 5 seconds
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

// Format price
function formatPrice(price) {
    return `GH₵ ${parseFloat(price).toFixed(2)}`;
}

// Format date
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

// Get condition badge class
function getConditionBadge(condition) {
    const badges = {
        'new': 'bg-success',
        'like_new': 'bg-info',
        'good': 'bg-primary',
        'fair': 'bg-warning'
    };
    return badges[condition] || 'bg-secondary';
}

// Get condition label
function getConditionLabel(condition) {
    const labels = {
        'new': 'New',
        'like_new': 'Like New',
        'good': 'Good',
        'fair': 'Fair'
    };
    return labels[condition] || condition;
}

// Get status badge class
function getStatusBadge(status) {
    const badges = {
        'pending': 'bg-warning',
        'confirmed': 'bg-info',
        'completed': 'bg-success',
        'cancelled': 'bg-danger'
    };
    return badges[status] || 'bg-secondary';
}

// Generate star rating HTML
function generateStarRating(rating, maxStars = 5) {
    let html = '<span class="star-rating">';
    for (let i = 1; i <= maxStars; i++) {
        if (i <= rating) {
            html += '<i class="bi bi-star-fill"></i>';
        } else {
            html += '<i class="bi bi-star"></i>';
        }
    }
    html += '</span>';
    return html;
}

// Get user initials for avatar
function getUserInitials(name) {
    if (!name) return '?';
    const parts = name.split(' ');
    if (parts.length >= 2) {
        return (parts[0][0] + parts[1][0]).toUpperCase();
    }
    return name.substring(0, 2).toUpperCase();
}

// Generate WhatsApp URL
function generateWhatsAppURL(phone, message) {
    // Remove non-digits
    let cleanPhone = phone.replace(/\D/g, '');
    
    // Add Ghana country code if needed
    if (cleanPhone.length === 10 && cleanPhone[0] === '0') {
        cleanPhone = '233' + cleanPhone.substring(1);
    }
    
    return `https://wa.me/${cleanPhone}?text=${encodeURIComponent(message)}`;
}
