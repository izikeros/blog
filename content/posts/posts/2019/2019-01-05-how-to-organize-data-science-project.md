---
Category: Howto
Date: '2019-01-05'
Image: /images/head/books.jpg
Modified: '2023-01-19'
Start: '2019-01-05'
Status: published
Summary: Having several notebook-based projects behind you might result in a mess in the projects directory. Organize your Data Science project based on Jupyter notebooks in a way that one can navigate through it. Especially that "the one" will be most probably you in a few months time. To achieve that, keep your projects directory clean, name the project in a descriptive way and take care of the internal structure of the project.
Tags: jupyter, python, notebook, howto, machine-learning, best-practices, project-management, data-science
Title: How to Organize Data Science Project Based on Jupyter Notebook
banner: "/images/head/books.jpg"
---

In this blog post, I will share the way to organize your Data Science project based on Jupyter notebooks in a way that one can navigate through it. Especially that "the one" will be most probably you in a few months' time. So be nice to yourselves and organize your project in a rational structure rather than spontaneous chaos.

<!-- MarkdownTOC autolink="true" autoanchor="true" -->

- [Problem with finding valuable work you did in the Jupyter notebook in the past](#problem-with-finding-valuable-work-you-did-in-the-jupyter-notebook-in-the-past)
- [Rules I try to follow](#rules-i-try-to-follow)
- [Using version control](#using-version-control)
- [Specific aspects for different use cases](#specific-aspects-for-different-use-cases)
- [Additional Tips](#additional-tips)

<!-- /MarkdownTOC -->

<a id="problem-with-finding-valuable-work-you-did-in-the-jupyter-notebook-in-the-past"></a>

## Problem with finding valuable work you did in the Jupyter notebook in the past

I had a few problems like that. In my projects, I used to find multiple untitled notebooks such as `Untitled1.ipynb`, `Untitled2.ipynb`, `Untitled3.ipynb` - that requires extra effort to check out what is inside. Similarly, with data: shall this be in `~/datasets` or `~/projects/my_project/datasets`. The need for standardization emerged after creating like dozen of notebook-based projects. Here are lessons learned and solutions worked out for my use cases.

<a id="rules-i-try-to-follow"></a>

## Rules I try to follow

**Rule #1: Keep your projects' directory clean**

This means not to put notebooks directly in your `projects`, `src` directory (or as you call it) but rather keep each project in a separate directory in order to have a uniform structure and, at the projects view level - only one item (directory) per project. This also helps when using version control on the project level.
Having this primitive in place, you should be able to get back to valuable pieces of code you have done in the past and adopt or reuse them whenever needed. Just don't mix raw data, processed data, images, and notebooks in one top-level directory, and you are 80% done.

**Rule #2: Name the project in a descriptive way**

Use the names in a way that you will be sure which project it is. In the case of my side projects, I use different names for different incarnations of the project - when I start attacking the same problem from a different angle and starting basically from the scratch.

**Rule #3: Take care of the internal structure of the project**
There might be a simple project that fits into one notebook and does not require any external files, but if you are doing something more complex e.g. using files with data and preprocessing the data - having well-thought structure of the project might pay off. Please note that the internal structure of the project depends on the use case. For my practice, I distinguish three use cases:

- **End-to-end individual work**
This is a typical case of my side projects - if it is interesting enough it might evolve into one of the subsequent categories.
Example: A data scientist working on a personal project to analyze customer data from a retail store. This project would likely be short-term, have low complexity, and could be completed using a single Jupyter notebook.
 
- **Collaborative project**
This can be work done for the client and deliverable could be further developed collaboratively to finally land as a product feature in production.
Example: A team of data scientists working on a project for a client to predict customer churn. This project would likely be of medium complexity, involve multiple Jupyter notebooks, and require collaboration among team members. The project may also require extracting some mature code into a python module that is imported into a notebook.
 
- **Individual work but final notebook shares as result**
This can be the analysis on-demand where a notebook report is a deliverable or think of a side-project/tutorial that you would like to publish on the blog.
Example: A data scientist working on an analysis on demand for a company's management team. The analysis would be done in a Jupyter notebook, and the final report would be shared with the management team.

- **Production-ready projects**
Example: A data scientist working on a project to build a recommendation engine for a streaming service. This project would likely be of high complexity, involve multiple Jupyter notebooks, and require extracting code into a python module that is imported into a notebook. Additionally, the final model would need to be deployed in a production environment.

5. **Research projects**
Example: A data scientist working on a project to develop a new machine learning algorithm. This project would likely involve a lot of experimentation and iteration, and the final results would be shared in a research paper or conference presentation.

Depending on the use case project directory structure, data directory structure, and notebook directory structure might differ but from my experience, for small to medium Data Science projects a structure similar to this should work well:

```text
my_project_name/
  ├── 1-preprocessing.ipynb
  ├── 2-analysis.ipynb
  ├── data
  │   ├── interim
  │   ├── processed
  │   └── raw
  └── reports
```

<a id="using-version-control"></a>

## Using version control

The use of version control tools like Git to manage and track changes in the project over time is a standard in software projects. However, data science project has its own specificity related to the fact that:

- data is a part of the project
- Jupyter notebooks are typically stored as in JSON format and can contain output that can cause problems in reviewing the changes in the notebook.
Using version control in the Data Science project is a topic for a separate article.

<a id="specific-aspects-for-different-use-cases"></a>

## Specific aspects for different use cases

**End-to-end individual work**

Characteristics:

- short-time activity
- low complexity
- consist of a small number of notebooks (fits into a single notebook)

For longer/bigger projects consider using guidelines from Collaborative Project

If not using version control or not doing small (atomic) commits consider adding a changelog cell to track the evolution of the notebook.

**Collaborative project**

Consider extracting some mature code into a python module that is imported into a notebook and take some effort to clean up and test the code. Take advantage of using modern IDEs such as PyCharm.

Using version control is also highly recommended even if tracing differences in JSON files (format of Jupyter notebooks) is less convenient when compared to plain source code you will have a record of previous versions of the notebook.

**Individual work but final notebook shares as a result**

Take care of reproducibility - either for yourself if the updates to the outcome document will be needed or for someone else that would like to reproduce your results e.g. when following the tutorial you created.

For a more complex project setup take look at [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science).

<a id="additional-tips"></a>

## Additional Tips

**Notebook metadata**

It is useful to include some metadata in the notebook. Here is an example borrowed from [pbpython](http://pbpython.com/notebook-process.html):
For that we will need to import `Path` from `pathlib` and `datetime`:

```python
from pathlib import Path
from datetime import datetime
```

Exemplary meta information on time (might indicate last modification) and files used might look like this:

```python
today = datetime.today()
sales_file = Path.cwd() / "data" / "raw" / "Sales-History.csv"
pipeline_file = Path.cwd() / "data" / "raw" / "pipeline_data.xlsx"
summary_file = Path.cwd() / "data" / "processed" / f"summary_{today:%b-%d-%Y}.pkl"
```

**Use cookiecutter to standardize your projects**

To bootstrap the software projects from a template one can use cookiecutter. You can create your template by following short instructions [](). Here is an exception from the documentation:

> Cookiecutter takes a source directory tree and copies it into your new project. It replaces all the names that it finds surrounded by templating tags `{{` and `}}` with names that it finds in the file `cookiecutter.json`. That’s basically it.
>
> The replaced names can be file names, directory names, and strings inside files.

X::[[2023-02-13-how_to_organize_datascience_project]]
X::[[competitive_data_science_project]]
X::[[MOC_Python_Project]]

See also:

- [[2023-01-19-common_types_of_data_science_projects|Common Types of Data Science Projects]]

*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*
