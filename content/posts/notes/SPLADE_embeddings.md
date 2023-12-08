---
Title: SPLADE sparse vectors - explaination, properties
Slug: splade-sparse-vectors
Date: 2023-11-10
Modified: 2023-12-08
Status: published
tags: splade, tf-idf, bag-of-words, bert, beir, sparse, text-vectorization 
Category: note
---


**TL; DR** SPLADE is a neural retrieval model which learns query/document **sparse** expansion via the BERT MLM head and sparse regularization. Sparse representations benefit from several advantages compared to dense approaches: efficient use of inverted index, explicit lexical match, interpretability... They also seem to be better at generalizing on out-of-domain data (BEIR benchmark).

I have learned about SPLADE from the article: [SPLADE for Sparse Vector Search Explained | Pinecone](https://www.pinecone.io/learn/splade/). Here below are the key concepts from the article (LLM summary)


The article discusses the evolution of search and recommendation systems, focusing on the shift from traditional "bag of words" methods to modern vector search. It explains how big tech companies like Google, Netflix, and Amazon use vector search to power their systems.

The traditional **bag of words** methods transform documents into a set of words, populating a sparse "frequency vector". While these methods are **efficient and interpretable**, they are **not perfect** due to their **reliance on exact term matching,** which doesn't align with human nature.

Dense embedding models offer a solution by allowing search based on semantic meaning. However, they require vast amounts of data for fine-tuning and don't perform well in niche domains where data is scarce.

The article introduces a solution to these problems: **a merger of sparse and dense retrieval through hybrid search and learnable sparse embeddings**. It focuses on **SPLADE** (Sparse Lexical and Expansion model), a **model that uses a pretrained language model like BERT to enhance sparse vector embedding.**

The article also discusses the pros and cons of sparse and dense vectors, the concept of two-stage retrieval, and the drawbacks of this approach. It then delves into the workings of SPLADE, explaining how it builds sparse embeddings and how it can be implemented using Hugging Face and PyTorch or the official SPLADE library.

The article concludes by acknowledging the **limitations of SPLADE**, such as its **slower retrieval speed compared to other sparse methods**, and suggests solutions to these problems. It also highlights the potential of mixing both dense and sparse representations using hybrid search indexes to make vector search more accurate and accessible.

X::[[tf_idf]]

## References
- [GitHub - naver/splade: SPLADE: sparse neural search (SIGIR21, SIGIR22)](https://github.com/naver/splade)
