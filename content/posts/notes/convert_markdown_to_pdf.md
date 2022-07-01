---
category: note
date: '2022-05-12'
status: published
slug: convert-markdown-to-pdf
tags: conversion, markdown, pdf, pandoc, wkhtmltopdf
title: Convert markdown to pdf
---


## With pagination
convert with pandoc to pdf
```sh
pandoc \
--from=markdown \
--standalone \
--to=pdf \
--pdf-engine=xelatex \
--output=book.pdf \
--metadata title="My booklet"
```

## Without pagination

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
Experiment with page size to impact margins and font size

see: https://blog.scottlowe.org/2018/09/27/a-markdown-to-pdf-workflow-on-linux/

