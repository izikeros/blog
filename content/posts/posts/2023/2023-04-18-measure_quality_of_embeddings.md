---
Title: Intrinsic vs. Extrinsic Evaluation - What's the Best Way to Measure Embedding Quality?
Slug: measure-quality-of-embeddings
Date: 2023-04-18
Modified: 2023-04-18
Start: 2023-04-18
Tags: machine-learning, python
Category: Machine Learning
Image: /images/head/abstract_6.jpg
Summary: Learn how to measure the quality of word and sentence embeddings in natural language processing (NLP), including intrinsic and extrinsic evaluation, and their strengths and limitations.
Status: published
prompt: In machine learning, NLP - How to measure quality of embeddings (e.g. word embeddings or sentence embeddings). Give me long blog-post style text on that, audience for the article should be expert data scientists. Provide mathematical formulas in LaTeX in display format (not inline) if needed. - If there is any process described provide mermaid diagram of mermaid gantt chart - propose 10 intriguing or catchy titles for this article - In the end provide also HTML page description for this article (less than 140-200 characters)
---

## Introduction
Let's start with the concept of embedding vectors. In natural language processing (NLP), an embedding vector is a mathematical representation of words or phrases. It's a way to convert text data into numerical values that can be processed by machine learning algorithms. Word embeddings and sentence embeddings are widely used in natural language processing (NLP) for a variety of tasks, such as text classification, named entity recognition, machine translation, and sentiment analysis. However, it is not always straightforward to evaluate the quality of embeddings, and different evaluation metrics may be appropriate for different use cases. In this blog post, we will explore several ways to measure the quality of embeddings, including intrinsic and extrinsic evaluation, and discuss their strengths and limitations.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Intrinsic Evaluation](#intrinsic-evaluation)
	- [Cosine Similarity](#cosine-similarity)
	- [Spearman Correlation](#spearman-correlation)
	- [Accuracy](#accuracy)
- [Extrinsic Evaluation](#extrinsic-evaluation)
	- [F1 Score](#f1-score)
	- [Perplexity](#perplexity)
- [Limitations](#limitations)
- [Conclusion](#conclusion)

<!-- /MarkdownTOC -->

<a id="intrinsic-evaluation"></a>
## Intrinsic Evaluation
 > **Intrinsic evaluation** - aims to measure the quality of embeddings by assessing their performance on specific NLP tasks that are related to the embedding space itself, such as word similarity, analogy, and classification.
 
In this section, we will discuss three commonly used intrinsic evaluation metrics: cosine similarity, Spearman correlation, and accuracy.

<a id="cosine-similarity"></a>
### Cosine Similarity
Cosine similarity measures the similarity between two vectors by computing the cosine of the angle between them. In the context of embeddings, cosine similarity is often used to measure the similarity between two words, or between a word and its context. The formula for cosine similarity is as follows:

$$
cosine\_similarity(\textbf{v}_1, \textbf{v}_2) = \frac{\textbf{v}_1 \cdot \textbf{v}_2}{\|\textbf{v}_1\|\|\textbf{v}_2\|}
$$

where $\textbf{u}$ and $\textbf{v}$ are the embeddings of two words, and $|\cdot|$ denotes the Euclidean norm.

<a id="spearman-correlation"></a>
### Spearman Correlation
Spearman correlation measures the monotonic relationship between two variables, which can be the similarity scores of two sets of words or phrases computed by humans and by embeddings. A high Spearman correlation indicates that the embeddings are able to capture the semantic relationships between words that humans perceive. The formula for Spearman correlation is as follows:

$$
\text{Spearman's correlation} = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}

$$

where $d_i$ is the difference between the ranks of the $i$-th pair of similarity scores, and $n$ is the number of pairs.

<a id="accuracy"></a>
### Accuracy
Accuracy measures the performance of embeddings on classification tasks, such as sentiment analysis or topic classification. Given a dataset of labeled examples, the embeddings are used to represent each example, and a classifier is trained on these representations. The accuracy of the classifier on a held-out test set is then used as a measure of the quality of the embeddings.

<a id="extrinsic-evaluation"></a>
## Extrinsic Evaluation
> **Extrinsic evaluation** - aims to measure the quality of embeddings by assessing their performance on downstream NLP tasks, such as machine translation or text classification, that are not directly related to the embedding space itself.

In this section, we will discuss two commonly used extrinsic evaluation metrics: F1 score and perplexity.
<a id="f1-score"></a>
### F1 Score
F1 score is a metric commonly used in binary classification problems, such as sentiment analysis or named entity recognition. It combines precision and recall into a single score that ranges from 0 to 1. A high F1 score indicates that the embeddings are able to capture the relevant features of the input data. The formula for F1 score is as follows:

$$
F1 = \frac{2 \cdot \text{precision} \cdot \text{recall}}{\text{precision} + \text{recall}}
$$

where precision is the fraction of true positives among the predicted positives, and recall is the fraction of true positives among the actual positives.

<a id="perplexity"></a>
### Perplexity
Perplexity is a metric commonly used in language modeling tasks, such as machine translation or text generation. It measures how well a language model can predict a held-out test set of text, given the embeddings as input. A low perplexity indicates that the embeddings  are able to capture the semantic and syntactic structures of the language. The formula for perplexity is as follows:

$$
\text{perplexity} = 2^{-\frac{1}{N}\sum_{i=1}^{N} \log_2 p(w_i | \textbf{e}_i)}
$$

where $N$ is the number of tokens in the test set, $\textbf{e}_i$ is the embedding of the $i$-th token, and $p(w_i | \textbf{e}_i)$ is the conditional probability of the $i$-th token given its embedding.

<a id="limitations"></a>
## Limitations
While intrinsic and extrinsic evaluation metrics can provide useful insights into the quality of embeddings, they also have some limitations. Intrinsic evaluation may not always reflect the performance of embeddings on downstream tasks, and extrinsic evaluation may not always isolate the contribution of embeddings from other factors, such as the choice of model architecture or the quality of the training data. Moreover, the choice of evaluation metrics may depend on the specific use case and the available resources, and there is no one-size-fits-all solution.
