---
Title: Rank Fusion Algorithms - From Simple to Advanced
Slug: Rank-fusion-algorithms-from-simple-to-advanced
Date: 2023-07-28
Modified: 2023-10-09
Status: published
tags: rank-fusion, rank, search, hybrid-search
Category: note
---
## Introduction

Rank fusion is a fundamental technique used in various domains, including data science and search engine optimization, to combine multiple ranked lists into a single, more reliable ranking. This process aims to exploit the strengths of individual ranking algorithms and mitigate their weaknesses, leading to improved overall performance. In this blog post, we will explore a range of rank fusion algorithms, starting from simple yet effective methods to advanced techniques employed by tech giants to achieve state-of-the-art results.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Algorithms](#algorithms)
 	- [Borda Algorithm](#borda-algorithm)
 	- [Combining Probability Mass Function \(CPMF\)](#combining-probability-mass-function-cpmf)
 	- [Rank-Biased Precision \(RBP\)](#rank-biased-precision-rbp)
 	- [LambdaMART](#lambdamart)
 	- [Neural Rank Fusion](#neural-rank-fusion)
 	- [Reciprocal rank fusion](#reciprocal-rank-fusion)
- [Conclusion](#conclusion)
- [References](#references)

<!-- /MarkdownTOC -->

<a id="algorithms"></a>

## Algorithms

<a id="borda-algorithm"></a>

### Borda Algorithm

The Borda algorithm is one of the simplest rank fusion techniques. It assigns scores to items based on their positions in the individual rankings and then combines these scores to obtain a fused ranking. In the context of search engine results, each document receives points based on its position in the ranked lists. The points are then summed up to form the final rank.

Consider $n$ ranked lists $\{R_1, R_2, \ldots, R_n\}$ with $m$ items. The Borda algorithm assigns points to each item $i$ in the following way:

$$
\text{Borda Score}(i) = \sum_{j=1}^{n} (m - \text{rank}_j(i))
$$
Where $\text{rank}_j(i)$ denotes the position of item $i$ in the $j$th ranked list.

The Borda algorithm is easy to implement, but it might lag in performance for large datasets or when the individual rankings are significantly diverse.

<a id="combining-probability-mass-function-cpmf"></a>

### Combining Probability Mass Function (CPMF)

CPMF is a probabilistic rank fusion method that incorporates the probability of an item being at a certain rank in individual lists. It assumes that the rankings are probabilistic and uses the Probability Mass Function (PMF) to calculate the fused ranking. CPMF outperforms Borda for diverse and noisy datasets.

Let $p_{ij}$ be the probability that item $i$ appears at rank $j$ in the $n$ lists. The CPMF score for item $i$ is given by:

$$
\text{CPMF Score}(i) = \sum_{j=1}^{m} p_{ij}
$$

The probabilities $p_{ij}$ can be estimated using techniques like the [Plackett-Luce model](https://hturner.github.io/PlackettLuce/articles/Overview.html) or the Thurstone-Mosteller model.

<a id="rank-biased-precision-rbp"></a>

### Rank-Biased Precision (RBP)

RBP is a rank fusion method widely used in information retrieval systems. It incorporates a user-defined persistence parameter $p$ to reflect the probability that a user will examine the search results up to a certain rank. This parameter allows the search engine to optimize rankings based on user behavior.

For a given ranked list $R_j$, the RBP score is calculated as follows:

$$
\text{RBP Score}(R_j) = (1 - p) \sum_{k=1}^{m} p^{k-1} \text{rel}(R_j[k])
$$
Where $\text{rel}(R_j[k])$ is an indicator function representing the relevance of the item at rank $k$ in list $R_j$.

RBP provides more flexibility in tuning the importance of different ranks based on user preferences.

<a id="lambdamart"></a>

### LambdaMART

LambdaMART is an advanced algorithm used by tech giants like Microsoft and Yahoo for learning-to-rank tasks. It is based on the gradient boosting framework and employs LambdaRank, which optimizes the ListNet loss function using gradient descent.

The LambdaMART algorithm involves constructing a set of weak rankers (usually decision trees) that are iteratively refined to minimize the LambdaRank objective, which directly measures the pairwise disagreement between ranks.

$$
\text{LambdaRank Objective} = \sum_{i=1}^{m} \sum_{j=1}^{m} \text{DCG gain}(i, j) \cdot \text{Lambda}(i, j)
$$

Where $\text{DCG gain}(i, j)$ is the gain of swapping items at ranks $i$ and $j$ in the ranking, and $\text{Lambda}(i, j)$ is a weight function that depends on the gradients of the individual models.

LambdaMART's ability to optimize for ranking measures directly contributes to its superior performance in learning-to-rank scenarios.

<a id="neural-rank-fusion"></a>

### Neural Rank Fusion

With the rise of deep learning, neural rank fusion methods have gained popularity due to their ability to learn complex patterns from data. Neural rank fusion models typically employ techniques like siamese networks or transformer-based architectures to process individual rankings and generate a fused ranking.

In a siamese network-based approach, the individual rankings are fed into two parallel networks with shared weights. The networks learn to map the rankings into a common embedding space, where the fused ranking is generated based on similarity scores.

On the other hand, transformer-based rank fusion models utilize attention mechanisms to process and combine individual rankings effectively.

Neural rank fusion methods often outperform traditional algorithms when sufficient training data is available, but they may require substantial computational resources.

<a id="reciprocal-rank-fusion"></a>

### Reciprocal rank fusion

The [Reciprocal Rank Fusion (RRF)](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf) is an advanced algorithmic technique designed to amalgamate multiple result sets, each having distinct relevance indicators, into a unified result set. One of the key advantages of RRF is its ability to deliver high-quality results without the necessity for any tuning. Moreover, it does not mandate the relevance indicators to be interconnected or similar in nature.

Diving deeper into the algorithm, RRF is based on the concept of reciprocal rank. The reciprocal rank of a document is the multiplicative inverse of its rank. In the context of information retrieval, the rank of a document is its position in a list of documents sorted by relevance. The reciprocal rank is used to give higher weight to documents that appear earlier in the list.

The RRF algorithm combines the reciprocal ranks of the same document from different result sets to compute a combined score. The combined score is then used to rank the documents in the final result set. The formula used in the RRF algorithm is as follows:

$$
\text{RRF Score} = \frac{1}{k + rank}
$$

Where $k$ is a constant (usually set to 60), and $rank$ is the rank of the document in a particular result set. The RRF score is calculated for each document in each result set, and the scores are then summed up to get the final score for each document.

The properties of the RRF algorithm include its simplicity, effectiveness, and robustness. It is simple because it only requires the ranks of the documents and does not need any tuning. It is effective because it can combine result sets with different relevance indicators and still produce high-quality results. It is robust because it is not sensitive to the choice of $k$ and can handle a large number of result sets.
<a id="conclusion"></a>

## Conclusion

Rank fusion serves as a potent tool in the arsenal of data scientists and search engine experts, enhancing the efficacy of ranking performance. The spectrum of rank fusion algorithms ranges from the **straightforward Borda algorithm** to the more complex Neural Rank Fusion, each tailored to meet specific scenarios and data attributes. While the **Borda** algorithm is **appreciated** for its **simplicity** and **ease of implementation**, more advanced techniques like **LambdaMART** and **Neural Rank Fusion** are capable of delivering **cutting-edge results for large-scale applications**.

Incorporating the Reciprocal Rank Fusion (RRF) into this discussion, it stands out for its ability to **combine multiple result sets with varying relevance indicators** **without the need for tuning**. This makes it a robust and effective choice for many applications.

**Edits**:

- 2023-10-09 - Added "Reciprocal rank fusion", rewrite conclusion
<a id="references"></a>

## References

1. Wikipedia article: [Borda algorithm](https://en.wikipedia.org/wiki/Borda_count)
2. [From RankNet to LambdaRank to LambdaMART: An Overview](https://www.microsoft.com/en-us/research/publication/from-ranknet-to-lambdarank-to-lambdamart-an-overview/)
3. [Burges, Christopher. "From RankNet to LambdaRank to LambdaMART: An overview." Learning 11.23-581 (2010): 81.](https://www.microsoft.com/en-us/research/publication/from-ranknet-to-lambdarank-to-lambdamart-an-overview/)
4. [Rank-Biased Precision for Measurement of Retrieval Effectiveness](https://people.eng.unimelb.edu.au/jzobel/fulltext/acmtois08.pdf)
5. [Reciprocal rank fusion (RRF)](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf)

X::[[posts/notes/implementing_reciprocal_rank_fusion_in_python]]
