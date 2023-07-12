---
Category: note
Date: '2021-10-12'
Modified: '2023-07-12'
Slug: add-logo-to-notebook-header
Status: published
Summary: Instruction on how to add a logo to notebook header cell to strengthen visual identification of the project
Tags: jupyter, howto, notebook, jupyter-notebook, project/logo, visual-identification, logo
Title: Add Logo to Notebook Header Cell
citation_needed: true
todo: add a screenshot with an example
---

Do you want to strengthen the visual identification of your project by adding a logo to the header of your Jupyter notebook? Follow these simple instructions to do so.

At the top of the first markdown cell in your notebook (e.g. the one where you describe your project), add the following HTML code:

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

This code creates two columns in your markdown cell, one for the title of your notebook and the other for your logo. The width of each column is determined by the number following "col-md-". In this case, the first column takes up 8 out of 12 units of width, while the second column takes up 4 out of 12 units. This means that the logo will take up 1/3 of the width of the cell and the title will take up 2/3 of the width. You can change these ratios by adjusting the 8 and 4, just make sure that the sum of the two numbers is always 12.

You will also need to replace "Notebook title" with the actual title of your notebook and `../../gfx/project_logo_150px.jpg` with the file path to your logo. The logo's height can also be adjusted by changing `height=600px` to your desired value.

One thing to keep in mind is that a proper logo file format is `.jpg or .png. If you don't have a logo, you can create one easily with Canva or Adobe Illustrator.

And don't forget to add a screenshot of your notebook with the logo on top, that will help other people to understand the process better.

After following these steps, your Jupyter notebook should now have a stylish and professional-looking logo in the header, making it easy for others to identify your project.

**Credits:**

the example is taken from the website [Have two columns in Markdown](https://newbedev.com/have-two-columns-in-markdown)