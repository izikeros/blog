---
Title: Tutorial on How to Create new Theme for Pelican Static Site Generator
Slug: create-theme-for-pelican-blog-tutorial
Date: 2022-03-01
Modified: 2022-03-01
Start: 2022-03-01
Tags: pelican, static-site-generator, theme-development, web-development, css, html, templates, site-design, web-design
Category: Howto
Image: /images/head/abstract_1.jpg
Summary: A great Pelican theme can make all the difference. Learn how to design your own with our comprehensive tutorial.
Status: published
prompt: Give me detailed outline of the tutorial on How to create from scratch a new theme for Pelican (Static Site Generator).

---
<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [1.  **Choose a name for your theme**:](#1-choose-a-name-for-your-theme)
- [2.  **Create a new directory for your theme**](#2-create-a-new-directory-for-your-theme)
- [3.  **Create a `templates` directory**](#3-create-a-templates-directory)
- [4.  **Create a base template**](#4-create-a-base-template)
- [5.  **Create a `static` directory**](#5-create-a-static-directory)
- [6.  **Create a `theme.conf` file**](#6-create-a-themeconf-file)
- [7.  **Add CSS to your theme**](#7-add-css-to-your-theme)
- [8.  **Create other templates**](#8-create-other-templates)
- [9.  **Configure your Pelican project**](#9-configure-your-pelican-project)
- [10.  **Test your theme**](#10-test-your-theme)

<!-- /MarkdownTOC -->

<a id="1-choose-a-name-for-your-theme"></a>
## 1.  **Choose a name for your theme**
Choose a name that reflects the design or purpose of your theme. Make sure it's not already taken by another Pelican theme.
    
<a id="2-create-a-new-directory-for-your-theme"></a>
## 2.  **Create a new directory for your theme**
Create a new directory under the `themes` directory in your Pelican project. Use the name you chose in step 1 as the directory name.
    
<a id="3-create-a-templates-directory"></a>
## 3.  **Create a `templates` directory**
Inside your theme directory, create a new directory called `templates`. This is where you'll store all the HTML templates for your theme.
    
<a id="4-create-a-base-template"></a>
## 4.  **Create a base template**
Create a base template for your theme. This template will define the basic structure of all your pages, and will be used as the starting point for all other templates. Here's an example of a simple base template:
    

```html
<!DOCTYPE html>
<html>
    <head>
        <title>{{ page.title }} | {{ site.title }}</title>
    </head>
    <body>
        <header>
            <h1><a href="{{ SITEURL }}">{{ site.title }}</a></h1>
            <nav>
                <ul>
                    <li><a href="{{ SITEURL }}">Home</a></li>
                    {% for category, articles in categories.items() %}
                        <li><a href="{{ SITEURL }}/category/{{ category|slug }}">{{ category }}</a></li>
                    {% endfor %}
                </ul>
            </nav>
        </header>
        <main>
            {% block content %}{% endblock %}
        </main>
        <footer>
            &copy; {{ date.today().year }} {{ site.author }}
        </footer>
    </body>
</html>

```

In this template, `{{ page.title }}` and `{{ site.title }}` will be replaced with the title of the current page and the title of your site, respectively. The `header` section includes a navigation menu that lists all the categories on your site. The `main` section is where the content of each page will go. The `footer` includes your copyright information.

<a id="5-create-a-static-directory"></a>
## 5.  **Create a `static` directory**
Create a new directory called `static` inside your theme directory. This is where you'll store all the static assets (like CSS, images, and JavaScript) for your theme.
    
<a id="6-create-a-themeconf-file"></a>
## 6.  **Create a `theme.conf` file**
Create a new file called `theme.conf` in your theme directory. This file will contain metadata about your theme, like its name, author, and description. Here's an example `theme.conf` file:

```ini
[theme]
name = My New Theme
description = A simple, responsive theme for Pelican
author = Jane Doe

```

<a id="7-add-css-to-your-theme"></a>
## 7.  **Add CSS to your theme**
Create a new file called `style.css` in your `static` directory. This is where you'll define the styles for your theme. Here's an example:

```css
/* Base styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

a {
    color: #0066cc;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* Header styles */
header {
    background-color: #f2f2f2;
    border-bottom: 1px solid #ddd;
    padding: 10px;
}

header h1 {
    margin: 0;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

nav li {
    display: inline-block;
    margin-right: 10px;
}

/* Main styles */

```
In addition to the base styles, you'll also want to add styles specific to your theme's layout and design. For example, if you're creating a blog theme, you might want to style the blog post titles, dates, and tags differently than the rest of the content. Here's an example:

```css
/* Blog post styles */
.post-title {
    font-size: 24px;
    margin-bottom: 10px;
}

.post-date {
    font-style: italic;
    color: #666;
    margin-bottom: 10px;
}

.post-tags {
    margin-bottom: 10px;
}

.post-tags a {
    display: inline-block;
    background-color: #ddd;
    padding: 5px;
    margin-right: 5px;
    color: #333;
    font-size: 12px;
    text-transform: uppercase;
    border-radius: 3px;
}

.post-content {
    line-height: 1.5;
}

/* Sidebar styles */
.sidebar {
    float: right;
    width: 30%;
    margin-left: 20px;
}

.sidebar h2 {
    font-size: 18px;
    margin-bottom: 10px;
}

.sidebar ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.sidebar li {
    margin-bottom: 10px;
}

.sidebar li a {
    color: #0066cc;
    text-decoration: none;
}

.sidebar li a:hover {
    text-decoration: underline;
}

```

<a id="8-create-other-templates"></a>
## 8.  **Create other templates**
Now that you have a base template and some CSS, it's time to create the other templates for your theme. This will include templates for individual pages, blog posts, tags, categories, and any other pages your site might have. Here's an example of a blog post template:

```html
{% extends "base.html" %}

{% block content %}
<article>
    <h1 class="post-title">{{ page.title }}</h1>
    <p class="post-date">{{ page.date.strftime('%B %d, %Y') }}</p>
    <div class="post-tags">
        {% for tag in page.tags %}
            <a href="{{ SITEURL }}/tag/{{ tag|slug }}">{{ tag }}</a>
        {% endfor %}
    </div>
    <div class="post-content">
        {{ page.content }}
    </div>
</article>
{% endblock %}

```

In this template, the `extends` tag tells Pelican to use the `base.html` template as the starting point. The `block content` tag defines where the content of the page should go. The `page.title`, `page.date`, and `page.tags` variables are replaced with the title, date, and tags of the current blog post.

<a id="9-configure-your-pelican-project"></a>
## 9.  **Configure your Pelican project**
Once you've created your new theme, you'll need to configure your Pelican project to use it. In your `pelicanconf.py` file, set the `THEME` variable to the name of your theme directory. For example:

```python
THEME = 'my-new-theme'
```

<a id="10-test-your-theme"></a>
## 10.  **Test your theme**
Finally, test your theme by running `pelican` and generating your site. If everything is working correctly, your new theme should be applied to all the pages on your site.

That's it! By following these steps, you should be able to create a new Pelican theme from scratch. Of course, this is just a basic example, and you can customize your theme further by adding more templates, styles, and features.