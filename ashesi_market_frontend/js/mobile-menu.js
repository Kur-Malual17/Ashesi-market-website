// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    // Create mobile menu toggle button
    const navInner = document.querySelector('.nav-inner');
    const navActions = document.querySelector('.nav-actions');
    
    if (navInner && navActions) {
        // Create toggle button
        const toggleBtn = document.createElement('button');
        toggleBtn.className = 'mobile-menu-toggle';
        toggleBtn.setAttribute('aria-label', 'Toggle menu');
        toggleBtn.innerHTML = '☰';
        
        // Insert before nav-actions
        navInner.insertBefore(toggleBtn, navActions);
        
        // Toggle menu on click
        toggleBtn.addEventListener('click', function() {
            navActions.classList.toggle('active');
            
            // Change icon
            if (navActions.classList.contains('active')) {
                toggleBtn.innerHTML = '✕';
            } else {
                toggleBtn.innerHTML = '☰';
            }
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!navInner.contains(event.target) && navActions.classList.contains('active')) {
                navActions.classList.remove('active');
                toggleBtn.innerHTML = '☰';
            }
        });
        
        // Close menu when clicking a link
        const navLinks = navActions.querySelectorAll('.nav-link, .btn');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navActions.classList.remove('active');
                toggleBtn.innerHTML = '☰';
            });
        });
    }
});
