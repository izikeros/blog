---
Title: Using Mermaid Diagrams in Pelican Blog Post
Slug: mermaid-in-pelican-post
Date: 2023-11-28
Modified: 2023-11-28
Status: published
tags:
  - mermaid
  - pelican
  - diagram
  - graph
  - plot
Category: note
---

up::[[MOC_Pelican]]

Sometimes, you might want to embed the mermaid diagram in your blogpost written in markdown. Here is how to do it.

## Embed the HTML code (recommended)

In your markdown file, you can embed HTML code loading mermaid code and initialising it, then include mermaid diagram you want.

```html
<script type="module"> import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs'; mermaid.initialize({ startOnLoad: true }); </script>

Here is a mermaid diagram:
<pre class="mermaid">
 graph TD 
 A[Client] --> B[Load Balancer] 
 B --> C[Server01] 
 B --> D[Server02]
</pre>

```

## Extension

There is extension, not sure if it works:

[Lee-W/md\_mermaid](https://github.com/Lee-W/md_mermaid) - mermaid extension to add support for mermaid graph inside markdown file. NOTE: you need Markdown<3.2 (e.g. 3.1.1)
