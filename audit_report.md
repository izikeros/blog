# Pelican Flex Theme Frontend Audit Report

## Introduction

This report summarizes the findings of a comprehensive code audit of the Pelican Flex theme, focusing on the frontend (HTML, CSS, JavaScript) for bugs, performance bottlenecks, and areas ripe for simplification.

## Findings

### 1. Less.js and Gulp.js

*   Less.js is not used in the theme.
*   Gulp.js is used for JavaScript minification, Font Awesome copying, and Pygments CSS minification.
*   Alternative tools for these tasks can be integrated into npm scripts.

**Recommendation:**

*   Remove Gulp.js and related dependencies.
*   Implement npm scripts for JavaScript minification, Font Awesome copying, and Pygments CSS minification.

**Proposed `package.json` changes:**

```json
{
  "name": "flex",
  "version": "2.3.0",
  "description": "A minimalist Pelican theme",
  "main": "index.js",
  "directories": {
    "test": "tests"
  },
  "scripts": {
    "test": "source venv/bin/activate && pip install pelican markdown && pelican -s tests/pelicanconf.py && deactivate",
    "minify-js": "terser static/dark-theme/dark-theme.js -o static/dark-theme/dark-theme.min.js",
    "copy-fontawesome": "copyfiles -u 1 node_modules/font-awesome/**/* static/font-awesome",
    "minify-pygments": "cssnano static/pygments/*.css --base static/pygments/ --dir static/pygments/ --ext .min.css",
    "build": "npm run minify-js && npm run copy-fontawesome && npm run minify-pygments"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/alexandrevicenzi/Flex.git"
  },
  "keywords": [
    "pelican"
  ],
  "author": "Alexandre Vicenzi",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/alexandrevicenzi/Flex/issues"
  },
  "homepage": "https://github.com/alexandrevicenzi/Flex#readme",
  "devDependencies": {
    "copyfiles": "^2.4.1",
    "cssnano": "^2.1.3",
    "terser": "^5.16.1"
  }
}
```

**Note:** Due to file writing issues, these changes could not be applied directly.

### 2. Pelican Plugins

*   `pelican_jupyter.markup`: This plugin allows using Jupyter notebooks as articles. It can have a significant impact on performance.
*   `representative_image`: This plugin extracts a representative image from the summary or content. Its performance impact is likely minimal.
*   `render_math`: This plugin enables rendering mathematics using MathJax. It can have a significant impact on performance.
*   `neighbors`: This plugin adds navigation links between articles. Its performance impact is likely minimal.
*   `share_post`: This plugin is not installed and should be removed.
*   `sitemap`: This plugin generates sitemaps. Its performance impact is likely minimal.
*   `obsidian`: This plugin is installed from a Git repository and should be investigated.

**Recommendations:**

*   `pelican_jupyter.markup`: Evaluate the need for Jupyter notebook support, optimize notebook content, and customize plugin settings.
*   `representative_image`: Keep the plugin enabled, optimize images, and consider using the `image` metadata.
*   `render_math`: Evaluate the need for math rendering, optimize MathJax settings, and consider alternative rendering methods.
*   `neighbors`: Keep the plugin enabled and consider using category-specific navigation.
*   `share_post`: Remove the plugin from `pelicanconf.py`.
*   `sitemap`: Keep the plugin enabled, review the sitemap configuration, and consider excluding specific URLs.
*   `obsidian`: Investigate the plugin's purpose and configuration, as it is installed from a Git repository.

**Note:** Some plugins are installed as Python packages, as indicated in `pyproject.toml`. These include:

*   `beautifulsoup4`
*   `pelican`
*   `pelican-jupyter`
*   `pelican-render-math`
*   `pelican-share-post`
*   `typogrify`
*   `pygments`

### 3. Tipue Search

*   Tipue Search is not currently functional.

**Recommendation:**

*   Remove Tipue Search from the theme.
*   Consider alternative search solutions.

### 4. Code Structure

**Recommendations:**

*   Organize JavaScript code into modules.
*   Use consistent naming conventions.
*   Add comments to explain complex code.

### 5. Accessibility

**Recommendations:**

*   Ensure that all images have appropriate `alt` attributes.
*   Use semantic HTML elements.
*   Provide sufficient color contrast.

## Conclusion

This report provides a comprehensive overview of the Pelican Flex theme's frontend code, highlighting areas for improvement and offering actionable recommendations. By implementing these recommendations, the theme can be made more performant, maintainable, and accessible.

To ensure harmonization between styles and template files and avoid regressions, you should:

1.  **Review the template files:** Carefully examine each template file to understand how it uses CSS classes and styles.
2.  **Update the template files:** If you make any changes to the CSS, update the template files accordingly to ensure that the styles are applied correctly.
3.  **Use consistent naming conventions:** Use consistent naming conventions for CSS classes and IDs in both the CSS files and the template files.
4.  **Test thoroughly:** Test the theme thoroughly after making any changes to the CSS or template files to ensure that there are no visual regressions or inconsistencies.

See [npm Scripts Guide](npm_scripts_guide.md) for instructions on how to execute the tasks that were previously managed by Gulp using npm tools.

See [CSS Styling Guide](css_styling_guide.md) for a bottom-up guide on how to use the CSS architecture in this project, with special attention on how to introduce the changes.