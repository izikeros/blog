---
Title: Kaggle evaluation metrics used for regression problems
Date: 2019-02-16
Start: 2019-02-05
Modified: 2019-03-01
Tags: machine learning, evaluation, metrics, model performance evaluation, Kaggle
Category: Data Science
Image: /images/head/performance_metrics.jpg
Summary: This post describe evaluation metrics used in Kaggle competitions where problem to solve is has regression nature. Eight different metrics are described, namely: Absolute Error (AE), Mean Absolute Error (MAE), Weighted Mean Absolute Error (WMAE), Pearson Correlation Coefficient, Spearman’s Rank Correlation, Root Mean Squared Error (RMSE), Root Mean Squared Logarithmic Error (RMSLE), Mean Columnwise Root Mean Squared Error (MCRMSE).
Status: published
---

While crafting machine learning model there is always need to asses its performance. When trying multiple models or hyper parameter tuning it is useful to compare different approaches and choose the best one. The [sklearn.metrics](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics) provides plethora of metrics for suitable for distinct purposes.

In this series of posts I will discuss four groups of common machine learning tasks each requires specific metrics:

1. *Regression* - predict value of one or more variables that are continuous, e.g. predict stock price of given asset or predict temperature for next day.
2. *Binary classification* - assign sample to one of two classes - example: classify image as one containing "cat" or "dog"
3. *Multiple class classification* - assign sample to one of many classes example: classify new article to category "sport", "politics", "economy", "pop-culture",...
4. *Other*

