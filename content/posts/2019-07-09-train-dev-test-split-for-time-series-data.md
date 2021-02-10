---
title: Train-, Dev-, Test-set split for time series data
started: 2020-02-07
date: '2019-07-09'
tags: machine learning, statistics, probability
Category: 'Data Science'
image: /images/learn_bayes/probab_distrib.png
status: draft
Summary: 4 lines
---
# 



# Problem statement

- approach: go towards desired split in small steps. Start with CV for time series data.



# CV for time series data
## superset approach (sklearn)
![asd](../images/time_series_dev_set/sphx_glr_plot_cv_indices_010.png)
<img style="float: lefts;" src="/images/time_series_dev_set/sphx_glr_plot_cv_indices_010.png" width="25%" height="25%">
  - see: #  https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html
  - 
##  moving window - period fold
[TODO generate analogue plot, create notebook for that purpose]
![asd](../images/time_series_dev_set/sphx_glr_plot_cv_indices_010.png)
<img style="float: lefts;" src="/images/time_series_dev_set/sphx_glr_plot_cv_indices_010.png" width="25%" height="25%">

# Decisions for dev set:
- get samples from train set
- get samples from test set
- set ratio between train, de, and test samples

# Discussion of the options:





Plan for today:
- introduce multiplier
- introduce model optimization


