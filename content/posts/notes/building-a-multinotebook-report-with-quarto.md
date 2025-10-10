---
Title: Building a Multi-Notebook Report with Quarto
Slug: building-a-multinotebook-report-with-quarto
Date: 2025-07-23
Modified: 2025-07-23
Status: published
Tags:
  - quarto
  - jupyter-notebooks
  - nbconvert
  - reporting
  - experiment-management
  - research
  - research-report
Category: note
---

Over the past few months, I’ve been using Jupyter notebooks to explore and document various data analysis tasks. At some point, I realized I wanted to share the results in a more polished way, so I used quarto to generate report. Over the time analysis notebook has grown to the monster size. I wanted to split it into multiple notebooks, each focusing on a specific aspect of the analysis. But I also wanted to combine them into a single cohesive report.
Something that reads like a real report. I didn't want to just dump a bunch of disconnected notebooks on someone.

That’s where **Quarto** with book project functionality came in. In this post, I’ll show you two practical ways to combine multiple notebooks into a single, unified report using Quarto:

- **Option 1:** Turn your notebooks into a structured book (like GitBook)
- **Option 2:** Embed notebooks into a single `.qmd` file

Both methods let you keep your notebooks clean and modular while generating a polished report that looks great in HTML, PDF, or even EPUB formats.

## Option 1: Create a Book-Like Report with Quarto

This is the approach I went with for a larger project. It gives you a navigation sidebar, automatic chapter numbering, and multiple output formats. Think of it as building a small website or PDF book.

### Step 1: Install Quarto

If you haven’t installed Quarto yet:

```bash
# On macOS/Linux
brew install quarto

# Or download manually
https://quarto.org/docs/get-started/
```

Make sure Jupyter is also installed and working.

### Step 2: Create a New Book Project

Let’s set up the project:

```bash
quarto create project book my-report
cd my-report
```

You’ll now see a few files and folders:

```
my-report/
├── _quarto.yml
├── index.qmd
├── intro.qmd
└── references.qmd
```

This is your basic structure. You can remove `intro.qmd` or rename it. For now, we’ll leave it.

> **NOTE**: you can use vscode quarto extensions and start project from vscode as described in Quick Start in [documentation](https://quarto.org/docs/books/).


### Step 3: Add Your Notebooks

Drop your notebooks into the folder. For example:

```
my-report/
├── chapter1.ipynb
├── chapter2.ipynb
├── conclusion.ipynb
```

You can keep working in Jupyter as usual.

> **NOTE**: I encourage you to read about structuring your "book" in the official docs [here](https://quarto.org/docs/books/book-structure.html). There are many other options than chapter: book parts, appendices 

### Step 4: Configure `_quarto.yml`

This is where the magic happens. You define the structure of your report here:

```yaml
project:
  type: book

book:
  title: "My Analysis Report"
  author: "Your Name"
  chapters:
    - index.qmd
    - chapter1.ipynb
    - chapter2.ipynb
    - conclusion.ipynb

format:
  html:
    toc: true
  pdf:
    toc: true
    documentclass: book
```

Make sure the filenames match your actual notebooks. You can mix `.qmd` and `.ipynb` files freely.

Each "chapter" notebook can have its own quarto front matter (YAML header) if you want to customize titles, authors, or other metadata.

> **NOTE**: The official documentation describes many options for customizing style, layout, controls, social media sharing options. Check it out [here](https://quarto.org/docs/books/book-output.html).

### Step 5: Preview Your Report

To preview as you work:

```bash
quarto preview
```

This starts a live-reloading web server at `http://localhost:4200`.

When you’re ready to render:

```bash
quarto render
```

This generates the output in `_book/` (for HTML) and optionally `.pdf` or `.epub` depending on your formats.

## Option 2: One `.qmd` File That Embeds Notebooks

Sometimes you want to pick and choose what parts of your notebooks go into a report. Or maybe you want to glue them together with a lot of custom narrative. That’s where embedding comes in.

Instead of building a whole book, you write one `.qmd` file and embed specific cells or whole notebooks into it.

### Step 1: Create a New Quarto Project

This time we’ll use a regular document project:

```bash
quarto create project article embedded-report
cd embedded-report
```

Your structure will look like:

```
embedded-report/
├── _quarto.yml
└── report.qmd
```

You can drop your notebooks here too:

```
embedded-report/
├── notebook_a.ipynb
├── notebook_b.ipynb
```

### Step 2: Write the Report with Embeds

Edit `report.qmd` like this:

````markdown
---
title: "Combined Report"
format: html
execute:
  enabled: false
---

# Introduction

This is a combined report from two notebooks.

# Results from Notebook A

```{=embed}
notebook_a.ipynb
````

# Specific Figure from Notebook B

```{=embed}
notebook_b.ipynb#cell-3
```

# Full Notebook B

```{=embed}
notebook_b.ipynb
```

You can embed the whole notebook or reference individual cells by their labels or indices. If you want to embed only specific cells, give them labels in Jupyter using `#| label: my-cell`.

### Step 3: Render It

```bash
quarto render
```

You’ll get a clean report with selected content pulled from your notebooks. You can even combine this approach with more Markdown narrative, custom styling, and conditional content.

## Summary

Both methods have their strengths:

- The **Quarto Book** approach is great when you want a navigable multi-chapter report or site. It’s structured, scalable, and looks professional out of the box.
- The **embedding approach** gives you more flexibility when curating content or writing more detailed commentary around selected outputs.

I personally use the book format for larger projects, and embedding for quick curated reports. With both approaches, notebooks stay clean and modular — and reports look great with just a few lines of configuration.

## Alternative tools
## Additional tools (optional)

- **Mercury**: converts notebooks into interactive web apps, with widgets, hideable code, etc. More suited for dashboards rather than structured multi-notebook books. [Quarto+1Reddit+1](https://quarto.org/docs/books/?utm_source=chatgpt.com)[Reddit+15Reddit+15Quarto+15](https://www.reddit.com/r/Python/comments/s7ngj0?utm_source=chatgpt.com)[Quarto+6csoneson.github.io+6jumpingrivers.com+6](https://csoneson.github.io/ReproduciblePublishing2024/IntroToQuarto/quarto.html?utm_source=chatgpt.com)[blog.adyog.com](https://blog.adyog.com/2025/02/15/quarto-convert-jupyter-notebooks-into-professional-reports-websites-and-dashboards/?utm_source=chatgpt.com)[Reddit+2jumpingrivers.com+2Medium+2](https://www.jumpingrivers.com/blog/reproducible-reports-jupyter-quarto-python/?utm_source=chatgpt.com)[GitHub+1Quarto+1](https://github.com/RobertsLab/resources/discussions/1719?utm_source=chatgpt.com)[Reddit+4Reddit+4Reddit+4](https://www.reddit.com/r/Python/comments/11tp5fa?utm_source=chatgpt.com)
    
- **Pretty Jupyter**: a tool for styling notebook outputs into elegant self‑contained HTML—less structured than Quarto “books”, but quick and visually appealing. [Reddit+2Reddit+2Reddit+2](https://www.reddit.com/r/MachineLearning/comments/w9ec2e?utm_source=chatgpt.com)
- 
## References
- [Creating a Book – Quarto](https://quarto.org/docs/books/) - official documentation for quarto books
- [Python for Data Analysis, 3E](https://wesmckinney.com/book/) - exemplary book created with Quarto