---
Title: TF-IDF with examples
Slug: tfidf-with-examples
Date: 2023-11-10
Modified: 2023-11-10
Status: published
tags: tfidf, tf-idf, bag-of-words, embeddings, text-vectorization, information-retrieval, text-mining
Category: note
prompt: Explain me how the TF-IDF works. Give me a minimal example that showcase calculation of high and low TF-IDF
prompt2: give me TF-IDF inline latex equation
---

X::[[SPLADE_embeddings]]

**TF-IDF** stands for **Term Frequency-Inverse Document Frequency**. It's a numerical statistic used to reflect how important a word is to a document in a collection or corpus. It's often used in information retrieval and text mining.

TF-IDF is composed of two parts:

1. **Term Frequency (TF)**: This measures the frequency of a word in a document. It's the ratio of the number of times a word appears in a document compared to the total number of words in that document. It increases as the number of occurrences of that word within the document increases. Each document has its own term frequency.

2. **Inverse Document Frequency (IDF)**: This measures the importance of the word in the entire corpus. The IDF of a rare word is high, whereas the IDF of a frequent word is likely to be low. Thus, words that occur frequently across many documents will have a lower IDF, and rare words will have a high IDF.

The TF-IDF value is calculated by multiplying these two metrics: TF and IDF.

## Minimal example

## High TF-IDF

Consider a document containing 100 words wherein the word 'cat' appears 3 times.

The term frequency (TF) for 'cat' is then (3 / 100) = 0.03.

Now, assume we have 10 million documents and the word 'cat' appears in one thousand of these. Then, the inverse document frequency (IDF) is calculated as log(10,000,000 / 1,000) = 4.

So, the TF-IDF weight is the product of these quantities: 0.03 * 4 = 0.12.

### Low TF-IDF

Now, let's consider a common word like 'the'. Assume it appears 20 times in a document of 100 words. So, TF for 'the' is (20/100) = 0.2.

Assume 'the' appears in 1 million out of 10 million documents. So, IDF for 'the' is log(10,000,000 / 1,000,000) = 1.

The TF-IDF weight for 'the' is 0.2 * 1 = 0.2.

Even though 'the' appeared more times than 'cat' in the document, the TF-IDF weight for 'cat' is higher than 'the'. This is because IDF gives a higher weight to words that are less frequent in the corpus, making 'cat' more important than 'the' in the context of our corpus.

## The formula

here is the TF-IDF equation in LaTeX format:

The term frequency $TF$ is calculated as:

$$
TF(t, d) = \frac{f_{t, d}}{\sum_{t' \in d} f_{t', d}}
$$

Where:

- $f_{t, d}$ is the frequency of term $t$ in document $d$
- The denominator is the sum of frequencies of all terms in document $d$

The inverse document frequency $IDF$ is calculated as:

$$
IDF(t, D) = \log \frac{|D|}{|\{d \in D: t \in d\}|}
$$

Where:

- $|D|$ is the total number of documents in the corpus
- The denominator is the number of documents where the term $t$ appears

Finally, the TF-IDF is calculated as:

$$
TFIDF(t, d, D) = TF(t, d) \cdot IDF(t, D)
$$

Where:

- $t$ is the term
- $d$ is the document
- $D$ is the corpus (set of all documents)
