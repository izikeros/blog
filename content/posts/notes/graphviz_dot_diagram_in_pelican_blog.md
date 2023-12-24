---
Title: Using Graphviz (dot) Diagrams in Pelican Blog
Slug: graphviz-dot-diagram-in-pelican-blog
Date: 2023-01-19
Modified: 2023-07-12
Tags: graphviz, visualization, pelican
Category: note
Status: published
Prompt: How can I dynamically generate graphviz diagrams in pelican post written in markdown. How can I have diagram generated if I embed diagram description in dot in code fences (labeled as dot or graphviz)?
---

One way to dynamically generate Graphviz diagrams in a Pelican blog post written in Markdown is to use a plugin that can parse code fences labeled as `dot` or `graphviz` and convert the contents of the code fence into a diagram.

One such plugin is the `pelican-graphviz` plugin, which can be installed via pip and configured in the Pelican settings to automatically generate diagrams from code fences.

Once the plugin is installed and configured, you can include Graphviz diagrams in your blog post by writing the diagram description in the `dot` language within a code fence, and labeling the code fence as `dot` or `graphviz`. The plugin will then automatically convert the description into a diagram and include it in the rendered blog post.

You can also use the pelican-ipynb plugin to execute the code block and include the generated diagram in the post.

X::[[use_mermaid_in_pelican]]
