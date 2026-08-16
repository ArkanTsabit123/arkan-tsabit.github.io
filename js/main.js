// ============================================================
// MAIN FUNCTIONALITY
// ============================================================

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    var hamburger = document.getElementById('hamburger');
    var navList = document.getElementById('navList');
    var currentYear = document.getElementById('currentYear');

    // ============================================================
    // MOBILE MENU
    // ============================================================
    if (hamburger && navList) {
        hamburger.addEventListener('click', function() {
            navList.classList.toggle('open');
            var isOpen = navList.classList.contains('open');
            hamburger.setAttribute('aria-expanded', isOpen);
        });

        document.addEventListener('click', function(e) {
            var isClickInside = hamburger.contains(e.target) || navList.contains(e.target);
            if (!isClickInside && navList.classList.contains('open')) {
                navList.classList.remove('open');
                hamburger.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // ============================================================
    // FOOTER YEAR
    // ============================================================
    if (currentYear) {
        currentYear.textContent = new Date().getFullYear();
    }

    // ============================================================
    // SMOOTH SCROLL
    // ============================================================
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            var targetId = this.getAttribute('href');
            if (targetId === '#') return;

            var targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // ============================================================
    // ACTIVE NAV LINK
    // ============================================================
    var currentPath = window.location.pathname;
    var navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(function(link) {
        var linkPath = link.getAttribute('href');
        if (linkPath === currentPath || (currentPath === '/' && linkPath === 'index.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});