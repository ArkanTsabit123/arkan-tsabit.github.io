// ============================================================
// MULTI-LANGUAGE SUPPORT (i18n)
// ============================================================

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    const langToggle = document.getElementById('langToggle');
    const langText = document.getElementById('langText');

    let currentLang = localStorage.getItem('lang') || 'en';
    let translations = {};

    // ============================================================
    // LOAD TRANSLATIONS
    // ============================================================
    async function loadTranslations(lang) {
        try {
            const response = await fetch(`data/i18n/${lang}.json`);
            if (!response.ok) {
                throw new Error(`Failed to load translations for ${lang}`);
            }
            translations = await response.json();
            return true;
        } catch (error) {
            console.error('Error loading translations:', error);
            return false;
        }
    }

    // ============================================================
    // APPLY TRANSLATIONS TO PAGE
    // ============================================================
    function applyTranslations() {
        document.querySelectorAll('[data-i18n]').forEach(function(element) {
            const key = element.getAttribute('data-i18n');
            const value = getNestedValue(translations, key);

            if (value !== undefined) {
                if (element.tagName === 'INPUT' && element.hasAttribute('placeholder')) {
                    element.placeholder = value;
                } else if (element.tagName === 'META' && element.hasAttribute('name')) {
                    // Skip meta tags for now
                } else {
                    element.textContent = value;
                }
            }
        });

        // Update language toggle button text
        if (langText) {
            langText.textContent = currentLang.toUpperCase();
        }
    }

    // ============================================================
    // GET NESTED OBJECT VALUE
    // ============================================================
    function getNestedValue(obj, path) {
        return path.split('.').reduce(function(current, key) {
            return current && current[key] !== undefined ? current[key] : undefined;
        }, obj);
    }

    // ============================================================
    // SET LANGUAGE
    // ============================================================
    async function setLanguage(lang) {
        if (lang === currentLang && Object.keys(translations).length > 0) {
            return;
        }

        const loaded = await loadTranslations(lang);
        if (loaded) {
            currentLang = lang;
            localStorage.setItem('lang', lang);
            applyTranslations();
            document.documentElement.lang = lang === 'id' ? 'id' : 'en';
        }
    }

    // ============================================================
    // TOGGLE LANGUAGE
    // ============================================================
    function toggleLanguage() {
        const nextLang = currentLang === 'en' ? 'id' : 'en';
        setLanguage(nextLang);
    }

    // ============================================================
    // INITIALIZE
    // ============================================================
    async function initLanguage() {
        const savedLang = localStorage.getItem('lang') || 'en';
        await setLanguage(savedLang);
    }

    // ============================================================
    // EVENT LISTENERS
    // ============================================================
    if (langToggle) {
        langToggle.addEventListener('click', toggleLanguage);
    }

    // ============================================================
    // START
    // ============================================================
    initLanguage();

    console.log('i18n: Initialized');
});