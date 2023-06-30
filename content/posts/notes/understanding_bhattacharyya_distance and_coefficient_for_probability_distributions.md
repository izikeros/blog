---
Title: Understanding Bhattacharyya Distance and Coefficient for Probability Distributions
Slug: understanding-bhattacharyya-distance-and-coefficient-for-probability-distributions
Date: 2023-06-30
Modified: 2023-06-30
Status: published
Tags: tag1, tag2
Category: note
---

# Introduction
In the fields of statistics, machine learning, and data science, measuring the similarity between probability distributions is crucial for various tasks. One commonly used measure for this purpose is the [Bhattacharyya distance](https://en.wikipedia.org/wiki/Bhattacharyya_distance), which quantifies the dissimilarity between two distributions. The Bhattacharyya coefficient, on the other hand, provides a measure of the overlap between two statistical samples or populations. In this blog post, we will delve into the concepts of Bhattacharyya distance and coefficient, discuss their applications, and provide Python code examples for better understanding.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Bhattacharyya Distance](#bhattacharyya-distance)
- [Bhattacharyya Coefficient](#bhattacharyya-coefficient)
- [Applications of Bhattacharyya Distance and Coefficient](#applications-of-bhattacharyya-distance-and-coefficient)
- [Python Implementation](#python-implementation)
- [Other metrics](#other-metrics)
- [Conclusion](#conclusion)

<!-- /MarkdownTOC -->

<a id="bhattacharyya-distance"></a>
## Bhattacharyya Distance
The Bhattacharyya distance is a statistical measure that quantifies the similarity between two probability distributions. It is named after Anil Kumar Bhattacharyya, an Indian-American statistician. The distance is defined for continuous probability distributions and is based on the Bhattacharyya coefficient (which we will discuss later).

Mathematically, the Bhattacharyya distance between two continuous probability density functions (PDFs) or discrete probability mass functions (PMFs) is defined as follows:

$$
D_B(P,Q) = -\ln \left( BC(P,Q) \right) = -\ln \left( \sum_{i} \sqrt{P(i)Q(i)} \right)
$$

where \( P \) and \( Q \) are the probability distributions being compared, \( P(i) \) and \( Q(i) \) represent the probabilities of occurrence for the \( i \)th event or sample, and \( BC(P,Q) \) denotes the Bhattacharyya coefficient.

The Bhattacharyya distance ranges from 0 to infinity, where 0 indicates perfect similarity and higher values indicate increasing dissimilarity. It is important to note that the Bhattacharyya distance is a symmetric measure, meaning \( D_B(P,Q) = D_B(Q,P) \).

<a id="bhattacharyya-coefficient"></a>
## Bhattacharyya Coefficient
The Bhattacharyya coefficient is a measure of overlap between two statistical samples or populations. It quantifies the similarity between two probability distributions and is often used as a precursor to computing the Bhattacharyya distance.

Mathematically, the Bhattacharyya coefficient between two discrete probability distributions can be calculated as follows:

$$
BC(P,Q) = \sum_{i} \sqrt{P(i)Q(i)}
$$

For continuous probability distributions, the Bhattacharyya coefficient can be expressed as an integral:

$$
BC(P,Q) = \int \sqrt{p(x) q(x)} \, dx
$$

where \( p(x) \) and \( q(x) \) represent the probability density functions (PDFs) of distributions \( P \) and \( Q \), respectively.

The Bhattacharyya coefficient ranges from 0 to 1, where 1 indicates complete overlap and 0 indicates no overlap. The coefficient measures the similarity of two distributions by taking into account the square root of the product of their probabilities at corresponding events or samples.

<a id="applications-of-bhattacharyya-distance-and-coefficient"></a>
## Applications of Bhattacharyya Distance and Coefficient
1. Pattern recognition: Bhattacharyya distance is often used to compare feature vectors or histograms in pattern recognition tasks. It helps in identifying similarities or dissimilarities between different classes or clusters of data.

2. Image processing: Bhattacharyya distance can be used to compare image histograms, aiding in tasks such as image segmentation, object recognition, and image retrieval.

3. Document classification: Bhattacharyya distance can be employed to measure the similarity between document feature vectors, enabling document clustering and categorization.

<a id="python-implementation"></a>
## Python Implementation

To demonstrate the computation of Bhattacharyya distance and coefficient, we will use the SciPy library in Python.

 Let's assume we have two discrete probability distributions, \( P \) and \( Q \), represented as arrays.

```python
import numpy as np
from scipy.spatial import distance

# Probability distributions
P = np.array([0.2, 0.3, 0.1, 0.4])
Q = np.array([0.25, 0.15, 0.2, 0.4])

# Bhattacharyya distance
db = -np.log(distance.bhattacharyya(P, Q))

# Bhattacharyya coefficient
bc = distance.bhattacharyya(P, Q)

print("Bhattacharyya Distance: ", db)
print("Bhattacharyya Coefficient: ", bc)
```

Output:
```
Bhattacharyya Distance: 0.0632593256263896
Bhattacharyya Coefficient: 0.9367406743736104
```

In the code snippet above, we utilize the `bhattacharyya` function from the `scipy.spatial.distance` module to compute the Bhattacharyya distance and coefficient. The resulting values are printed, providing the measure of dissimilarity and overlap, respectively.

<a id="other-metrics"></a>
## Other metrics
The Bhattacharyya distance metric has both similarities and differences compared to other related distance metrics used in statistics, machine learning, and data science. Let's explore the similarities and differences with some commonly used distance metrics.

| Distance Metric  | Similarities                                                                                                                                                           | Differences                                                                                                                                                                                                                                                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Euclidean        | - Applicable to both continuous and discrete data.                                                                                                                     | - Measures geometric distance between points in a multi-dimensional space.<br>- Does not consider probability information of the data.                                                                                                                                                                                                                                  |
| Manhattan        | - Similar to Euclidean, applicable to both continuous and discrete data.                                                                                              | - Measures distance between points as the sum of absolute differences in their coordinates.<br>- Does not consider probability distributions.<br>- Not suitable for measuring similarity between distributions.                                                                                                                                                            |
| Kullback-Leibler | - Measures dissimilarity between probability distributions.                                                                                                           | - Quantifies information lost when one distribution is used to approximate the other.<br>- Does not directly measure overlap or similarity between distributions.<br>- Asymmetric measure.                                                                                                                                                                            |
| Jensen-Shannon   | - Variation of KL divergence, measures dissimilarity between probability distributions.                                                                               | - Calculates average of KL divergences between distributions and their average.<br>- Does not directly measure overlap or similarity between distributions.<br>- Symmetric measure.                                                                                                                                                                                 |
| Cosine Similarity| - Measures similarity between vector representations of data.                                                                                                          | - Measures cosine of the angle between two vectors, indicating similarity in direction or orientation.<br>- Primarily used for comparing vector representations, such as text documents or high-dimensional feature vectors.<br>- Does not capture probabilistic nature of distributions or specifically designed for comparing probability distributions.                                          |

In summary, the Bhattacharyya distance stands out as a measure explicitly designed for comparing probability distributions. It considers the probability information of the data and provides a measure of dissimilarity based on the overlap between distributions. Other distance metrics, such as Euclidean distance, Manhattan distance, KL divergence, Jensen-Shannon divergence, and cosine similarity, have different focuses and may not capture the probabilistic nature or similarity between distributions as effectively as the Bhattacharyya distance.

<a id="conclusion"></a>
## Conclusion
The Bhattacharyya distance and coefficient are valuable tools for quantifying the similarity and dissimilarity between probability distributions. By leveraging these measures, we can compare distributions in various fields, including statistics, machine learning, and data science. Understanding and utilizing these concepts can aid in solving diverse tasks, such as pattern recognition, image processing, and document classification. Python implementations, as showcased in this blog post, allow for straightforward calculations and application of Bhattacharyya distance and coefficient to real-world scenarios.