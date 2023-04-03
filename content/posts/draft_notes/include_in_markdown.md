---
Title: Markdown - include a file
Slug: markdown-include
Date: 2023-01-31
Modified: 2023-01-31
Status: draft
Tags: markdown, content-creation, publishing, book/writing 
Category: note
prompt: what are the methods to include file contents in markdown documents (like LaTeX \include{} command). Are there any markdown extensions or markdown supersets that allows including?
---
up:[[markdown]]
#blog/post-idea 

Including file contents in Markdown documents can be achieved using a few methods. Here are some of the ways you can include file contents in Markdown:

1.  Using shell scripts or Makefiles: You can write a shell script or Makefile to concatenate the contents of multiple Markdown files into a single file, which can then be processed by Pandoc. This method is useful for large, complex documents, where it's easier to manage the content as separate files.
    
2.  Pandoc file inclusion: Pandoc provides a way to include file contents directly in a Markdown file using the `include` directive. For example:
    



`# Main document  This is the main document.  ```{include=Chapter1.md}`

## Stack overflow
- https://stackoverflow.com/questions/4779582/markdown-and-including-multiple-files/
	- repo with pandoc example: https://github.com/izikeros/markdown-multiple-files-example (I forked it already)
	- **NOTE: This post has many views - write article on that**
	
- https://stackoverflow.com/questions/41238290/include-markdown-inside-markdown


## Markdown Preprocessor ([MarkdownPP](https://github.com/jreese/markdown-pp)).

## pandoc + includes.txt


## [Multimarkdown](http://fletcherpenney.net/multimarkdown/) has this natively. It calls it [file transclusion](https://fletcher.github.io/MultiMarkdown-5/transclusion.html):