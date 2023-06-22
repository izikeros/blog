---
Title: Embeddings similarity metrics
Slug: embeddings-similarity-metrics
Date: 2023-06-08
Modified: 2023-06-08
Start: 2023-06-08
Tags: machine-learning, python
Category: Machine Learning
Image: /images/head/abstract_1.jpg
banner: "/images/head/abstract_1.jpg"
Summary: 
Status: draft
prompt: You are the Data Science deep learning expert. Give me long, markdown, blog-post style text on Similarity metrics for the embeddings (used in Natural Language Processing). The target audience are NLP professionals. For each method first explain it in simple words then delve into details for the professionals. Use LaTeX inline equations when needed. For each method discuss when the metrics is proven best to be used and then, what are the drawbacks and heads-up when using it. When each metric can fail?
---

> approximate nearest neighbors (ANN) algorithms like HNSW and IVFPQ

# Similarity Metrics for Embeddings in Natural Language Processing

In Natural Language Processing (NLP), one of the fundamental tasks is to measure the similarity between textual data. Embeddings play a crucial role in representing text as continuous vectors in a high-dimensional space, enabling effective comparison and analysis. However, determining the most appropriate similarity metric for embeddings is vital for accurate NLP applications. In this article, we will explore various similarity metrics commonly used in NLP, explaining their concepts in simple terms and delving into details for NLP professionals. We will also discuss the strengths, drawbacks, and potential failure cases of each metric.

## Cosine Similarity

Let's begin with the widely used cosine similarity metric. Cosine similarity measures the cosine of the angle between two vectors and determines their similarity based on the direction, rather than the magnitude, of the vectors. The cosine similarity between two vectors $\mathbf{a}$ and $\mathbf{b}$ is defined as:
$$
\text{{Cosine Similarity}} = \frac{{\mathbf{a} \cdot \mathbf{b}}}{{\|\mathbf{a}\| \|\mathbf{b}\|}}
$$
Please note that $\mathbf{a} \cdot \mathbf{b}$ represents the dot product of vectors $\mathbf{a}$ and $\mathbf{b}$, while ${\|\mathbf{a}\| \|\mathbf{b}\|}$ denote the magnitudes (norms) of vectors $\mathbf{a}$ and $\mathbf{b}$, respectively.

In simple terms, cosine similarity calculates the cosine of the angle between two vectors, providing a value between -1 and 1. A value of 1 indicates that the vectors have the same direction (maximum similarity), while a value of -1 indicates opposite directions (maximum dissimilarity). A value close to 0 suggests little or no similarity.

Cosine similarity is advantageous in various NLP scenarios. It is efficient to compute and works well with high-dimensional embeddings. Additionally, it is robust to vector magnitude, making it suitable for cases where the length of the vectors might vary.

However, cosine similarity also has some drawbacks. It fails to capture the notion of negative similarity, meaning it cannot distinguish between vectors that point in the opposite direction. For example, if $\mathbf{a}$ represents "good" and $\mathbf{b}$ represents "bad," their cosine similarity will be close to 1, indicating high similarity. Another limitation is that cosine similarity only measures the geometric similarity between vectors, disregarding the individual components or meanings of the vectors. Therefore, it may not reflect semantic or contextual similarity accurately.

## Euclidean Distance

Moving on, let's explore the Euclidean distance metric, which measures the straight-line distance between two vectors in the embedding space. The Euclidean distance between vectors $\mathbf{a}$ and $\mathbf{b}$ is defined as:

$$
d(\mathbf{a}, \mathbf{b}) = \sqrt{\sum_{i=1}^{n}(a_i - b_i)^2}
$$

In simpler terms, the Euclidean distance calculates the length of the direct path between two vectors in the embedding space. Smaller distances indicate higher similarity, while larger distances represent greater dissimilarity.

Euclidean distance is useful in certain NLP scenarios. It provides a measure of geometric similarity that can be beneficial when analyzing embeddings with clear separations in the space. It is also well-suited for clustering or classifying similar and dissimilar texts.

