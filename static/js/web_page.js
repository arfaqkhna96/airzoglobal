function showEnquiryMessage() {
 console.log('Enquiry Now button clicked!');
 }
document.addEventListener('DOMContentLoaded', function () {
    // Normalize path to remove trailing slash
    const path = window.location.pathname.replace(/\/$/, '');

    // Define path-to-ID mapping
    const navLinks = {
        '/': 'nav-home',
        '/about': 'nav-about',
        '/careers': 'nav-careers',
        '/news': 'nav-news',
        '/contact': 'nav-contact',
    };

    // Remove 'active' class from all nav links
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
    });

    // Add 'active' class to the matched link, if it exists
    const navItem = document.getElementById(navLinks[path]);
    if (navItem) {
        navItem.classList.add('active');
    }
});

