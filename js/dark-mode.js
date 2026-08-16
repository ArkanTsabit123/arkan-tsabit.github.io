// ============================================================
// DARK MODE TOGGLE
// ============================================================

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    var themeToggle = document.getElementById('themeToggle');
    var themeIcon = document.getElementById('themeIcon');
    var htmlElement = document.documentElement;

    var STORAGE_KEY = 'theme';

    // ============================================================
    // GET PREFERRED THEME
    // ============================================================
    function getPreferredTheme() {
        var storedTheme = localStorage.getItem(STORAGE_KEY);
        if (storedTheme === 'dark' || storedTheme === 'light') {
            return storedTheme;
        }

        var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        return prefersDark ? 'dark' : 'light';
    }

    // ============================================================
    // SET THEME
    // ============================================================
    function setTheme(theme) {
        htmlElement.setAttribute('data-theme', theme);
        localStorage.setItem(STORAGE_KEY, theme);

        if (themeIcon) {
            if (theme === 'dark') {
                themeIcon.className = 'fas fa-sun';
            } else {
                themeIcon.className = 'fas fa-moon';
            }
        }
    }

    // ============================================================
    // TOGGLE THEME
    // ============================================================
    function toggleTheme() {
        var currentTheme = htmlElement.getAttribute('data-theme') || 'light';
        var newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    }

    // ============================================================
    // INITIALIZE
    // ============================================================
    var initialTheme = getPreferredTheme();
    setTheme(initialTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }

    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
        if (!localStorage.getItem(STORAGE_KEY)) {
            var newTheme = e.matches ? 'dark' : 'light';
            setTheme(newTheme);
        }
    });
});