---
title: What is the difference between Matthews correlation coefficient and F1 metrics
date: 2023-01-05
modified: 2023-01-05
status: published
tags: machine-learning, classification, metrics
summary: Description of the difference between Matthews correlation coefficient and F1
category: note
citation_needed: false
---

The Matthews correlation coefficient (MCC) is a measure of the quality of binary classifications, while the F1 score is a measure of the overall performance of a classification model. Here is a comparison of the two metrics:

-   **Matthews correlation coefficient**: The MCC is a measure of the correlation between the predicted class labels and the true class labels. It takes into account true and false positives and negatives and is therefore more balanced than other metrics such as accuracy or precision. The MCC is defined as:

$$
MCC = \frac{(TP * TN - FP * FN)}{\sqrt{(TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)}}
$$

where TP is the number of true positives, TN is the number of true negatives, FP is the number of false positives, and FN is the number of false negatives. The MCC ranges from -1 to 1, where 1 is a perfect classification, 0 is no better than random guessing, and -1 is a completely wrong classification.

-   **F1 score**: The F1 score is a measure of a classification model's overall performance, taking into account both precision and recall. It is defined as the harmonic mean of precision and recall, where precision is the ratio of true positives to (true positives + false positives) and recall is the ratio of true positives to (true positives + false negatives). The F1 score is defined as:
$$
F1 = 2 * \frac{precision * recall}{precision + recall}
$$
The F1 score ranges from 0 to 1, where 1 is a perfect classification and 0 is a completely wrong classification.

In summary, the MCC is a metric that measures the quality of binary classifications, taking into account all four possible outcomes (true positives, true negatives, false positives, and false negatives), while the F1 score is a metric that measures the overall performance of a classification model, taking into account both precision and recall.

## Strengths and weaknesses of the Matthews correlation coefficient
The Matthews correlation coefficient (MCC) is a measure of the quality of binary classifications, taking into account true and false positives and negatives. Here are some strengths and weaknesses of the MCC:

**Strengths**:

-   The MCC is a balanced metric, taking into account all four possible outcomes of a binary classification (true positives, true negatives, false positives, and false negatives). This makes it **useful for cases where the classes are imbalanced or the cost of false positives and false negatives is different**.
-   The MCC can be used to compare the performance of different classification models, as it is **independent of the class distribution** and the prevalence of the positive class.
-   The MCC is easy to interpret, as it ranges from -1 to 1, where 1 is a perfect classification, 0 is no better than random guessing, and -1 is a completely wrong classification.

**Weaknesses**:

-   The MCC is sensitive to small changes in the data and can be unstable **when the number of true and false positives and negatives is small**.
-   The MCC is **not defined for multi-class classification**, as it is only designed for binary classification.
-   The MCC may not be suitable for some applications, as it is sensitive to the prevalence of the positive class and **may not be as informative in cases where the positive class is rare**.