However, Euclidean distance has its limitations. It can be sensitive to noise, outliers, and variations in vector magnitudes. If the dimensions of the embedding space are not equally informative or normalized, certain dimensions may dominate the distance calculation. Moreover, Euclidean distance does not consider the direction or angle between vectors, neglecting the overall geometry of the embedding space.

## Manhattan Distance

Next, let's discuss the Manhattan distance metric, also known as the city block distance or L1 distance. The Manhattan distance between vectors $\mathbf{a}$ and $\mathbf{b}$ is defined as:
$$
\|\mathbf{a} - \mathbf{b}\|_1 = \sum_{i=1}^{n} |a_i - b_i|

$$
In simple terms, the Manhattan distance calculates the sum of absolute differences between corresponding components of two vectors. It measures the total distance needed to travel in a city block-like manner to reach from one vector to another.

Manhattan distance has its strengths in certain NLP scenarios. It is robust to outliers and provides a measure of similarity that considers both magnitude and direction of the differences between vectors. This metric can be useful when the magnitude of differences is significant in determining similarity.

However, Manhattan distance also has limitations. It is sensitive to variations in vector magnitude and does not account for the overall geometry or angle between vectors. Similar to Euclidean distance, the Manhattan distance may not capture the semantic or contextual similarity accurately.

## Minkowski Distance

The Minkowski distance is a generalization of both the Euclidean and Manhattan distances. It allows us to control the sensitivity to magnitude differences through a parameter called the order or degree. The Minkowski distance between vectors $\mathbf{a}$ and $\mathbf{b}$ is defined as:

$$
d(\mathbf{x}, \mathbf{y}) = \left(\sum_{i=1}^{n} |x_i - y_i|^p\right)^{\frac{1}{p}}
$$

Here, the parameter $p$ controls the degree of the Minkowski distance. When $p=2$, it becomes the Euclidean distance, and when $p=1$, it becomes the Manhattan distance.

The Minkowski distance provides flexibility in adjusting the sensitivity to magnitude differences. By varying the value of $p$, NLP professionals can experiment with different degrees of sensitivity, aligning it with their specific use case requirements.

However, the Minkowski distance inherits some of the limitations from both the Euclidean and Manhattan distances. It does not capture the overall geometry of the embedding space and can still be sensitive to variations in vector magnitudes.

## Jaccard Similarity

Let's now explore a similarity metric specifically designed for sets of elements, such as words or n-grams. The Jaccard similarity measures the similarity between two sets based on their intersection and union. For two sets $A$ and $B$, the Jaccard similarity is defined as:

$$
J(A, B) = \frac{{|A \cap B|}}{{|A \cup B|}}
$$

In the above equation, A and B represent the two sets for which we want to calculate the Jaccard similarity.

In simpler terms, the Jaccard similarity calculates the size of the common elements divided by the total number of distinct elements in the two sets. The resulting value ranges between 0 and 1, where 1 indicates complete similarity, and 0 indicates no common elements.

The Jaccard similarity is particularly useful in NLP tasks involving set comparisons, such as text classification, document clustering,

## Levenshtein Distance

The Levenshtein distance, also known as the edit distance, measures the minimum number of single-character edits (insertions, deletions, or substitutions) required to transform one string into another. It is commonly used to compare the similarity between two texts or sequences. The Levenshtein distance between strings $a$ and $b$ is defined as:
$$
Levenshtein Distance(a,b)=minimum\ number\ of\ edits
$$
The Levenshtein distance provides a measure of similarity by quantifying the number of transformations needed to convert one string into another. It is suitable for tasks such as spelling correction, text comparison, and approximate string matching.

However, the Levenshtein distance has certain drawbacks. It treats all characters equally, without considering their semantics or contextual meanings. Additionally, it does not account for the order or position of the characters, which can be important in some NLP tasks. Therefore, while the Levenshtein distance is useful for measuring string similarity, it may not capture the underlying meaning or semantics accurately.

## Word Mover's Distance

The Word Mover's Distance (WMD) is a similarity metric designed specifically for comparing pairs of text documents or sequences. It considers the semantic meaning of words and their relationships to measure the dissimilarity between two texts. The WMD calculates the minimum cumulative distance that words from one document need to travel to match the distribution of words in another document.

