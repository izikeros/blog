---
Category: note
Date: 2022-05-12
Modified: 2023-07-12
Slug: convert-markdown-to-pdf
Status: published
Summary: Learn how to convert Markdown documents to PDF using Pandoc, including options for adding a table of contents and alternative PDF engines.
ai_summary: true
Tags:
  - conversion
  - markdown
  - pdf
  - pandoc
  - wkhtmltopdf
  - html
Title: Convert Markdown to PDF
---
X::[[pandoc]]
X::[[writing_book_or_ebook_using_pandoc]]

## Without ToC

convert with [Pandoc](https://pandoc.org/) to PDF

```sh
pandoc \
--from=markdown \
--standalone \
--to=pdf \
--pdf-engine=xelatex \
--output=book.pdf \
--metadata title="My booklet"
```

alternative pdf-engines:
- typst
- pdflatex
- ...


## With ToC

```sh
# convert to HTML
pandoc \
--from=markdown \
--standalone \
--to=html \
--output=book.html \
--metadata title="My book title" \
--toc

# convert to pdf
wkhtmltopdf \
-B 5mm -T 5mm -L 5mm -R 5mm \
-s A5 \
book.html book_html.pdf
```

> **NOTE:** Experiment with page size to impact margins and font size

You can install wkhtmltopdf using brew:
```sh
brew install wkhtmltopdf
```

## See also

- [A Markdown-to-PDF Workflow on Linux - Scott's Weblog - The weblog of an IT pro focusing on cloud computing, Kubernetes, Linux, containers, and networking](https://blog.scottlowe.org/2018/09/27/a-markdown-to-pdf-workflow-on-linux/)
- [[convert_html_to_markdown_with_pandoc]]
