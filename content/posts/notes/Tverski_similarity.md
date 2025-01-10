---
Title: Tverski Similarity Metrics
Slug: tverski-similarity-metrics
Date: 2023-12-10
Modified: 2023-12-10
Status: published
Tags: nlp, text-similarity, string-similarity, similarity-metrics, jaccard, cosine-similarity, levenshtein, word-embeddings, soundex
Category: note
---

Tversky similarity and [[jaro_winkler_similarity|Jaro-Winkler]] similarity are two different similarity metrics that are used to compare strings or sequences. They are designed for specific purposes and have different mathematical formulas and applications.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Tversky Similarity](#tversky-similarity)
   - [Formula](#formula)
   - [Python Example](#python-example)
- [Jaro-Winkler Similarity \(for reference\)](#jaro-winkler-similarity-for-reference)
- [Summary](#summary)

<!-- /MarkdownTOC -->

<a id="tversky-similarity"></a>

## Tversky Similarity

**Tversky similarity is a metric used to compare sets**, typically in the context of information retrieval, information retrieval evaluation, and recommendation systems. It was introduced by Amos Tversky in his work on set comparison. Tversky similarity takes into account the **number of common elements** between two sets as well as the **differences in elements between them**. It has two parameters, alpha and beta, which control the balance between precision and recall.

Let's dive into the mathematical formula, explanation, and Python examples for  Tversky similarity.

<a id="formula"></a>

### Formula

Tversky similarity measures the similarity between two sets A and B, considering the trade-off between false positives and false negatives. The formula for Tversky similarity is:

$$
Tversky(A, B) = \frac{|A \cap B|}{|A \cap B| + \alpha |A - B| + \beta |B - A|}
$$

Where:
- $(|A \cap B|)$ is the size of the intersection of sets A and B.
- $(|A - B|)$ is the size of the set difference of A minus B.
- ($|B - A|)$ is the size of the set difference of B minus A.
- $\alpha$ and $\beta$ are parameters that control the trade-off between precision and recall. When $\alpha = \beta = 1$, the Tversky similarity becomes the Jaccard similarity.

<a id="python-example"></a>

### Python Example

```python
def tversky_similarity(set_a, set_b, alpha, beta):
    intersection = len(set_a.intersection(set_b))
    a_minus_b = len(set_a.difference(set_b))
    b_minus_a = len(set_b.difference(set_a))
    
    similarity = intersection / (intersection + alpha * a_minus_b + beta * b_minus_a)
    return similarity

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "date", "elderberry"}

alpha = 0.5
beta = 0.5
similarity = tversky_similarity(set1, set2, alpha, beta)
print("Tversky Similarity:", similarity)
```

<a id="jaro-winkler-similarity-for-reference"></a>

## Jaro-Winkler Similarity (for reference)

Jaro-Winkler similarity is a metric used to compare two strings, often used in record linkage and fuzzy string matching tasks. It was developed by William E. Winkler and Matthew A. Jaro. Jaro-Winkler similarity calculates a score between 0 and 1, where 1 indicates a perfect match and 0 indicates no similarity. It considers the number of matching characters between two strings and the positions of those matching characters. The Jaro-Winkler similarity gives more weight to the common prefix of the strings, making it particularly useful for comparing names and short strings. For more information about Jaro-Winkler similarity see: [[jaro_winkler_similarity]].

<a id="summary"></a>

## Summary

The main differences between Tversky similarity and Jaro-Winkler similarity are:

- **Application Domain:** Tversky similarity is used to compare sets, while Jaro-Winkler similarity is used to compare strings.
- **Parameters:** Tversky similarity has parameters alpha and beta to control precision and recall, while Jaro-Winkler similarity does not have such parameters.
- **Target Data:** Tversky similarity works with sets of items, while Jaro-Winkler similarity works with individual strings.
- **Use Cases:** Tversky similarity is commonly used in information retrieval and recommendation systems, while Jaro-Winkler similarity is used in fuzzy string matching and record linkage tasks.

X::[[jaro_winkler_similarity]]
