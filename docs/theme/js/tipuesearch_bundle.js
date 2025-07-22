// Use a CDN for jQuery
document.write('<script src="https://code.jquery.com/jquery-3.6.0.min.js"><\/script>');

// Inline script
$(document).ready(function () {
    $("#tipue_search_input").tipuesearch({
        show: 10,
        mode: "json",
        contentLocation: "{{ SITEURL }}/tipuesearch_content.js",
    });
});