The Word Mover's Distance leverages word embeddings to compute the semantic similarity between words. It considers the meaning and context of words, making it suitable for tasks such as document clustering, text similarity, and information retrieval.

However, the WMD can be computationally expensive, especially when dealing with large vocabularies or documents. The calculation involves comparing the word embeddings of each word pair in the texts, resulting in a high time complexity. Additionally, the WMD heavily relies on the quality and coverage of the word embeddings used. Inadequate or biased embeddings may lead to inaccurate similarity measurements.

## Summary

In summary, choosing the most appropriate similarity metric for embeddings in NLP depends on the specific task and requirements. Cosine similarity is widely used and efficient, suitable for high-dimensional embeddings, but it may not capture negative similarity or semantic nuances. Euclidean distance provides a measure of geometric similarity, while Manhattan distance considers both magnitude and direction of differences. The Minkowski distance offers flexibility by controlling sensitivity to magnitude differences. Jaccard similarity is useful for set comparisons, and Levenshtein distance measures the minimum number of string edits. Word Mover's Distance incorporates semantic meaning but can be computationally expensive.

Understanding the strengths, limitations, and potential failure cases of each similarity metric is crucial for ensuring accurate results in NLP applications. It is recommended to evaluate and experiment with different metrics to find the one that aligns best with the specific task and data at hand.

# Similarity Metrics for Embedding Vectors in Natural Language Processing

Embedding vectors play a crucial role in Natural Language Processing (NLP) tasks by representing words or sentences in a continuous numerical space. These vectors capture semantic and syntactic information, allowing us to measure the similarity between words or sentences. A variety of similarity metrics exist for comparing embedding vectors, each with its own strengths and limitations. In this blog post, we will explore some commonly used similarity metrics, explain them in simple terms, and then dive into the details for professionals.

## Cosine Similarity

Cosine similarity is a popular metric for measuring the similarity between two embedding vectors. It calculates the cosine of the angle between the vectors, indicating how close they are in terms of direction. Cosine similarity ranges from -1 to 1, where 1 denotes perfect similarity, 0 denotes no similarity, and -1 denotes complete dissimilarity.

### Simple Explanation

To understand cosine similarity intuitively, imagine the embedding vectors as arrows pointing in a high-dimensional space. Cosine similarity measures the alignment between these arrows. If two vectors are perfectly aligned (pointing in the same direction), their cosine similarity will be 1. If they are orthogonal (perpendicular), the cosine similarity will be 0. And if they point in opposite directions, the cosine similarity will be -1.

### Mathematical Formulation

The cosine similarity between two embedding vectors, **a** and **b**, can be calculated using the dot product and vector norms as follows:

cosine_similarity(�,�)=�⋅�∥�∥∥�∥cosine_similarity(a,b)=∥a∥∥b∥a⋅b​

where �⋅�a⋅b denotes the dot product of vectors �a and �b, and ∥�∥∥a∥ and ∥�∥∥b∥ represent their respective Euclidean norms.

### Applicability and Drawbacks

Cosine similarity is widely used in NLP tasks such as word similarity, sentence similarity, and document retrieval. It is particularly effective when the magnitude of the vectors is not essential, and only the direction matters. For example, in word embeddings, cosine similarity can capture semantic relationships like "king" and "queen" being similar while ignoring their individual magnitudes.

However, cosine similarity has a few limitations. One important consideration is that it does not account for the magnitude of the vectors, only their direction. Thus, it may not distinguish between two vectors with the same direction but different lengths. Additionally, cosine similarity treats all dimensions equally, which may not be desirable in some cases where certain dimensions are more informative than others.

Moreover, cosine similarity is not suitable for measuring similarity between rare or out-of-vocabulary words, as their embedding vectors might be sparse or zero. In such cases, alternative approaches like word sense disambiguation or contextual embeddings may be more appropriate.

## Euclidean Distance

