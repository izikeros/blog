---
Title: RAG-Fusion - Enhancing Information Retrieval in Large Language Models
Slug: rag-fusion-enhancing-information-retrieval-in-large-language-models
Date: 2023-11-06
Modified: 2023-11-06
Status: published
tags: llm, information-retrieval, rag, re-ranking, semantic-search 
Category: note
---

In the realm of Large Language Models (LLMs) such as ChatGPT, a new technique known as Retrieval Augmented Generation (RAG) is gaining prominence. This technique is designed to enhance a user's input by incorporating additional information from an external source. This supplementary data is then leveraged by the LLM to enrich the response it generates. In this blog post, we will delve deeper into the core concept of RAG-fusion, which revolves around multiple query generation and re-ranking of results. For other methods that can improve RAG performance see my other [[2023-11-01-boosting_RAG|article]].

## What is RAG-fusion?

**The principle behind RAG-fusion is to generate multiple versions of the user's original query using a LLM, and then re-rank the results to select the most relevant retrieved parts.**

> NOTE: The term RAG in the name of the technique might be a bit misleading since "RAG-fusion" refers only to the first part of RAG - retrieval process.

How it works? For instance, the prompt template for this task might look something like this: "Generate multiple search queries related to: {original_query}", where `{original_query}` is a placeholder for the user's original query. This step enables the model to explore different perspectives and interpretations of the original query, thereby broadening the range of potential responses.

## Re-ranking: A Crucial Step

The next vital step in the RAG-fusion process is re-ranking. This step is critical in determining the most pertinent answers to the user's query. The re-ranking process, often referred to as [[posts/notes/implementing_reciprocal_rank_fusion_in_python|Reciprocal Rank Fusion (RRF)]], involves collecting ranked search outcomes from multiple strategies.

Each document is assigned a reciprocal rank score. These scores are then merged to create a new ranking. The underlying principle here is that documents that consistently appear in top positions across diverse search strategies are likely more pertinent and should, therefore, receive a higher rank in the consolidated result.

![RAG Fusion](https://miro.medium.com/v2/resize:fit:1400/1*tDALPmWxwAPf7UADpZwjWQ@2x.jpeg)
Figure 1. RAG fusion proces flow for ranking four documents A, B, C, D against three retrieval sources (can be three variants of the original user query). Source of image: [Forget RAG, the Future is RAG-Fusion article by Adrian H. Raudaschl](https://towardsdatascience.com/forget-rag-the-future-is-rag-fusion-1147298d8ad1)

## Why RAG-fusion Matters?

It provides a boost to the LLM's ability to generate more accurate, contextually relevant responses. By considering multiple interpretations of the original query and re-ranking the results, it ensures that the model's output is as closely aligned with the user's intent as possible.

RAG-fusion might be a powerful technique that brings together the strengths of large language models and advanced information retrieval strategies. By employing multiple query generation and re-ranking, it takes a leap towards making AI-powered systems more responsive, accurate, and user-friendly.

**NOTE 1:** For more methods that can improve RAG performance see my other [[2023-11-01-boosting_RAG|article]].
**NOTE 2:** This technique is also referred as Query-Rewriting. You can find a section on that on LlamaIndex documentation ([Query Transformation Cookbook](https://docs.llamaindex.ai/en/stable/examples/query_transformations/query_transform_cookbook.html))

- X::[[2023-08-24_understanding-retrieval-augmented-generation-rag-empowering-llms]]
- X::[[posts/notes/implementing_reciprocal_rank_fusion_in_python]]

up::[[MOC_RAG]]

**Edits:**

- 2024-03-06: Added RAG fusion paper
- 2024-02-01: Add reference to LLamaIndex Query Transform Cookbook

## References
- [RAG-Fusion: a New Take on Retrieval-Augmented Generation](https://arxiv.org/html/2402.03367v2)
- [GitHub - Raudaschl/rag-fusion](https://github.com/Raudaschl/rag-fusion/tree/master) - exemplary implementation
- [Forget RAG, the Future is RAG-Fusion | by Adrian H. Raudaschl | Oct, 2023 | Towards Data Science](https://towardsdatascience.com/forget-rag-the-future-is-rag-fusion-1147298d8ad1)
- RAG-fusion in LangChain: [usage](https://python.langchain.com/docs/templates/rag-fusion), template [code](https://github.com/langchain-ai/langchain/tree/master/templates/rag-fusion)
- [Query Transformation Cookbook](https://docs.llamaindex.ai/en/stable/examples/query_transformations/query_transform_cookbook.html)
