---
title: 10 Lesser-known, yet powerful python plotting libraries
date: 2023-01-06
modified: 2023-01-06
status: published
tags: python, plotting, visualization, ChatGPT 
slug: lesser-known-yet-powerful-python-plotting-libraries
summary: The most widely used libraries for plotting in python are matplotlib, Plotly, seaborn, and bokeh. This article describes 10 other powerful plotting libraries available in Python that can be used to create high-quality plots and visualizations.
category: Howto
image: /images/head/lesser_known_plotting_libraries.jpg
citation_needed: false
---
There are a few widely used plotting libraries used in python projects: [matplotlib](https://matplotlib.org/), [plotly](https://plotly.com/python/), [seaborn](https://seaborn.pydata.org/) , and [Bokeh](https://docs.bokeh.org/en/latest/index.html). However, the python ecosystem is not limited to these libraries. Many powerful and lesser-known plotting libraries in Python can be used to create high-quality plots and visualizations. 

<!-- MarkdownTOC levels='2,3' autolink=True -->

- [1. HoloViews](#1-holoviews)
- [2. Bqplot](#2-bqplot)
- [3. Plotnine](#3-plotnine)
- [4. Geoplotlib)](#4-geoplotlib)
- [5. Pygal](#5-pygal)
- [6. Vincent](#6-vincent)
- [7. PyNGL](#7-pyngl)
- [8. Ggplot](#8-ggplot)
- [9. PyQtGraph](#9-pyqtgraph)
- [10. PyQwt](#10-pyqwt)
- [Plotly Express](#plotly-express)

<!-- /MarkdownTOC -->

### 1. [HoloViews](https://holoviews.org/) ![GitHub stars shield](https://img.shields.io/github/stars/ioam/holoviews.svg?logo=github)
<img src="https://holoviews.org/_static/logo_horizontal.png" style="max-height: 100px;" alt="HoloViews logo"> 

A library that makes it easy to create and interact with data visualizations in Python, using a high-level interface. The high-level interface refers to the library's ease of use and user-friendly design for creating and interacting with data visualizations in Python. This interface is designed to abstract away some of the complexities of the underlying plotting and data manipulation, making it simpler for users to create and customize their visualizations with minimal code.
By default, HoloViews plots with Bokeh but has extensions for matplotlib and plotly.
[Gallery — HoloViews v1.15.3](https://holoviews.org/gallery/index.html)
[Reference Gallery — HoloViews v1.15.3](https://holoviews.org/reference/index.html)


### 2. [Bqplot](https://github.com/bqplot/bqplot) ![GitHub stars shield](https://img.shields.io/github/stars/bloomberg/bqplot.svg?logo=github)

Bqplot is a Python interactive data visualization library developed by researchers at Bloomberg. This is a 2D data visualization library based on the Jupyter interactive widget framework, which allows you to create interactive plots that can be easily embedded in notebooks.

### 3. [Plotnine](https://plotnine.readthedocs.io/en/stable/)![GitHub stars shield](https://img.shields.io/github/stars/has2k1/plotnine.svg?logo=github)
<img src="https://plotnine.readthedocs.io/en/stable/_images/logo-540.png" style="max-height: 100px;" alt="Plotnine logo"> 

Plotnine is a data visualization library for Python, based on the popular data visualization package ggplot2 for R programming language.

It is designed to mimic the syntax and structure of ggplot2, making it easy for R users to transition to using Python for data visualization. It provides a powerful and flexible way to create plots and charts by using a "grammar of graphics" approach, where the user can build plots by combining different elements such as layers, scales, and geoms.

The library provides a wide range of visualization options and customization capabilities for creating plots and charts, including bar plots, line plots, scatter plots, box plots, heat maps, and many more.

It is built on top of other libraries such as pandas and matplotlib, it allow to make complexe graphics with simple code. Additionally, plotnine supports a variety of input data formats, such as pandas dataframe, numpy arrays, and more. It also supports different types of output formats such as static image files and interactive web-based plots.

In short, plotnine is a great library for creating powerful, flexible, and customizable data visualizations in Python and it is designed for those familiar with R ggplot2 package.

[Gallery — plotnine 0.10.1 documentation](https://plotnine.readthedocs.io/en/stable/gallery.html)

![]() A library for creating interactive web-based plots and dashboards using Plotly, which allows you to create highly customizable and interactive plots.

### 4. [Geoplotlib]([http://www.geoplotlib.org/examples.html](https://github.com/andrea-cuttone/geoplotlib)) ![GitHub stars shield](https://img.shields.io/github/stars/andrea-cuttone/geoplotlib.svg?logo=github)
A library for creating geospatial visualizations, which can be used to create maps, choropleths, and other types of geospatial plots.

### 5. [Pygal](https://www.pygal.org/en/stable/) ![GitHub stars shield](https://img.shields.io/github/stars/Kozea/pygal.svg?logo=github)
Pygal is a library for creating SVG charts and graphs, which provides a wide range of chart types and a simple interface for creating interactive plots.

### 6. [Vincent](https://vincent.readthedocs.io/en/latest/index.html) ![GitHub stars shield](https://img.shields.io/github/stars/wrobstory/vincent.svg?logo=github)
The concept behind this library is:

> The data capabilities of Python. The visualization capabilities of JavaScript.

Vincent allows you to build Vega specifications in a Pythonic way and performs type-checking to help ensure that your specifications are correct. It also has a number of convenience chart-building methods that quickly turn Python data structures into Vega visualization grammar, enabling graphical exploration. It allows for quick iteration of visualization designs via getters and setters on grammar elements, and outputs the final visualization to JSON.

Perhaps most importantly, Vincent has Pandas-Fu, and is built specifically to allow for quick plotting of DataFrames and Series.
[Charts Library — Vincent 0.4 documentation](https://vincent.readthedocs.io/en/latest/charts_library.html)

NOTE: The repository for vincent has been archived by the owner. It is now read-only. There is no active development ongoing on original repo.

### 7. [PyNGL](https://www.pyngl.ucar.edu/Examples/)

A library for creating visualizations of scientific data, which provides a wide range of plotting and visualization options for working with multidimensional data.
[PyNGL Graphical Gallery](https://www.pyngl.ucar.edu/Examples/gallery.shtml)


### 8. [Ggplot](https://ggplot2.tidyverse.org/reference/index.html) ![GitHub stars shield](https://img.shields.io/github/stars/tidyverse/ggplot2.svg?logo=github)

<img src="https://ggplot2.tidyverse.org/logo.png" style="max-height: 100px;" alt="ggplot logo"> 
A library for creating plots using the Grammar of Graphics, which provides a high-level interface for creating a wide range of statistical plots.

### 9. [PyQtGraph](http://www.pyqtgraph.org/documentation/examples.html) ![GitHub stars shield](https://img.shields.io/github/stars/pyqtgraph/pyqtgraph.svg?logo=github)

<img src="https://pyqtgraph.readthedocs.io/en/latest/_static/peegee_02.svg" style="max-height: 100px;" alt="PyQtGraph logo"> 
**PyQtGraph** is a pure-python graphics and GUI library built on [PyQt](http://www.riverbankcomputing.co.uk/software/pyqt/intro) / [PySide](http://www.pyside.org/) and [numpy](http://www.numpy.org/). It is intended for use in mathematics / scientific / engineering applications. Despite being written entirely in python, the library is very fast due to its heavy leverage of NumPy for number crunching and [Qt's GraphicsView framework](https://doc.qt.io/qt-5/qgraphicsview.html) for fast display

### 10. [PyQwt](https://pyqwt.sourceforge.net/)

A library for creating 2D and 3D plots and visualizations, which is built on top of PyQt and provides a wide range of plotting and visualization options.
PyQwt is a set of Python bindings for the [Qwt](http://qwt.sourceforge.net/) C++ class library which extends the [Qt](http://www.trolltech.com/) framework with widgets for scientific and engineering applications. It provides a widget to plot 2-dimensional data and various widgets to display and control bounded or unbounded floating point values.

PyQwt addresses the problem of integrating [PyQt](http://www.riverbankcomputing.co.uk/pyqt), Qt, Qwt, [NumPy](http://numpy.scipy.org/) and optionally [SciPy](http://www.scipy.org/). Look at the [Command Line Interface (CLI) examples](https://pyqwt.sourceforge.net/cli-examples.html) and the [Graphical User Interface (GUI) examples](https://pyqwt.sourceforge.net/gui-examples.html) to get an idea of what you can do with PyQwt.

### [Plotly Express](https://plotly.com/python/plotly-express/) ![GitHub stars shield](https://img.shields.io/github/stars/plotly/plotly_express.svg?logo=github)

<img src="https://images.plot.ly/logo/new-branding/plotly-logomark.png" style="max-height: 100px;" alt="Plotly Express logo"> 
It is not a new plotting library but a high-level interface to Plotly, which allows you to create interactive plots and visualizations with minimal code.
