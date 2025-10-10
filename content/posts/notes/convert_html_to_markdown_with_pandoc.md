---
Category: note
Date: 2022-08-31
Modified: 2023-07-12
Slug: how-to-convert-html-to-clean-markdown
Status: published
Summary: Instruction on how to convert HTML document to markdown with cleaning the output from the clutter.
Tags:
  - html
  - markdown
  - pandoc
  - conversion
  - cli
  - grep
  - sed
Title: How to Convert HTML to Clean Markdown With Pandoc
citation_needed: false
todo: add a screenshot with an example
---

I have collected source material in form of HTML pages that I would like to keep in one place as knowledge base (technically: create [Obsidian](https://obsidian.md/) vault for these pages). But first I needed to convert them all to Markdown. First tool to use that came into my mind was using [Pandoc](https://pandoc.org/)

I started with basic syntax to check what is my baseline:

```sh
pandoc -i index.html -o index.md
```

The text were converted to markdown but had some additional elements that wish not to see in the output markdown document.

- remaining after div elements, iframes
- references in curly brackets
- raw HTML comments as codefences blocks

Here is an example of the clutter in my Markdown document.

<pre>
::: iframe
:::

::: site-container
::: site-header
::: wrap
::: title-area
[Page Title](../../../index.html)
:::

::: {.widget-area .header-widget-area}
::: {#nav_menu-27 .section .widget .widget_nav_menu}
::: widget-wrap
- [[Articles](../../../blog/index.html)]{#menu-item-2360}
- [[Books ](../../index.html)]{#menu-item-8729}
:::
:::
:::
:::
:::

::: site-inner
::: content-sidebar-wrap
::: {.content role="main"}
::: entry-header

- "Happiness doesn't just flow from success, it actually causes it".

```{=html}
<!-- -->
```
</pre>

Using `--strict, -s` mode adds YAML frontmatter with metadata - which contains few fields that I want to keep.

## My final solution

To remove parts that remained in Markdown document you can use `grep` and `sed`

```sh
pandoc -s -i index.html -t markdown |\
grep -v "^:" |\
grep -v '^```' |\
grep -v '<!-- -->' |\
sed -e ':again' -e N -e '$!b again' -e 's/{[^}]*}//g' \
>! index.md
```

The sed is used to remove content in curly brackets spanning multiple lines:

```
# Linux
sed ':again;$!N;$!b again; s/{[^}]*}//g'

# macOS
sed -e ':again' -e N -e '$!b again' -e 's/{[^}]*}//g' file
```

solution by [John1024](https://unix.stackexchange.com/users/53604/john1024) from: [Linux Stack Exchange](https://unix.stackexchange.com/a/166878/359426)

## Note

You can further experiment with Markdown variants supported by pandoc.

In addition to pandoc’s extended Markdown, the following Markdown variants are supported:

- `markdown_phpextra` (PHP Markdown Extra)
- `markdown_github` (deprecated GitHub-Flavored Markdown)
- `markdown_mmd` (MultiMarkdown)
- `markdown_strict` (Markdown.pl)
- `commonmark` (CommonMark)
- `gfm` (Github-Flavored Markdown)
- `commonmark_x` (CommonMark with many pandoc extensions)

## Beyond pandoc

You can give a try to a dedicated python package for converting HTML to markdown: [markdownify · PyPI](https://pypi.org/project/markdownify/) - it has command line interface and support many options for the conversion.

## See also

[[convert_markdown_to_pdf]]
