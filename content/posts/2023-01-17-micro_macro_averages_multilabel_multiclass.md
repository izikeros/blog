---
Title: Understanding Micro and Macro Averages in Multiclass Multilabel Problems
Slug: micro-and-macro-averages-in-multiclass-multilabel-problems
Date: 2022-12-22
Modified: 2023-01-17
Start: 2023-01-17
Tags: classification, metrics
Category: Machine Learning
Image: /images/head/micro_macro_averaging.jpg
Summary: Learn about micro and macro averages in multiclass multilabel problems, the difference between multiclass and multilabel problems and when to use micro and macro averages.
Status: published
prompt: Give me long, markdown article with hyperlinks and references to learn more about it. Use hyperlinks on crucial terms and tools. Provide mathematical formulas in LaTeX in display format (not inline). Article should be on how to calculate micro/macro averages in case of multiclass multilabel problems. In the end provide also HTML page description for this article (less than 160 characters)
---

When working with multiclass multilabel problems, it's important to understand how to calculate micro and macro averages in order to evaluate the performance of a model. Micro and macro averages provide different perspectives on the performance of a model and are useful in different situations. In this article, we will explore the concepts of micro and macro averages and how to calculate them.

## Multiclass vs Multilabel

Before diving into micro and macro averages, let's first understand the difference between multiclass and multilabel problems.

In a multiclass problem, there is only one correct label per example. For example, in a problem of classifying animals into different categories (e.g. mammals, birds, reptiles, etc.) each example can only have one correct label.

On the other hand, in a multilabel problem, there can be multiple correct labels per example. For example, in a problem of categorizing music into different genres (e.g. rock, pop, hip hop, etc.) an example can belong to multiple genres.

## Micro and Macro Averages

In multiclass multilabel problems, there are two commonly used measures of performance: micro and macro averages.

### Micro Average

Micro average is calculated by taking the total number of true positives (TP), false positives (FP), true negatives (TN), and false negatives (FN) and then using these counts to calculate the precision, recall, and F1-score. Micro average gives more weight to the majority class and is particularly useful when the classes are imbalanced. The formula for calculating micro average is as follows:

$$Precision_{micro} = \frac{\sum_{i=1}^{n} TP_i}{\sum_{i=1}^{n} (TP_i + FP_i)}$$

$$Recall_{micro} = \frac{\sum_{i=1}^{n} TP_i}{\sum_{i=1}^{n} (TP_i + FN_i)}$$

$$F1-score_{micro} = 2 * \frac{Precision_{micro} * Recall_{micro}}{Precision_{micro} + Recall_{micro}}$$

### Macro Average

Macro average, on the other hand, calculates the performance of each class individually and then takes the unweighted mean of the class-wise performance. Macro average gives equal weight to each class and is useful when all classes are of equal importance. The formula for calculating macro average is as follows:

$$Precision_{macro} = \frac{1}{n} \sum_{i=1}^{n} \frac{TP_i}{TP_i + FP_i}$$

$$Recall_{macro} = \frac{1}{n} \sum_{i=1}^{n} \frac{TP_i}{TP_i + FN_i}$$

$$F1-score_{macro} = 2 * \frac{Precision_{macro} * Recall_{macro}}{Precision_{macro} + Recall_{macro}}$$

where n is the number of classes.

It's important to note that in multilabel problems, these metrics are calculated for each label independently and then combined by taking the mean, sum or some other combination.

## Choosing between Micro and Macro averages

The choice between micro and macro averages depends on the specific problem and the desired perspective on the model's performance. Micro averages are useful when the classes are imbalanced and it is important to have a better understanding of the model's performance on the majority class. Macro averages, on the other hand, are useful when all classes are of equal importance and you want to have a better understanding of the model's performance on each class individually.

In some cases, it may be useful to report both micro and macro averages to get a more comprehensive understanding of the model's performance.

It's also important to note that micro and macro averages are not the only metrics to evaluate the performance of a model in multiclass multilabel problems. Other metrics such as ROC-AUC, [Hamming loss](https://en.wikipedia.org/wiki/Multi-label_classification#Statistics_and_evaluation_metrics) and [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) can also be used.

In conclusion, micro and macro averages are important measures of performance in multiclass multilabel problems. They provide different perspectives on the model's performance and should be used depending on the specific problem and desired perspective. It's important to consider the class imbalance and the relative importance of each class when choosing between micro and macro averages.

**Credits:**

Heading image from [Unsplash](https://unsplash.com/photos/pv5SUbgRRIU) by [vackground.com](https://unsplash.com/@vackground)
