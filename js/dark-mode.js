// ============================================================
// DARK MODE TOGGLE
// ============================================================

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const html = document.documentElement;

    // ============================================================
    // GET PREFERRED THEME
    // ============================================================
    function getPreferredTheme() {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            return savedTheme;
        }
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        return prefersDark ? 'dark' : 'light';
    }

    // ============================================================
    // APPLY THEME
    // ============================================================
    function applyTheme(theme) {
        html.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);

        if (themeIcon) {
            themeIcon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
        }
    }

    // ============================================================
    // TOGGLE THEME
    // ============================================================
    function toggleTheme() {
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        applyTheme(newTheme);
    }

    // ============================================================
    // INITIALIZE THEME
    // ============================================================
    const initialTheme = getPreferredTheme();
    applyTheme(initialTheme);

    // ============================================================
    // EVENT LISTENERS
    // ============================================================
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }

    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
        if (!localStorage.getItem('theme')) {
            const newTheme = e.matches ? 'dark' : 'light';
            applyTheme(newTheme);
        }
    });

    console.log('Dark Mode: Initialized');
});