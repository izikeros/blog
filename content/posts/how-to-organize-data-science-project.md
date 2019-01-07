---
Title: How to organize Data Science project based on Jupyter notebook
Date: '2019-01-05T13:01:34+01:0'
Tags: jupyter, python, notebook
Category: Posts
Image:  /images/books.jpg
Summary: Having several notebook-based projects behind you might result in mess in projects directory. Organize your Data Science project based on Jupyter notebooks in a way that one can navigate through it. Especially that "the one" will be most probably you in few months time. To achieve that: keep your projects directory clean, name the project in a descriptive way and take care of internal structure of the project.
Status: published
---

In this blog post I will share way to organize your Data Science project based on Jupyter notebooks in a way that one can navigate through it. Especially that "the one" will be most probably you in few months time. So be nice for yourselves and organize your project in rational structure rather than spontaneous chaos.

# Problem with finding valuable work you done in the Jupyter notebook in the past
I had few problems like that. In my projects I used to find multiple untitled notebooks such as: `Untitled1.ipynb`, `Untitled2.ipynb`, `Untitled3.ipynb` - that requires extra effort to check out what is inside. Similarly with data: shall this be in `~/datasets` or `~/projects/my_project/datasets`. The need for standardization emerged after creating like dozen of notebook-based projects. Here are lessons learned and solutions worked out for my use cases.

# Rules I try to follow
**Rule #1: Keep your projects directory clean**

This means not to put notebooks directly in your `projects`, `src` directory (or as you call it) but rather keep each project in separate directory in order to have uniform structure and, at projects view level - only one item (directory) per project. This also help when using version control on project-level.
Having this primitive in place, you should be able to get back to valuable pieces of code you done in the past and adopt or reuse it whenever needed. Just don't mix raw data, processed data, images and notebooks in one top level directory and you are 80% done.

**Rule #2: Name the project in a descriptive way**

Use the names in the way that you will be sure which project it is. In case of my side projects I use different names fir different incarnations of the project - when I start attacking the same problem from different angle and starting basically from the scratch.

**Rule #3: Take care of internal structure of the project**
There might be simple project that fits into one notebook and does not require any external files, but if you are doing something more complex e.g. using file with data and preprocessing the data - having well thought structure of the project might pay off. Please note that internal structure of the project depends on the use case. For my practice, I distinguish three use cases:
	* End-to-end individual work. This is typically case of my side projects - if it's interesting enough it might evolve into one of the subsequent categories.
	* Collaborative project. This can be work done for the client and deliverable could be further developed corroboratively to finally land as a product feature in production.
	* Individual work but final notebook shares as result. This can be analysis on demand where notebook report is the deliverable or think of side-project/tutorial that you would like to publish on the blog.

Depending in the use case project directory structure, data directory structure and notebook directory structure might differ but from my experience, for small to medium Data Science projects the structure similar to this should works well:
```
my_project_name/
  ├── 1-preprocessing.ipynb
  ├── 2-analysis.ipynb
  ├── data
  │   ├── interim
  │   ├── processed
  │   └── raw
  └── reports
```

# Specific aspects for different use cases

**End-to-end individual work**

Characteristics:

* short-time activity
* low complexity
* consist of small number of notebooks (fits into single notebook

For longer/bigger projects consider using guidelines from Collaborative Project

If not using version control or not doing small (atomic) commits consider adding changelog cell to track evolution of the notebook.

**Collaborative project**

Consider extracting some mature code into python module that in imported into notebook and take some effort to clean-up and test the code. Take advantage of using modern IDEs such as PyCharm.

Using version control is also highly recommended even if tracing differences in json files (format of Jupyter notebooks) is less convenient when compared to plain source code you will have record of previous versions of notebook.

**Individual work but final notebook shares as result**

Take care of reproducibility - either for yourself if the updates to the outcome document will be needed or for someone else that would like to reproduce your results e.g. when following tutorial you created.

For more complex project setup take look at [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science).

# Additional Tips
**Notebook metadata**

It is useful to include some metadata to the notebook. Here is example borrowed from [pbpython](http://pbpython.com/notebook-process.html):
For that we will need to import `Path` from `pathlib` and `datetime`:
```python
from pathlib import Path
from datetime import datetime
```
Exemplary meta information on time (might indicate last modification) and files used might looks like this:
```python
today = datetime.today()
sales_file = Path.cwd() / "data" / "raw" / "Sales-History.csv"
pipeline_file = Path.cwd() / "data" / "raw" / "pipeline_data.xlsx"
summary_file = Path.cwd() / "data" / "processed" / f"summary_{today:%b-%d-%Y}.pkl"
```

**Use cookiecutter to standardize your projects**

To bootstrap the software projects from template one can use cookiecutter. You can create your template by following short instructions [](). Here is exception from the documentation:

> Cookiecutter takes a source directory tree and copies it into your new project. It replaces all the names that it finds surrounded by templating tags `{{` and `}}` with names that it finds in the file `cookiecutter.json`. That’s basically it.
>
> The replaced names can be file names, directory names, and strings inside files.
