/**
 * Hide documentation link on production (GitHub Pages)
 * Documentation is only accessible on localhost for internal use
 */
(function() {
    var isLocal = window.location.hostname === 'localhost' || 
                  window.location.hostname === '127.0.0.1';
    
    var docsLink = document.getElementById('docsLink');
    
    if (docsLink && !isLocal) {
        docsLink.style.display = 'none';
    }

    // Also hide the link after the DOM is fully loaded
    document.addEventListener('DOMContentLoaded', function() {
        var docsLink = document.getElementById('docsLink');
        if (docsLink && !isLocal) {
            docsLink.style.display = 'none';
        }
    });
})();