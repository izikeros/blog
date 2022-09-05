---
category: note
date: '2022-05-12'
status: 'published'
slug: convert-pdf-to-image
tags:
- convert
- image
- pdf
title: Convert pdf to image
---

# Convert pdf to image

## install poppler-utils
```
# on Ubuntu, Debian Linux:
sudo apt install poppler-utils

# on macOS
brew install poppler
```

## convert
To convert the entire PDF into PNG format, run the command below. In this case, our PDF file is document.pdf
```sh
pdftoppm -png document.pdf document
```

To convert a range of PDF pages, simply include the `–f N` and `–l N` instructions. Where
- `-f N` stands for the first page to be converted
- `-l N` stands for the last page to be converted.

To convert from page 5 to page 15, run the following command.
```sh
pdftoppm -png -f 5 -l 15 document.pdf document
```

Change the PNG resolution if you want. By default, images will have a DPI of 150. If you're going to increase the resolution, simply include the `–rx` and `–ry` commands. To create an image of 300 DPI, use the code below.
```sh
pdftoppm -png -rx 300 -ry 300 document.pdf document
```

References:
- [Steps to Convert PDF to PNG on Linux](https://pdf.wondershare.com/pdf-knowledge/pdf-to-png-linux.html)