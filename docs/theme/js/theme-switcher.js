/**
 * Theme Switcher - Dark/light mode toggle with sun/moon icons
 * 
 * Behavior:
 * - On first visit: Follow browser's prefers-color-scheme
 * - When user clicks toggle: Switch theme and save to localStorage
 * - On return visit: Restore saved preference
 * 
 * Note: Initial theme is applied via inline script in <head> to prevent FOIT.
 */
(function() {
  'use strict';

  var STORAGE_KEY = 'theme-preference';
  var darkQuery = window.matchMedia('(prefers-color-scheme: dark)');

  function getStoredTheme() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      return null;
    }
  }

  function setStoredTheme(theme) {
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch (e) {
      // localStorage not available
    }
  }

  function getEffectiveTheme() {
    var stored = getStoredTheme();
    if (stored === 'dark' || stored === 'light') {
      return stored;
    }
    // Follow system preference
    return darkQuery.matches ? 'dark' : 'light';
  }

  function applyTheme(theme) {
    if (theme === 'dark' || theme === 'light') {
      document.documentElement.setAttribute('data-theme', theme);
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
    updateIcon();
  }

  function updateIcon() {
    var btn = document.getElementById('theme-toggle');
    if (!btn) return;
    
    var sunIcon = btn.querySelector('.fa-sun');
    var moonIcon = btn.querySelector('.fa-moon');
    if (!sunIcon || !moonIcon) return;

    var effective = getEffectiveTheme();
    // Show sun when dark (click to go light), show moon when light (click to go dark)
    sunIcon.style.display = effective === 'dark' ? 'inline' : 'none';
    moonIcon.style.display = effective === 'light' ? 'inline' : 'none';
  }

  function toggle() {
    var current = getEffectiveTheme();
    var next = current === 'dark' ? 'light' : 'dark';
    setStoredTheme(next);
    applyTheme(next);
  }

  // Initialize on DOM ready
  document.addEventListener('DOMContentLoaded', function() {
    var btn = document.getElementById('theme-toggle');
    if (btn) {
      btn.addEventListener('click', toggle);
    }
    updateIcon();
  });

  // Listen for system preference changes (when no manual override)
  darkQuery.addEventListener('change', function() {
    if (!getStoredTheme()) {
      updateIcon();
    }
  });

  // Expose global API
  window.theme = {
    toggle: toggle,
    get: getEffectiveTheme
  };
})();

/**
 * Reading Progress Bar
 * Shows scroll progress as a thin bar at the top of the page
 */
(function() {
  'use strict';

  var progressBar = null;

  function updateProgress() {
    if (!progressBar) return;
    
    var scrollTop = window.scrollY || document.documentElement.scrollTop;
    var docHeight = document.documentElement.scrollHeight - window.innerHeight;
    
    if (docHeight > 0) {
      var progress = (scrollTop / docHeight) * 100;
      progressBar.style.width = Math.min(progress, 100) + '%';
    }
  }

  document.addEventListener('DOMContentLoaded', function() {
    progressBar = document.getElementById('reading-progress');
    if (progressBar) {
      window.addEventListener('scroll', updateProgress, { passive: true });
      updateProgress();
    }
  });
})();

/**
 * Table of Contents Generator
 * Auto-generates TOC from h2/h3 headings in article content
 * Only shows if there are 3+ headings, hidden by default (uses <details>)
 */
(function() {
  'use strict';

  document.addEventListener('DOMContentLoaded', function() {
    var tocContainer = document.getElementById('toc-container');
    var tocList = tocContainer ? tocContainer.querySelector('.toc-list') : null;
    var content = document.querySelector('.article-content');
    
    if (!tocContainer || !tocList || !content) return;

    var headings = content.querySelectorAll('h2, h3');
    
    // Hide TOC if fewer than 3 headings
    if (headings.length < 3) {
      tocContainer.style.display = 'none';
      return;
    }

    headings.forEach(function(heading, index) {
      // Ensure heading has an ID
      if (!heading.id) {
        heading.id = 'heading-' + index;
      }

      var li = document.createElement('li');
      li.className = 'toc-item toc-' + heading.tagName.toLowerCase();
      
      var a = document.createElement('a');
      a.href = '#' + heading.id;
      a.textContent = heading.textContent;
      
      li.appendChild(a);
      tocList.appendChild(li);
    });
  });
})();

/**
 * Copy Code Button
 * Adds a copy button to all code blocks
 */
(function() {
  'use strict';

  document.addEventListener('DOMContentLoaded', function() {
    // Find all code blocks (both <pre><code> and highlight tables)
    var codeBlocks = document.querySelectorAll('.article-content pre, .article-content .highlight');
    
    codeBlocks.forEach(function(block) {
      // Skip if already has a copy button
      if (block.querySelector('.copy-btn')) return;
      
      // Create wrapper if needed
      var wrapper = block;
      if (!block.classList.contains('code-block-wrapper')) {
        wrapper = document.createElement('div');
        wrapper.className = 'code-block-wrapper';
        block.parentNode.insertBefore(wrapper, block);
        wrapper.appendChild(block);
      }
      
      // Create copy button
      var btn = document.createElement('button');
      btn.className = 'copy-btn';
      btn.setAttribute('aria-label', 'Copy code');
      btn.innerHTML = '<i class="fas fa-copy"></i>';
      
      btn.addEventListener('click', function() {
        var code = block.querySelector('code') || block.querySelector('pre') || block;
        var text = code.textContent || code.innerText;
        
        navigator.clipboard.writeText(text).then(function() {
          btn.innerHTML = '<i class="fas fa-check"></i>';
          btn.classList.add('copied');
          setTimeout(function() {
            btn.innerHTML = '<i class="fas fa-copy"></i>';
            btn.classList.remove('copied');
          }, 2000);
        }).catch(function() {
          // Fallback for older browsers
          var textarea = document.createElement('textarea');
          textarea.value = text;
          textarea.style.position = 'fixed';
          textarea.style.opacity = '0';
          document.body.appendChild(textarea);
          textarea.select();
          try {
            document.execCommand('copy');
            btn.innerHTML = '<i class="fas fa-check"></i>';
            btn.classList.add('copied');
            setTimeout(function() {
              btn.innerHTML = '<i class="fas fa-copy"></i>';
              btn.classList.remove('copied');
            }, 2000);
          } catch (e) {}
          document.body.removeChild(textarea);
        });
      });
      
      wrapper.appendChild(btn);
    });
  });
})();
