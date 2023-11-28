---
Title: Techniques to Boost RAG Performance in Production
Slug: techniques-to-boost-rag-performance-in-production
Date: 2023-11-01
Modified: 2023-11-04
Start: 2023-10-27
tags: machine-learning, python, rag, llm, retrieval-augmented-generation, re-reanking, 
Category: Generative AI
Image: /images/head/boosting_RAG.jpg
banner: "/images/head/boosting_RAG.jpg"
Summary: This article discusses several advanced techniques that can be applied at different stages of the RAG pipeline to enhance its performance in a production setting.
Status: published
prompt:
---
Retrieval-Augmented Generation (RAG) is a powerful tool in the domain of machine learning, offering significant potential for improving the quality of text generation in various applications. However, optimizing its performance can be a challenging task. For the introductory text on RAG see my other [article](https://safjan.com/understanding-retrieval-augmented-generation-rag-empowering-llms/). This article discusses several advanced techniques that can be applied at different stages of the RAG pipeline to enhance its performance in a production setting.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Leveraging Hybrid Search](#leveraging-hybrid-search)
- [Utilizing Summaries for Data Chunks](#utilizing-summaries-for-data-chunks)
- [Applying Query Transformations](#applying-query-transformations)
- [Query Compression](#query-compression)
- [Optimal Chunking Strategy](#optimal-chunking-strategy)
- [Fine-tuning Embedding Models](#fine-tuning-embedding-models)
- [Enriching Metadata](#enriching-metadata)
- [Employing Re-ranking](#employing-re-ranking)
- [Addressing the 'Lost in the Middle' Problem](#addressing-the-lost-in-the-middle-problem)
- [Meta-data Filtering](#meta-data-filtering)
- [Query Routing](#query-routing)
- [References](#references)

<!-- /MarkdownTOC -->

<a id="leveraging-hybrid-search"></a>
## Leveraging Hybrid Search

Hybrid search, a fusion of semantic search and keyword search, can be employed to retrieve pertinent data from a vector store. This method often yields superior results across a range of use cases. It essentially combines the strength of keyword search (precision) and semantic search (recall), providing a more comprehensive search solution.
[[hybrid_search]]

<a id="utilizing-summaries-for-data-chunks"></a>
## Utilizing Summaries for Data Chunks

An efficient way to enhance the quality of generation and reduce the number of tokens in the input is by summarizing the chunks of data and storing these summaries in the vector store. This technique is especially useful when dealing with data that includes numerous filler words. By summarizing the chunks, we can eliminate these superfluous elements, thereby refining the quality of the input data.
<a id="query-compression"></a>

<a id="applying-query-transformations"></a>
## Applying Query Transformations

Query transformations can significantly enhance the quality of responses. For instance, if a system does not find relevant context for a query, the LLM can rephrase the query and try again. See the [[rag_fussion|RAG Fusion]].

Similarly, the [HyDE](http://boston.lti.cs.cmu.edu/luyug/HyDE/HyDE.pdf) strategy generates a hypothetical response to a query and uses both for embedding lookup, which has been found to dramatically enhance performance. 

Another technique involves breaking down complex queries into sub-queries, a process that LLMs tend to handle better. This approach can be integrated into the RAG system to decompose a query into multiple simpler questions.

<a id="query-compression"></a>
## Query Compression

Query compression, (see a tool like [LongLLMLingua](https://www.microsoft.com/en-us/research/project/llmlingua/longllmlingua/)) is a technique for improving RAG's performance in long context scenarios where large language models often face challenges such as increased computational and financial costs, longer latency, and inferior performance. By enhancing the density and optimizing the position of key information in the input prompt, LongLLMLingua improves LLMs' perception of key information, which in turn, reduces computational load, decreases latency, and improves performance. This strategy ensures that vital information is not lost or diluted in lengthy contexts, thereby enhancing the relevance and quality of the generated output.
<a id="optimal-chunking-strategy"></a>
## Optimal Chunking Strategy

There are multiple strategies that can be applied to chunking see [Chunking strategies](https://safjan.com/from-fixed-size-to-nlp-chunking-a-deep-dive-into-text-chunking-techniques/#from-fixed-size-to-nlp-chunking-a-deep-dive-into-text-chunking-techniques). One of the aspects can be controlling the chunk overlap. Semantic retrieval may pose a challenge when a selected chunk has meaningful context in adjacent chunks that could be missed. To mitigate this, an overlap of chunks can be implemented, whereby neighboring chunks are also passed to the Language Model (LLM) for generation. This guarantees that the surrounding context is incorporated, thus enhancing the output's quality.

<a id="fine-tuning-embedding-models"></a>
## Fine-tuning Embedding Models

While off-the-shelf embedding models such as BERT and Ada may suffice for many use cases, they might not adequately represent specific domains in the vector space, leading to suboptimal retrieval quality. In such instances, it would be advantageous to fine-tune an embedding model using domain-specific data to significantly improve retrieval quality.

<a id="enriching-metadata"></a>
## Enriching Metadata

The provision of metadata like source information about the chunks being processed can enhance the LLM's comprehension of the context, leading to a better output generation. This additional layer of information can provide the LLM with a more holistic understanding of the data, enabling it to generate more accurate and relevant responses.

<a id="employing-re-ranking"></a>
## Employing Re-ranking

Semantic search may yield top-k results that are too similar to each other. To ensure a wider array of snippets, it is beneficial to [re-rank](https://www.sbert.net/examples/applications/retrieve_rerank/README.html) the results based on other factors such as metadata and keyword matches. This diversification of snippets can lead to a more nuanced and comprehensive context for the LLM to generate responses. Re-ranker can be based on a cross-encoder.

<a id="addressing-the-lost-in-the-middle-problem"></a>
## Addressing the 'Lost in the Middle' Problem

LLMs tend not to assign equal weight to all tokens in the input, often overlooking tokens located in the middle. This phenomenon, known as the ['lost in the middle' problem](https://arxiv.org/abs/2307.03172), can be addressed by reordering the context snippets to place the most vital snippets at the beginning and end of the input, with less important snippets situated in the middle.

<a id="meta-data-filtering"></a>
## Meta-data Filtering

Meta-data, such as date tags, can be added to your chunks to improve retrieval. For example, filtering by recency can be beneficial when querying email history. Recent emails may not necessarily be the most similar from an embedding standpoint, but they are more likely to be relevant. 

<a id="query-routing"></a>
## Query Routing

Having multiple indexes and routing queries to the appropriate index can be beneficial. For instance, different indexes could handle summarization questions, pointed questions, and date-sensitive questions. Trying to optimize one index for all these behaviors may compromise its effectiveness. 

In conclusion, the performance of RAG in production can be significantly improved by applying a range of techniques, including hybrid search, chunk summarization, overlapping chunks, fine-tuned embedding models, metadata enhancement, re-ranking, addressing the 'lost in the middle' problem, query transformations, meta-data filtering, and query routing. These strategies will help to optimize the RAG pipeline, ensuring higher quality output and improved overall performance.

<a id="references"></a>
## References
1. [Retrieval Augmented Generation (RAG): What, Why and How? | LLMStack](https://llmstack.ai/blog/retrieval-augmented-generation)
2. [[2307.03172] Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
3. [10 Ways to Improve the Performance of Retrieval Augmented Generation Systems | by Matt Ambrogi | Sep, 2023 | Towards Data Science](https://towardsdatascience.com/10-ways-to-improve-the-performance-of-retrieval-augmented-generation-systems-5fa2cee7cd5c)
4. Hypothetical Document Embeddings (HyDE) - [Precise Zero-Shot Dense Retrieval without Relevance Labels](http://boston.lti.cs.cmu.edu/luyug/HyDE/HyDE.pdf)
5. [Retrieve & Re-Rank — Sentence-Transformers documentation](https://www.sbert.net/examples/applications/retrieve_rerank/README.html)
6. [Improving RAG effectiveness with Retrieval-Augmented Dual Instruction Tuning (RA-DIT) | by Emanuel Ferreira | Oct, 2023 | LlamaIndex Blog](https://blog.llamaindex.ai/improving-rag-effectiveness-with-retrieval-augmented-dual-instruction-tuning-ra-dit-01e73116655d)
7. [Improving RAG (Retrieval Augmented Generation) Answer Quality with Re-ranker | by Shivam Solanki | Towards Generative AI | Medium](https://medium.com/towards-generative-ai/improving-rag-retrieval-augmented-generation-answer-quality-with-re-ranker-55a19931325)
8. SingleStore (db), finetuning embeddings model, CacheGPT, Nemo-Guardrails, [Secrets to Optimizing RAG LLM Apps for Better Performance, Accuracy and Lower Costs! | by Madhukar Kumar | madhukarkumar | Sep, 2023 | Medium](https://madhukarkumar.medium.com/secrets-to-optimizing-rag-llm-apps-for-better-accuracy-performance-and-lower-cost-da1014127c0a)
	1. [ run-llama/finetune-embedding: Fine-Tuning Embedding for RAG with Synthetic Data](https://github.com/run-llama/finetune-embedding)
	2. [zilliztech/GPTCache: Semantic cache for LLMs. Fully integrated with LangChain and llama\_index.](https://github.com/zilliztech/GPTCache)
	3. [NVIDIA/NeMo-Guardrails: NeMo Guardrails is an open-source toolkit for easily adding programmable guardrails to LLM-based conversational systems.](https://github.com/NVIDIA/NeMo-Guardrails)
	4. library to evaluate the context retrieved from your enterprise corpus of data (how do you know if the context being retrieved is accurate) [GitHub - explodinggradients/ragas: Evaluation framework for your Retrieval Augmented Generation (RAG) pipelines](https://github.com/explodinggradients/ragas)
	5.  LangSmith, introduced by LangChain - a highly effective tool for monitoring and examining the responses between the app and the LLM.

X::[[RAG_question_answering_deciding_on_the_strategies_Architecture]]





