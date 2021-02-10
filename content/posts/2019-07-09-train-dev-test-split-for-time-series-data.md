---
title: Use bootstraping to evaluate performance of ML model when working on time-series type of data
started: 2021-02-07
date: '2021-02-10'
modified: '2020-02-11'
tags: machine learning, statistics, probability
Category: 'Data Science'
slug: bootstrap-for-time-series-model-performance-assessment
image: /images/time_series_dev_set/bootstrap.png
status: draft
Summary: This post describes challenges with model performance evaluation when working with time-series type of data. Cross-validation is a handy technique that can be used to estimate accuracy of measured model performance scores e.g. by calculating spread of scores for different cross-validation folds. However, for the time-series type of data dedicated types of train-test dataset splits for cross validation needs to be used. This article presents train-tests splits method, inspired by bootstrapping that can be used for efficient model performance estimation.
---
## Prerequisites

This focuses on using bootstrapping to time-series data. There are references to other techniques such as cross-validation, k-fold split, bootstrap method that are not explained in details here. Please use material from references if there is need to familiarize with aforementioned methods.

## Introduction

### Model performance evaluation

For model performance evaluation we typically use *"train"-"test"* split or three-fold split with additional *"validation"* (called also *evaluation* or *"dev"*) set. To allow utilizing more samples for training or determine quality of performance parameter estimation we use cross-validation.

When applying typical cross-validation splits such as K-Fold. to time-series data we can easily introduce bias to our estimation of performance since in case of time series we would like to evaluate performance on the samples that are newer than those in training set. We try to predict future values (regression) or check classification performance on samples that are comes from future from the perspective of the training dataset.

### Bootstrap method for parameter estimation

Often we use sample from larger population to estimate population parameters. E.g. estimate average height of 18 yo folks in given country. When calculating statistics from sample we have point estimates - single number that characterize measured property. We have to keep in back of the head that this number is calculated on the sample. How much this result is dependent on the sample we already taken. How the results will differ if we take different sample. How can we estimate with given confidence (say 95%) what is the range for real value (from whole population). To answer this question statistical method called bootstrap comes with help.

> **Bootstrapping** is any test or metric that uses [random sampling with replacement](https://en.wikipedia.org/wiki/Sampling_(statistics)#Replacement_of_selected_units), and falls under the broader class of [resampling](https://en.wikipedia.org/wiki/Resampling_(statistics)) methods. Bootstrapping assigns measures of accuracy (bias, variance, [confidence intervals](https://en.wikipedia.org/wiki/Confidence_interval), prediction error, etc.) to sample estimates. (source: [wikipedia](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)))

![bootstrap method explained visually](/images/time_series_dev_set/bootstrap.png)

Original Source: [yashuseth.blog](https://yashuseth.blog/2017/12/02/bootstrapping-a-resampling-method-in-statistics/)

### Problem time-series data train-test split

When working with time-series data choice of samples for training and test set should be performed with care to best reflect trends that we want to model (training set) and have element of unknown if we have regression or classification type of problem.

![time series data example - dow john index](/images/time_series_dev_set/time_series_example.png)

### 

There are few methods to approach this problem:

- timeserie split as in scikit-learn
- ref. medium article
- bootstrap-based

## cv- superset approach (sklearn)

With this approach we taking different samples for testing in each train-test set. The weak-point of this approach is that there if very difeerent number of samples taken for the training. These different conditions for the training makes comparability of the resutls from each set questionable.

![time series split from scikit-learn](/images/time_series_dev_set/sphx_glr_plot_cv_indices_010.png)

  - see: #  https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html
##  cv - moving window - period fold

The moving window approach addressed issue with different number of training samples identified in case of previous approach, here however, number of training samples in each set is very limited to allow sweeping the dataset timeline with the train-test window.

[TODO generate analogue plot, create notebook for that purpose]
![moving widow time series split](/images/time_series_dev_set/sphx_glr_plot_cv_indices_010.png)

### cv - bootstrap-based

In this approach we keep test samples following in time the training samples and try to generate different versions of train-test sets for bootstraping.

