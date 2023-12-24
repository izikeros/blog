---
Category: note
Date: '2023-02-02'
Modified: '2023-07-12'
Prompt: How to embed markmap mindmap (javascript library) in pelican blog post written in markdown?
Slug: markmap-mindmap-in-pelican-blog
Status: published
Tags: mindmap, mindmapping, diagram, visualization, markmap, pelican
Title: Using Markmap Mindmap Diagrams in Pelican Blog
---



Embedding a markmap mindmap in a Pelican blog post written in Markdown requires a few steps:

1. Install the markmap library by running `npm install -g markmap` in your command line.

2. Create a mindmap file in the `.mm` format using a tool such as [Markmap](https://markmap.js.org/) or [Vim Markmap](https://github.com/dundalek/vim-markmap)

3. Add the following code to the head of your Pelican HTML template:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/markmap@2.4.2/dist/markmap.css" integrity="sha256-f1gjK1a7DwY52ePb7Jf0e9cKd26aOiZaN0Z1zKjH1Dc=" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/markmap@2.4.2/dist/markmap.min.js" integrity="sha256-1Q2bZgxjPf5bW80MvAq3SP1KjGg8Xl1V7vGjKg5V7e0=" crossorigin="anonymous"></script>

```

4. In your Markdown file, add a `div` element where you want the mindmap to appear, and give it an id: `<div id="mindmap"></div>`

5. Add a script to your Markdown file that loads the mindmap file and renders it in the div element:

```html
<script>
    const mindmap = markmap.create('#mindmap', {
        renderer: 'svg',
        openOnClick: true
    });
    mindmap.load('path/to/your/mindmap.mm');
</script>
```

6. Make sure that your `mindmap.mm` file is in the same directory as your pelican project and the path to it is correct.

7. Build and run your Pelican project to see the mindmap in your blog post.

Note that, you could also use a plugin to add the necessary links and script to your HTML template.

Please keep in mind that, Depending on the theme you are using, you might need to make some adjustments to the HTML and CSS to ensure that the mindmap is properly displayed.
