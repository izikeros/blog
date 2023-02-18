---
Title: Libraries for Automated Exploratory Data Analysis (EDA)
Slug: libraries-for-automated-eda
Date: 2023-02-12
Modified: 2023-02-12
Start: 2023-02-12
Tags: python, data-engineering, machine-learning/EDA, data-visualization, exploring, exploratory-data-analysis, data-analysis-process, python-libraries, automated-eda, pandas-profiling, dataprep, sweetviz, lux, dabl, autoviz, klib, explainerdashboard, pycaret, missing-data, feature-engineering, featuretools
Category: Machine Learning
Image: /images/head/auto_eda.jpg
Summary: EDA Made Easy - Discover Top-10 Python Libraries That Will Take Your Data Analysis to the Next Level! Learn the Secrets of Automated EDA!
Status: published
prompt:
todo: replace hotlinking images with local images
---

Exploratory Data Analysis (EDA) is an important step in the data analysis process. It allows us to explore and understand the dataset, identify patterns, and make informed decisions about data cleaning, feature engineering, and modeling. In recent years, several Python libraries have been developed to automate and streamline the EDA process. Here are 10 popular Python libraries for automated EDA:

## Top-10 Tools for Automated EDA

### Pandas Profiling
![github stars shield](https://img.shields.io/github/stars/ydataai/ydata-profiling.svg?logo=github)

[Pandas Profiling](https://github.com/ydataai/ydata-profiling) generates a report with descriptive statistics and visualizations for each variable in a Pandas DataFrame. The report includes correlations, missing values, and data types. 

![pandas-profiling](/images/auto_eda/pandas-profiling.jpg)


### 2.  DataPrep
![github stars shield](https://img.shields.io/github/stars/sfu-db/dataprep.svg?logo=github)

[DataPrep](https://github.com/sfu-db/dataprep) provides a set of functions for data cleaning and preprocessing, including automatic column type detection, outlier detection, and missing value imputation. 

![dataprep](/images/auto_eda/dataprep.jpg)

```sh
pip install dataprep
```

The following code demonstrates how to use `DataPrep.EDA` to create a profile report for the titanic dataset.

``` python
from dataprep.datasets import load_dataset
from dataprep.eda import create_report
df = load_dataset("titanic")
create_report(df).show_browser()
```

### 3.  Sweetviz

![github stars shield](https://img.shields.io/github/stars/fbdesignpro/sweetviz.svg?logo=github)

[Sweetviz](https://github.com/fbdesignpro/sweetviz) generates a report with detailed visualizations and statistical analysis for each variable in a Pandas DataFrame. The report includes comparisons between different subgroups and correlation matrices.

![Sweetviz](https://camo.githubusercontent.com/0965c07124443fe73d4343ebc1642b8b3c68ef49913f32a42c4b6f567a477143/687474703a2f2f636f6f6c74696d696e672e636f6d2f53562f66656174757265732e706e67)

### 4.  Lux

![github stars shield](https://img.shields.io/github/stars/lux-org/lux.svg?logo=github)

[Lux](https://github.com/lux-org/lux) is a library for interactive data visualization that provides a powerful and intuitive interface for exploring and visualizing data. It includes a recommendation system that suggests relevant visualizations based on the current selection. 

![Lux](https://github.com/lux-org/lux-resources/raw/master/readme_img/demohighlight.gif?raw=true)

### 5.  dabl

![github stars shield](https://img.shields.io/github/stars/dabl/dabl.svg?logo=github)

[dabl](https://github.com/dabl/dabl) is a library that provides a set of functions for automated data analysis and machine learning. It includes tools for data cleaning, feature engineering, and modeling, and provides an easy-to-use interface for non-experts. 

![dabl](https://dabl.github.io/dev/_images/sphx_glr_plot_mfeat_factors_005.png)

### 6.  Autoviz

![github stars shield](https://img.shields.io/github/stars/AutoViML/AutoViz.svg?logo=github)

[Autoviz](https://github.com/AutoViML/AutoViz) is a library that automatically generates visualizations for each variable in a Pandas DataFrame. It includes different types of charts such as scatterplots, histograms, and bar charts, and it can be used for both regression and classification tasks. 

![AutoViz](https://github.com/AutoViML/AutoViz/raw/master/var_charts.JPG)
    
### 7.  Klib

![github stars shield](https://img.shields.io/github/stars/akanz1/klib.svg?logo=github)

[Klib](https://github.com/akanz1/klib) is a library that provides a set of functions for data cleaning and preprocessing, including feature selection, missing value imputation, and correlation analysis. It includes useful visualizations and statistical analysis for each variable. 

![Klib](https://raw.githubusercontent.com/akanz1/klib/main/examples/images/header.png)

### 8.  ExplainerDashboard

![github stars shield](https://img.shields.io/github/stars/oegedijk/explainerdashboard.svg?logo=github)

[ExplainerDashboard](https://github.com/oegedijk/explainerdashboard) is a library that provides a dashboard for exploring and visualizing the results of machine learning models. It includes visualizations for feature importance, confusion matrices, and partial dependence plots. 

![ExplainerDashboard](https://github.com/oegedijk/explainerdashboard/raw/master/explainerdashboard.gif)

### 9.  PyCaret

![github stars shield](https://img.shields.io/github/stars/pycaret/pycaret.svg?logo=github)

[PyCaret](https://github.com/pycaret/pycaret) is a library for automated machine learning that includes tools for data preprocessing, feature selection, and model training. It includes a user-friendly interface that allows non-experts to build and deploy machine learning models. 

![PyCaret](https://github.com/pycaret/pycaret/raw/master/docs/images/pycaret_ts_quickdemo.gif)

### Missingno

![github stars shield](https://img.shields.io/github/stars/ResidentMario/missingno.svg?logo=github)

[Missingno](https://github.com/ResidentMario/missingno) is a library that provides a set of tools for **visualizing and understanding missing data in a dataset**. It includes tools for matrix visualization, bar charts, and heatmaps.

![Missingno](https://camo.githubusercontent.com/16475986b81be8268152a4423777683be2d95cdac5d84e70130eb98431959f20/68747470733a2f2f692e696d6775722e636f6d2f675775584b45722e706e67)

## Honorable mentions
There are three other tools that might be useful during data exploration.

## Featuretools

![github stars shield](https://img.shields.io/github/stars/FeatureLabs/featuretools.svg?logo=github)

[Featuretools](https://github.com/FeatureLabs/featuretools) is a library for **automated feature engineering** that allows you to automatically generate features from multiple tables. It includes tools for handling time-based data and can generate a set of feature definitions in just a few lines of code. 

![Featuretools](https://github.com/alteryx/featuretools/raw/main/docs/source/_static/images/entity_set.png?raw=true)

### PyExplainer

![github stars shield](https://img.shields.io/github/stars/awsm-research/pyExplainer.svg?logo=github)

[PyExplainer](https://github.com/awsm-research/pyExplainer) is a library that allows you to easily explain and interpret the results of machine learning models. It includes tools for feature importance, partial dependence plots, and permutation feature importance. 

![PyExplainer](https://github.com/awsm-research/PyExplainer/raw/master/img/pyexplainer_snap_demo.gif)

## References
There is interesting article that features EDA tools:
[Modern Exploratory Data Analysis. Review of 4 libraries for automatic EDA | by ChiefHustler | Towards Data Science](https://towardsdatascience.com/modern-exploratory-data-analysis-29fdbecec957)

It covers:
-   pandas-profiling (python)
-   summarytools (R)
-   explore (R)
-   dataMaid (R)