Another commonly used metric for measuring similarity between embedding vectors is Euclidean distance. Unlike cosine similarity, Euclidean distance considers both the direction and magnitude of vectors. It measures the straight-line distance between two vectors in the embedding space.

### Simple Explanation

To grasp the concept of Euclidean distance intuitively, imagine the embedding vectors as points in a geometric space. Euclidean distance is like measuring the length of a straight line between these points. The shorter the distance, the more similar the vectors are in terms of their overall position.

### Mathematical Formulation

The Euclidean distance between two embedding vectors, **a** and **b**, can be calculated as follows:

euclidean_distance(�,�)=∑�=1�(��−��)2euclidean_distance(a,b)=i=1∑n​(ai​−bi​)2​

where ��ai​ and ��bi​ represent the components of vectors �a and �b respectively, and �n denotes the dimensionality of the vectors.

### Applicability and Drawbacks

Euclidean distance is commonly used in tasks such as clustering, anomaly detection, and nearest neighbor search. It considers both magnitude and direction, making it suitable for scenarios where these factors are important. For example, in clustering tasks, Euclidean distance helps group similar points together based on their overall proximity.

However, Euclidean distance has certain limitations. One drawback is that it is sensitive to the scale of the vectors. If the magnitudes of the vectors differ significantly, the Euclidean distance will be dominated by the larger vector. Therefore, it is often necessary to normalize the vectors before computing the distance.

Additionally, Euclidean distance treats all dimensions equally, which may not be desirable when some dimensions are more relevant than others. In such cases, techniques like feature weighting or dimensionality reduction can be applied to mitigate this issue.

## Mahalanobis Distance

Mahalanobis distance is a metric that takes into account the correlation between different dimensions of the embedding vectors. It measures the distance between two vectors while considering the covariance structure of the data.

### Simple Explanation

To understand Mahalanobis distance intuitively, consider it as a way to account for the shape of the data cloud formed by the embedding vectors. Unlike Euclidean distance, which assumes uncorrelated dimensions, Mahalanobis distance adjusts for the correlation among dimensions. It captures the true distance between vectors, considering both the direction, magnitude, and the relationship between different dimensions.

### Mathematical Formulation

The Mahalanobis distance between two embedding vectors, **a** and **b**, can be calculated as follows:

mahalanobis_distance(�,�)=(�−�)��−1(�−�)mahalanobis_distance(a,b)=(a−b)TS−1(a−b)​

where �S represents the covariance matrix of the embedding vectors.

### Applicability and Drawbacks

Mahalanobis distance is particularly useful when dealing with high-dimensional data with correlated dimensions. It is often used in tasks like outlier detection, classification, and dimensionality reduction. By incorporating the covariance structure, Mahalanobis distance provides a more accurate measure of similarity.

However, there are certain considerations when using Mahalanobis distance. First, it requires estimating the covariance matrix from the available data, which can be challenging when the number of dimensions is large or the data is limited. Additionally, Mahalanobis distance assumes that the data follows a multivariate normal distribution, which may not hold true in all cases. Violations of this assumption can lead to inaccurate distance measurements.

Moreover, Mahalanobis distance is computationally expensive compared to Euclidean distance or cosine similarity due to the need to calculate and invert the covariance matrix. Therefore, it may not be suitable for large-scale applications with real-time constraints.

## Conclusion

In this blog post, we have explored some commonly used similarity metrics for comparing embedding vectors in NLP tasks. Cosine similarity, Euclidean distance, and Mahalanobis distance each offer unique advantages and considerations.

Cosine similarity is effective for capturing semantic relationships and disregarding vector magnitudes, but it does not account for vector lengths or dimension relevance. Euclidean distance considers both direction and magnitude, but it is sensitive to vector scale and treats all dimensions equally. Mahalanobis distance incorporates the covariance structure of the data, providing a more accurate measure of similarity, but it requires estimating the covariance matrix and assumes a multivariate normal distribution.

When selecting a similarity metric, it is essential to consider the specific requirements of the task at hand and the nature of the data. Understanding the strengths and limitations of each metric can help professionals make informed decisions and achieve better results in their NLP applications.