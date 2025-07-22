# Migrating from Gulp to npm Scripts: A Bottom-Up Guide

This document provides a step-by-step guide on how to execute the tasks that were previously managed by Gulp using npm scripts.

## 1. Understanding the Gulp Tasks

First, let's identify the tasks that were being performed by Gulp. Based on the `Gulpfile.js`, these tasks are:

*   **Less Compilation:** Compiling Less files into CSS.
*   **JavaScript Minification:** Minifying JavaScript files.
*   **Font Awesome Copying:** Copying Font Awesome files from `node_modules` to the `static` directory.
*   **Pygments CSS Minification:** Minifying the pygments CSS files.

## 2. Installing Dependencies

Next, we need to install the necessary dependencies for the npm scripts. These dependencies will be installed as development dependencies using the `--save-dev` flag:

*   **terser:** For JavaScript minification.
    ```bash
    npm install terser --save-dev
    ```
*   **copyfiles:** For copying files.
    ```bash
    npm install copyfiles --save-dev
    ```
*   **cssnano:** For CSS minification.
    ```bash
    npm install cssnano --save-dev
    ```

## 3. Configuring npm Scripts

Now, we need to configure the npm scripts in the `package.json` file. Open the `package.json` file and add the following scripts to the `scripts` section:

```json
{
  "scripts": {
    "minify-js": "terser static/dark-theme/dark-theme.js -o static/dark-theme/dark-theme.min.js",
    "copy-fontawesome": "copyfiles -u 1 node_modules/font-awesome/**/* static/font-awesome",
    "minify-pygments": "cssnano static/pygments/*.css --base static/pygments/ --dir static/pygments/ --ext .min.css",
    "build": "npm run minify-js && npm run copy-fontawesome && npm run minify-pygments"
  }
}
```

Let's break down each script:

*   **`minify-js`:** This script uses `terser` to minify the `static/dark-theme/dark-theme.js` file and output the minified file to `static/dark-theme/dark-theme.min.js`.
*   **`copy-fontawesome`:** This script uses `copyfiles` to copy all files from the `node_modules/font-awesome` directory to the `static/font-awesome` directory. The `-u 1` flag tells `copyfiles` to remove the first directory level (`node_modules`).
*   **`minify-pygments`:** This script uses `cssnano` to minify all CSS files in the `static/pygments` directory and output the minified files to the same directory with the `.min.css` extension. The `--base`, `--dir`, and `--ext` flags are used to configure the output path and extension.
*   **`build`:** This script runs all the other scripts in sequence. The `&&` operator ensures that each script is executed only if the previous script was successful.

## 4. Running the npm Scripts

To run the npm scripts, use the `npm run` command followed by the name of the script. For example, to run the `build` script, use the following command:

```bash
npm run build
```

This will execute the `minify-js`, `copy-fontawesome`, and `minify-pygments` scripts in sequence.

## 5. Removing Gulp

Now that we have migrated to npm scripts, we can remove Gulp and its related dependencies. To do this, run the following command:

```bash
npm uninstall gulp gulp-less gulp-rename gulp-uglify
```

This will remove Gulp and its plugins from the `node_modules` directory and update the `package.json` file.

## Conclusion

This document has provided a step-by-step guide on how to migrate from Gulp to npm scripts. By following these steps, you can simplify your frontend build process and reduce dependencies.