// ============================================================
// INTERNATIONALIZATION
// ============================================================

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    var langToggle = document.getElementById('langToggle');
    var langText = document.getElementById('langText');

    var STORAGE_KEY = 'language';
    var currentLang = 'en';
    var translations = {};

    // ============================================================
    // LOAD TRANSLATIONS
    // ============================================================
    async function loadTranslations(lang) {
        try {
            var response = await fetch('data/i18n/' + lang + '.json');
            if (!response.ok) {
                throw new Error('Failed to load translations for ' + lang);
            }
            return await response.json();
        } catch (error) {
            console.error('Error loading translations:', error);
            return {};
        }
    }

    // ============================================================
    // GET NESTED VALUE
    // ============================================================
    function getNestedValue(obj, path) {
        var keys = path.split('.');
        var result = obj;

        for (var i = 0; i < keys.length; i++) {
            if (result && typeof result === 'object' && keys[i] in result) {
                result = result[keys[i]];
            } else {
                return undefined;
            }
        }

        return result;
    }

    // ============================================================
    // APPLY TRANSLATIONS
    // ============================================================
    function applyTranslations(translations) {
        var elements = document.querySelectorAll('[data-i18n]');

        elements.forEach(function(element) {
            var key = element.getAttribute('data-i18n');
            var value = getNestedValue(translations, key);

            if (value !== undefined) {
                if (element.tagName === 'INPUT' && element.hasAttribute('placeholder')) {
                    element.placeholder = value;
                } else if (element.tagName === 'BUTTON' || element.tagName === 'A') {
                    var icon = element.querySelector('i');
                    if (icon) {
                        element.innerHTML = '';
                        element.appendChild(icon);
                        var textNode = document.createTextNode(' ' + value);
                        element.appendChild(textNode);
                    } else {
                        element.textContent = value;
                    }
                } else {
                    element.textContent = value;
                }
            }
        });
    }

    // ============================================================
    // SET LANGUAGE
    // ============================================================
    async function setLanguage(lang) {
        if (lang === currentLang && translations) {
            return;
        }

        var newTranslations = await loadTranslations(lang);
        if (Object.keys(newTranslations).length === 0) {
            return;
        }

        translations = newTranslations;
        currentLang = lang;
        localStorage.setItem(STORAGE_KEY, lang);

        if (langText) {
            langText.textContent = lang.toUpperCase();
        }

        applyTranslations(translations);
    }

    // ============================================================
    // TOGGLE LANGUAGE
    // ============================================================
    function toggleLanguage() {
        var newLang = currentLang === 'en' ? 'id' : 'en';
        setLanguage(newLang);
    }

    // ============================================================
    // INITIALIZE
    // ============================================================
    var storedLang = localStorage.getItem(STORAGE_KEY);
    var browserLang = navigator.language.split('-')[0];
    var initialLang = 'en';

    if (storedLang === 'en' || storedLang === 'id') {
        initialLang = storedLang;
    } else if (browserLang === 'id') {
        initialLang = 'id';
    }

    setLanguage(initialLang).then(function() {
        if (langText) {
            langText.textContent = initialLang.toUpperCase();
        }
    });

    if (langToggle) {
        langToggle.addEventListener('click', toggleLanguage);
    }
});