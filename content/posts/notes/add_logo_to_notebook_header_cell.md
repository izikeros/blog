---
title: Add logo to notebook header cell
date: 2021-10-12
status: published
tags: jupyter, howto, notebook, jupyter-notebook, project, visual-identification, logo
summary: Instruction hot to add logo to notebook header cell to strenghten visual-identification of the project
slug: add-logo-to-notebook-header
category: note
citation_needed: true
todo: add screenshot with example
---

In the top of first markdown cell (e.g. with notebook description) add html code:

```html
<div class="row">
  <div class="col-md-8" markdown="1">
      <h1>Notebook title</h1>
  </div>
  <div class="col-md-4" markdown="1">
      <img height="600px" class="center-block" src="../../gfx/project_logo_150px.jpg">
  </div>
</div>
```
Source: ?

> **NOTE:** replace `Notebook title` and `../../gfx/project_logo_150px.jpg` with your data.