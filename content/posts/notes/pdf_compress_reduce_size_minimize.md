---
Category: note
Date: '2023-01-27'
Modified: '2023-07-12'
Slug: pdf-compress-reduce-size-minimize
Status: published
Tags: pdf, ghostscript, pdfminify, compress, publishing
Title: Compress, Reduce or Minimize Size of PDF Document
---
X::[[convert_pdf_to_image]]

## pdfminify

use python package: pdfminify

## ghostscript

```
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress -dNOPAUSE -dQUIET -dBATCH -sOutputFile=compressed_PDF_file.pdf input_PDF_file.pdf
```

In the above command, you should add the correct path of the input and out PDF file.

The command looks scary and confusing. I advise copying and pasting most of it. What you need to know is the `dPDFSETTINGS` parameter. This is what determines the compression level and thus the quality of your compressed PDF file.

**`dPDFSETTINGS`** **description**:

```
/prepress (default) - Higher quality output (300 dpi) but bigger size
/ebook - Medium quality output (150 dpi) with moderate output file size
/screen - Lower quality output (72 dpi) but smallest possible output file size
```

Do keep in mind that some PDF files may not be compressed a lot or at all. Applying compression on some PDF files may even produce a file bigger than the original. There is not much you can do in such cases.

up::[[MOC_content_creation]]
