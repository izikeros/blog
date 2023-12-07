---
Category: Machine Learning
Date: '2020-01-19'
Image: /images/head/compare_histograms.jpg
Modified: '2023-07-12'
Slug: metrics-to-compare-histograms
Start: '2023-01-19'
Status: published
Summary: Learn about metrics used to compare histograms with examples of how to calculate them in python. From Chi-Squared distance to Kullback-Leibler divergence and Earth Mover's distance. A comprehensive guide.
Tags: histogram, statistics, machine-learning, statistical-tests, metrics, distance-metrics
Title: Metrics Used to Compare Histograms
---

## Introduction
Comparing histograms is a crucial step in data analysis, as it allows us to gain insights into the underlying distributions of our data. There are several metrics that can be used to compare histograms, each with its own strengths and weaknesses. In this article, we will discuss some of the most commonly used metrics for comparing histograms and provide examples of how to calculate them in Python.

<!-- MarkdownTOC autolink="true" autoanchor="true" -->

- [Most common methods](#most-common-methods)
	- [1. Chi-Squared Distance](#1-chi-squared-distance)
	- [2. Earth Mover's Distance](#2-earth-movers-distance)
	- [3. Kullback-Leibler Divergence](#3-kullback-leibler-divergence)
- [Other methods for histogram comparison](#other-methods-for-histogram-comparison)
- [Conclusion](#conclusion)

<!-- /MarkdownTOC -->

<a id="most-common-methods"></a>
## Most common methods

<a id="1-chi-squared-distance"></a>
### 1. Chi-Squared Distance

The Chi-Squared distance, also known as the Chi-Squared test, measures the difference between two histograms by comparing the observed frequencies to the expected frequencies. The Chi-Squared distance is defined as:

$$ \chi^2 = \sum_{i=1}^{n} \frac{(O_i - E_i)^2}{E_i} $$

Where $O_i$ is the observed frequency in bin $i$, $E_i$ is the expected frequency in bin $i$, and $n$ is the number of bins. The Chi-Squared distance is sensitive to large differences between the observed and expected frequencies, and is commonly used in hypothesis testing to determine if two histograms come from the same distribution.

To calculate the Chi-Squared distance in Python, we can use the `scipy.stats.chisquare` function from the SciPy library. Here is an example of how to use this function to calculate the Chi-Squared distance between two histograms:

```python
from scipy.stats import chisquare

# observed frequencies
obs1 = [10, 20, 30, 40]
obs2 = [15, 25, 35, 45]

# calculate the Chi-Squared distance
chi2, p = chisquare(obs1, obs2)

print(chi2)
```
<a id="2-earth-movers-distance"></a>
### 2. Earth Mover's Distance

The Earth Mover's distance (EMD) is a more sophisticated metric that takes into account the shape of the histograms as well as the differences in frequency. The EMD is defined as the minimum amount of "work" required to transform one histogram into the other, where "work" is defined as the product of the difference in frequency and the distance between the bins. The EMD is commonly used in image processing and computer vision, but can also be used to compare histograms.

To calculate the EMD in Python, we can use the `emd` function from the `pyemd` library. Here is an example of how to use this function to calculate the EMD between two histograms:

```python
import numpy as np
from pyemd import emd

# histogram bin centers
bins1 = [1, 2, 3, 4]
bins2 = [1.5, 2.5, 3.5, 4.5]

# histogram frequencies
freq1 = [10, 20, 30, 40]
freq2 = [15, 25, 35, 45]

# calculate the EMD
emd_val = emd(bins1, bins2, freq1, freq2)

print(emd_val)
```

<a id="3-kullback-leibler-divergence"></a>
### 3. Kullback-Leibler Divergence

The Kullback-Leibler divergence (KLD), also known as the relative entropy, measures the difference between two probability distributions. The KLD is defined as:

$$ D_{KL}(P||Q) = \sum_{i=1}^{n} P(i) \log\frac{P(i)}{Q(i)} $$

Where $P$ is the probability distribution of the first histogram, $Q$ is the probability distribution of the second histogram, and $n$ is the number of bins. The KLD is a measure of the information lost when approximating one histogram with the other. It is commonly used in information theory and machine learning.

To calculate the KLD in Python, we can use the `scipy.stats.entropy` function from the SciPy library. Here is an example of how to use this function to calculate the KLD between two histograms:

```python
from scipy.stats import entropy

# histogram frequencies
freq1 = [10, 20, 30, 40]
freq2 = [15, 25, 35, 45]

# normalize the frequencies to get probability distributions
prob1 = freq1 / np.sum(freq1)
prob2 = freq2 / np.sum(freq2)

# calculate the KLD
kld = entropy(prob1, prob2)

print(kld)
```

<a id="other-methods-for-histogram-comparison"></a>
## Other methods for histogram comparison

-   **Intersection**: it is a simple but widely used measure, which counts the number of bins where the histograms overlap. This metric gives a value between 0 and the minimum number of samples in the two histograms, with 0 indicating no overlap and the maximum value indicating perfect overlap.
    
-   **Bhattacharyya Distance**: The Bhattacharyya distance is a measure of similarity between two histograms. It is based on the Bhattacharyya coefficient, which is a measure of the similarity of two probability distributions.

-   **Wasserstein Distance**: Also known as the "Earth Mover's Distance" (EMD), it is a distance measure between probability distributions. It is widely used in image processing and computer vision, and has been applied to the comparison of histograms.

There are other metrics such as [Hellinger distance](https://en.wikipedia.org/wiki/Hellinger_distance), [Jeffreys divergence](https://encyclopediaofmath.org/wiki/Jeffreys_distance), [Jensen-Shannon divergence](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence), etc. that can be used to compare histograms as well.

<a id="conclusion"></a>
## Conclusion
There are several metrics that can be used to compare histograms, each with its own strengths and weaknesses. 
- The **Chi-Squared** distance is **sensitive to large differences in frequency**, 
- the **Earth Mover's Distance** takes into account the **shape of the histograms**, and 
- the **Kullback-Leibler Divergence** measures the **information lost** when approximating one histogram with the other.

By understanding these metrics and how to calculate them in Python, data scientists can choose the most appropriate metric for their analysis and gain deeper insights into the underlying distributions of their data.

It is always recommended to try out different metrics and choose the best one that suits the problem and data.

To learn more about these metrics and other techniques for comparing histograms, visit the following resources:

-   [Chi-Squared Test](https://en.wikipedia.org/wiki/Chi-squared_test)
-   [Earth Mover's Distance](https://en.wikipedia.org/wiki/Earth_mover%27s_distance)
-   [Kullback-Leibler Divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)
-   [pyemd library](https://pypi.org/project/pyemd/)
-   [SciPy library](https://scipy.org/)
