// ============================================================
// MAIN JAVASCRIPT
// ============================================================

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    // ============================================================
    // SET CURRENT YEAR IN FOOTER
    // ============================================================
    const yearElement = document.getElementById('currentYear');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }

    // ============================================================
    // MOBILE HAMBURGER MENU
    // ============================================================
    const hamburger = document.getElementById('hamburger');
    const navList = document.getElementById('navList');

    if (hamburger && navList) {
        hamburger.addEventListener('click', function() {
            navList.classList.toggle('open');
            hamburger.classList.toggle('active');
        });

        // Close menu on link click (mobile)
        const navLinks = navList.querySelectorAll('.nav-link');
        navLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                navList.classList.remove('open');
                hamburger.classList.remove('active');
            });
        });
    }

    // ============================================================
    // NAVIGATION ACTIVE STATE
    // ============================================================
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(function(link) {
        const href = link.getAttribute('href');
        if (href === currentPath || (href === 'index.html' && currentPath === '/')) {
            link.classList.add('active');
        } else if (href && currentPath.includes(href)) {
            link.classList.add('active');
        }
    });

    // ============================================================
    // SMOOTH SCROLL FOR ANCHOR LINKS
    // ============================================================
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                const headerHeight = document.querySelector('.header')?.offsetHeight || 0;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ============================================================
    // HEADER SHADOW ON SCROLL
    // ============================================================
    const header = document.querySelector('.header');
    let lastScrollY = window.scrollY;

    window.addEventListener('scroll', function() {
        const scrollY = window.scrollY;

        if (scrollY > 10) {
            header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.08)';
        } else {
            header.style.boxShadow = 'none';
        }

        lastScrollY = scrollY;
    });

    // ============================================================
    // OPEN CHATBOT FROM CTA BUTTON
    // ============================================================
    const openChatbotBtn = document.getElementById('openChatbotBtn');
    const chatbotToggle = document.getElementById('chatbotToggle');

    if (openChatbotBtn) {
        openChatbotBtn.addEventListener('click', function() {
            if (chatbotToggle) {
                chatbotToggle.click();
            }
        });
    }

});