The [Kaggle competitions](https://www.kaggle.com/competitions) give insight into approach taken by Kaggle team to select best evaluation metrics for given task. There use to be Kaggle wiki under containing short definitions of metrics used in Kaggle competitions but it is not available anymore. In this post we will look closer at the first group and explain few model evaluation metrics used in regression problems. Here metrics that are discussed in this post.

<!-- MarkdownTOC autolink="true" autoanchor="true" -->

- [Absolute Error - AE](#absolute-error---ae)
- [Mean Absolute Error - MAE](#mean-absolute-error---mae)
- [Weighted Mean Absolute Error - WMAE](#weighted-mean-absolute-error---wmae)
- [Pearson Correlation Coefficient](#pearson-correlation-coefficient)
- [Spearman’s Rank Correlation](#spearman%E2%80%99s-rank-correlation)
- [Root Mean Squared Error - RMSE](#root-mean-squared-error---rmse)
- [Root Mean Squared Logarithmic Error - RMSLE](#root-mean-squared-logarithmic-error---rmsle)
- [Mean Columnwise Root Mean Squared Error - MCRMSE](#mean-columnwise-root-mean-squared-error---mcrmse)
- [References](#references)

<!-- /MarkdownTOC -->



<a id="absolute-error---ae"></a>
## Absolute Error - AE

**The sum of the absolute value of each individual error.**
$$
\mathrm{AE} = \sum_{i=1}^n | y_i - \hat{y}_i |
$$

Where:

$\mathrm{AE} = |e_i| = |y_i-\hat{y_i}|$,

$n$ - number test of samples,

$y_i$ - actual variable value, 

$\hat{y}_i$ - predicted variable value.

MAE can cause notable difference between public and private leaderboard calculations. One drawback of the Absolute Error metrics is that direct comparison of the metrics for model used to predict variables on different scales is not possible. E.g. when using model to financial predictions of S&P 500 index and using the same model to predict value of Microsoft stock price we cannot compare their performance using this metrics since units and ranges are different. The S&P 500 is expressed in points and stock price of asset is expressed in dollars. In this situation one can use (percentage error) to get evaluation metrics in common scale.

Exemplary competition using Mean Absolute Error for model evaluation:

- [Forecast Eurovision Voting](https://www.kaggle.com/c/Eurovision2010#Evaluation) - This competition requires contestants to forecast the voting for this year's Eurovision Song Contest in Norway on May 25th, 27th and 29th.

<a id="mean-absolute-error---mae"></a>
## Mean Absolute Error - MAE
**Mean of the absolute value of each individual error.**

The mean absolute error (MAE) is a quantity used to measure how close forecasts or predictions are to the eventual outcomes. The mean absolute error is given by formula:

$$
\mathrm{MAE} = \frac{1}{n}\sum_{i=1}^n \left| y_i - \hat{y_i}\right| =\frac{1}{n}\sum_{i=1}^n \left| e_i \right|.
$$

Where:

$n$ - number test of samples,

$y_i$ - actual variable value, 

$\hat{y}_i$ - predicted variable value.

see also [paper](http://climate.geog.udel.edu/~climate/publication_html/Pdf/WM_CR_05.pdf): Advantages of the mean absolute error (MAE) over the root mean square error (RMSE) in assessing average model performance

Five exemplary competitions using Mean Absolute Error for model evaluation:

- [LANL Earthquake Prediction](https://www.kaggle.com/c/LANL-Earthquake-Prediction#evaluation) - Can you predict upcoming laboratory earthquakes?

* [PUBG Finish Placement Prediction](https://www.kaggle.com/c/pubg-finish-placement-prediction#evaluation) - Can you predict the battle royale finish of PUBG Players?

* [Allstate Claims Severity](https://www.kaggle.com/c/allstate-claims-severity#evaluation) - How severe is an insurance claim? 

* [Loan Default Prediction - Imperial College London](https://www.kaggle.com/c/loan-default-prediction#evaluation) - Constructing an optimal portfolio of loans.

* [Finding Elo](https://www.kaggle.com/c/finding-elo#evaluation) - Predict a chess player's FIDE Elo rating from one game.

<a id="weighted-mean-absolute-error---wmae"></a>
## Weighted Mean Absolute Error - WMAE
**Weighted average of absolute errors.**

WMAE can be used as evaluation tool for better assessing the model performance with respect to the goals of the application. For example, in the case of recommending books or movies it could be possible that the accuracy of the predictions varies when focusing on past or recent products. In this situation, it is not reasonable that every error were treated equally, so more stress should be put in recent items.

WMAE can be also useful as a diagnosis tool that, using a "magnifying lens", can help to identify those cases where an algorithm is having trouble with. The formula for calculating WMAE is:

$$
\textrm{WMAE} = \frac{1}{n} \sum_{i=1}^n w_i | y_i - \hat{y}_i |,
$$

where:

$n$ - number test of samples,

$w_i$ - weights for sample $i$,

$y_i$ - actual variable value,

$\hat{y}_i$ - predicted variable value.

Two exemplary competitions using Weighted Mean Absolute Error for model evaluation:

* [The Winton Stock Market Challenge](https://www.kaggle.com/c/the-winton-stock-market-challenge#evaluation) - Join a multi-disciplinary team of research scientists.

* [Walmart Recruiting - Store Sales Forecasting](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting#evaluation) - Use historical markdown data to predict store sales.

<a id="pearson-correlation-coefficient"></a>
## Pearson Correlation Coefficient
**Covariance of the two variables divided by the product of the standard deviation of each data sample.**

It is the normalization of the covariance between the two variables to give an interpretable score. The Pearson correlation coefficient can be used to summarize the strength of the linear relationship between two data samples. The formula for calculating Pearson correlation coefficient is:

$$
p = \frac{cov(y_i, \hat{y}_i)}{std(y_i)  std(\hat{y}_i)}
$$

where:

$cov()$ - is covariation function,

$std()$ - is standard deviation

$y_i$ - actual variable value, 

$\hat{y}_i$ - predicted variable value

$p$ - Pearson correlation coefficient.

The use of mean and standard deviation in the calculation requires data samples to have a Gaussian or Gaussian-like distribution.

Exemplary competition using Pearson Correlation Coefficient for model evaluation:

* [Merck Molecular Activity Challenge](https://www.kaggle.com/c/MerckActivity#evaluation) - Help develop safe and effective medicines by predicting molecular activity.

<a id="spearman%E2%80%99s-rank-correlation"></a>
## Spearman’s Rank Correlation
**Covariance of the two variables converted to ranks divided by the product of the standard deviation of ranks for each variable.**

Two variables may be related by a nonlinear relationship, such that the relationship is stronger or weaker across the distribution of the variables. The two variables being considered may have a non-Gaussian distribution.

The Spearman’s correlation coefficient can be used to summarize the nonlinear relation between the two data samples. Raw scores $y_i$ and $\hat{y}_i$ are converted to ranks respectively: $ry_i$ and $\hat{ry}_i$. The formula for calculating Spearman's rank correlation coefficient is:

$$
r=\frac{cov(ry_i, \hat{ry}_i)}{std(ry_i)std(\hat{ry}_i)}
$$

where:

$cov()$ - is covariation function,

$std()$ - is standard deviation,

$ry_i$ - rank of variable value, 

$\hat{ry}_i$ - rank of predicted variable value,

$r$ - Spearman's correlation coefficient.

Exemplary competition using Spearman’s Rank Correlation for model evaluation:

* Draper Satellite Image Chronology](https://www.kaggle.com/c/draper-satellite-image-chronology#evaluation) - Can you put order to space and time?

<a id="root-mean-squared-error---rmse"></a>
## Root Mean Squared Error - RMSE
**The square root of the mean/average of the square of all of the error.**

The use of RMSE is very common and it makes an excellent general purpose error metric for numerical predictions. Compared to the similar Mean Absolute Error, RMSE amplifies and severely punishes large errors. The formula for calculating RMSE is:

$$
\mathrm{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$

where:

$n$ - number test of samples,

$y_i$ - actual variable value, 

$\hat{y}_i$ - predicted variable value.

Five exemplary competition using Root Mean Squared Error for model evaluation:

* [Elo Merchant Category Recommendation](https://www.kaggle.com/c/elo-merchant-category-recommendation#evaluation) - Help understand customer loyalty.

* [Google Analytics Customer Revenue Prediction](https://www.kaggle.com/c/ga-customer-revenue-prediction#evaluation) - Predict how much GStore customers will spend.

* [House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques#evaluation) - Predict sales prices and practice feature engineering, RFs, and gradient boosting.

* [Predict Future Sales](https://www.kaggle.com/c/competitive-data-science-predict-future-sales#evaluation) - Final project for "How to win a data science competition" Coursera course.

* [New York City Taxi Fare Prediction](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction#evaluation) - Can you predict a rider's taxi fare?


<a id="root-mean-squared-logarithmic-error---rmsle"></a>
## Root Mean Squared Logarithmic Error - RMSLE
**Root mean squared error of variables transformed to logarithmic scale**.
$$
\mathrm{RMSLE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(log(\hat{y}_i + 1) - log(y_i + 1))^2}
$$

Where:

$n$ - number of test samples,

$\hat{y}_i$ is the predicted variable,

$y_i$ is the actual variable,

$log(x)$ is the natural logarithm of $x$.

The RMSLE is higher when the discrepancies between predicted and actual values are larger. Compared to Root Mean Squared Error (RMSE), RMSLE does not heavily penalize huge discrepancies between the predicted and actual values when both values are huge. In this cases only the percentage differences matter (difference of variable logarithms is equivalent to ratio of variables).

Exemplary competition using Root Mean Squared Logarithmic Error for model evaluation:

* [Santander Value Prediction Challenge](https://www.kaggle.com/c/santander-value-prediction-challenge#evaluation) - Predict the value of transactions for potential customers.

* [Mercari Price Suggestion Challenge](https://www.kaggle.com/c/mercari-price-suggestion-challenge#evaluation) - Can you automatically suggest product prices to online sellers?

* [Recruit Restaurant Visitor Forecasting](https://www.kaggle.com/c/recruit-restaurant-visitor-forecasting#evaluation) - Predict how many future visitors a restaurant will receive

* [New York City Taxi Trip Duration](https://www.kaggle.com/c/nyc-taxi-trip-duration#evaluation) - Share code and data to improve ride time predictions

* [Sberbank Russian Housing Market](https://www.kaggle.com/c/sberbank-russian-housing-market#evaluation) - Can you predict realty price fluctuations in Russia’s volatile economy?

<a id="mean-columnwise-root-mean-squared-error---mcrmse"></a>
## Mean Columnwise Root Mean Squared Error - MCRMSE
**Errors of each k-fold CV trials were averaged over n test samples across m target variables.**
$$
MCRMSE = \frac{1}{m}\sum_{j=1}^{m}\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_
{ij}-\hat{y}_{ij})^2}
$$
Note that expression under square root is RMSE, thus we can write:
$$
MCRMSE = \frac{1}{m}\sum_{j=1}^{m}RMSE_j
$$

Where:

$m$ - number of predicted variables,

$n$ - number of test samples,

$y_{ij}$ - $i$-th actual value of $j$-th variable,

$\hat{y}_{ij}$ - $i$-th predicted value of $j$-th variable.

Exemplary competition using Mean Columnwise Root Mean Squared Error for model evaluation:

- [Africa Soil Property Prediction Challenge](https://www.kaggle.com/c/afsis-soil-properties#evaluation) - Predict physical and chemical properties of soil using spectral measurements

<a id="references"></a>
## References
1. [Kaggle wiki](archive.org)
2. [Beating Kaggle the easy way, page 43](https://www.ke.tu-darmstadt.de/lehre/arbeiten/studien/2015/Dong_Ying.pdf)
3. [How to Use Correlation to Understand the Relationship Between Variables](https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/)
4. [Mean Columnwise Root Mean Squared Error - google books](https://books.google.pl/books?id=bsEDCwAAQBAJ&pg=PA23&lpg=PA23&dq=%22Mean+Column+Wise+Root+Mean+Squared+Error%22&source=bl&ots=CXTjTNgehR&sig=ACfU3U0Jsn7QkzFecjR-EQC5mtD9p_lBCA&hl=en&sa=X&ved=2ahUKEwjAqYPixa_gAhXF8qYKHeGrDbYQ6AEwBXoECAAQAQ#v=onepage&q=%22Mean%20Column%20Wise%20Root%20Mean%20Squared%20Error%22&f=false)
5. [Metrics to Understand Regression Models in Plain English: Part 1](https://towardsdatascience.com/metrics-to-understand-regression-models-in-plain-english-part-1-c902b2f4156f)



*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*