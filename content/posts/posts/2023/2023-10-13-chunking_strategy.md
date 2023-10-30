---
Title: From Fixed-Size to NLP Chunking - A Deep Dive into Text Chunking Techniques
Slug: from-fixed-size-to-nlp-chunking-a-deep-dive-into-text-chunking-techniques
Date: 2023-09-11
Modified: 2023-10-13
Start: 2023-09-11
tags: chunking, text-processing, nlp, semantic-search, language-models, fixed-size-chunking, recursive-structure-aware-splitting, structure-aware-splitting, nlp-chunking, content-aware-splitting, metadata, summaries, keyword-tagging, sentiment-analysis, entity-recognition, topic-classification, chunk-linking, llm, rag
Category: Machine Learning
Image: /images/head/chunking_puzzle_640px.jpg
banner: "/images/head/chunking_puzzle_640px.jpg"
Summary: Discover text chunking - the secret sauce behind accurate search results and smarter language models! By understanding how to effectively chunk text, we can improve the way we index documents, handle user queries, and utilize search results. Ready to uncover the secrets of text chunking?
Status: published
prompt:
---

## Understanding Chunking

Chunking is a process that aims to embed a piece of content with as little noise as possible while maintaining semantic relevance[^2]. This process is particularly useful in semantic search, where we index a corpus of documents, each containing valuable information on a specific topic. 

An effective chunking strategy ensures that search results accurately capture the essence of a user's query. If our chunks are too small or too large, it may lead to imprecise search results or missed opportunities to surface relevant content. As a **rule of thumb**, if the **chunk of text makes sense without the surrounding context to a human**, it will likely make sense to the language model as well[^2]. Therefore, finding the optimal chunk size for the documents in the corpus is crucial to ensuring that the search results are accurate and relevant.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Factors Influencing Chunking Strategy](#factors-influencing-chunking-strategy)
	- [Size of the Texts to be Indexed](#size-of-the-texts-to-be-indexed)
	- [Length and Complexity of User Queries](#length-and-complexity-of-user-queries)
	- [Utilization of the Retrieved Results in the Application](#utilization-of-the-retrieved-results-in-the-application)
- [Chunking Methods](#chunking-methods)
	- [Fixed-size \(in characters\) Overlapping Sliding Window](#fixed-size-in-characters-overlapping-sliding-window)
	- [Fixed-size \(in tokens\) Overlapping Sliding Window](#fixed-size-in-tokens-overlapping-sliding-window)
	- [Recursive Structure Aware Splitting](#recursive-structure-aware-splitting)
	- [Structure Aware Splitting \(by Sentence, Paragraph, Section, Chapter\)](#structure-aware-splitting-by-sentence-paragraph-section-chapter)
	- [NLP Chunking: Tracking Topic Changes](#nlp-chunking-tracking-topic-changes)
	- [Content-Aware Splitting \(Markdown, LaTeX, HTML\)](#content-aware-splitting-markdown-latex-html)
	- [Adding Extra Context to the Chunk \(metadata, summaries\)](#adding-extra-context-to-the-chunk-metadata-summaries)
- [References](#references)
- [Further Reading](#further-reading)

<!-- /MarkdownTOC -->

<a id="factors-influencing-chunking-strategy"></a>
## Factors Influencing Chunking Strategy

There are three main factors to consider when determining a chunking strategy for a specific use case and application:

1. The size of the texts to be indexed and chunked
2. The length and complexity of user queries
3. The utilization of the retrieved results in the application

<a id="size-of-the-texts-to-be-indexed"></a>
### Size of the Texts to be Indexed

The chunking unit and size should be adjusted according to the nature of the text. The chunk should be long enough to contain the relevant semantic load. For instance, individual words may not convey a specific message or piece of information, while putting an entire encyclopedia in one chunk may result in a chunk that is "about everything."

<a id="length-and-complexity-of-user-queries"></a>
### Length and Complexity of User Queries

- **Longer queries** or those with greater complexity typically **benefit from a smaller chunk length**. This helps to narrow down the search space and improve the precision of the search results. Smaller chunks allow more focused matching against embeddings, reducing the impact of irrelevant parts within the query.
- **Shorter and simpler queries** might not require chunking at all, as they can be processed as a single unit. Chunking may introduce unnecessary overhead in these cases, potentially hampering search performance.

<a id="utilization-of-the-retrieved-results-in-the-application"></a>
### Utilization of the Retrieved Results in the Application

In cases where search results are only an intermediate step in the whole chain in the app, the size of the chunk might have significant importance for the seamless operation of the application. For example, if results from multiple search queries are the input context for the prompt to the LLM, having small chunks might ease fitting all inputs in the maximum allowed context size for a given LLM. Conversely, if the search result is presented to the user, larger chunks may be more appropriate.

<a id="chunking-methods"></a>
## Chunking Methods

There are several methods for chunking text, each with its own advantages and disadvantages. The choice of method depends on the specific requirements of the use case and application.

<a id="fixed-size-in-characters-overlapping-sliding-window"></a>
### Fixed-size (in characters) Overlapping Sliding Window

The Fixed-size overlapping sliding window method is a naive approach to text chunking, dividing the text into fixed-size pieces regarded as chunks. In this method, the text is divided based on the count of characters, making it straightforward to implement. The use of overlap in this method aids in preserving the integrity of sentences or thoughts, ensuring they are not cut in the middle. If one window truncates a thought, another window might contain the complete thought.

However, this method presents certain limitations. One significant drawback is the lack of precise control over the context size. Most language models operate on the basis of tokens rather than characters or words, making this method less efficient. The strict and fixed-size nature of the window might also result in severing words, sentences, or paragraphs in the middle, which could impede comprehension and disrupt the flow of information.

Furthermore, this method does not take semantics into account, providing no guarantee that the semantic unit of the text capturing a given idea or thought will be accurately encapsulated within a chunk. Consequently, one chunk may not be semantically distinct from another.

#### Use Cases

The Fixed-size overlapping sliding window method can be beneficial in certain scenarios. It is especially useful in preliminary exploratory data analysis, where the goal is to obtain a general understanding of the text structure rather than a deep semantic analysis. Additionally, it could be employed in scenarios where the text data does not have a strong semantic structure, such as in certain types of raw data or logs.

However, for tasks that require semantic understanding and precise context, such as sentiment analysis, question-answering systems, or text summarization, more sophisticated text chunking methods would be more appropriate.

#### Summary

**Pros:**
- Counting characters makes implementation easy
- Using overlap helps to avoid having sentences or thoughts cut in the middle - if one window is cutting the thought, perhaps another will have it in one piece.

**Cons:**
- Not precise control of the context size - models work and size the text in tokens not in characters or words
- Having a strict, fixed-size window might lead to cutting words, sentences, or paragraphs in the middle.
- Doesn't take semantics into account, no guarantee that the semantic unit of text capturing the given idea, thought will be accurately captured in the chunk and another chunk will be dedicated to another idea

**Use cases:**
- Preliminary exploratory data analysis where a general understanding of the text is required
- Scenarios where the text does not have a strong semantic structure, such as certain types of raw data or logs
- Not recommended for tasks requiring semantic understanding and precise contexts like sentiment analysis, question-answering systems, or text summarization

<a id="fixed-size-in-tokens-overlapping-sliding-window"></a>
### Fixed-size (in tokens) Overlapping Sliding Window

The Fixed-size sliding window method in tokens is another approach to text chunking. Unlike the character-based method, this approach divides the text into chunks based on the count of tokens that came out from the tokenizer, making it more aligned with the way language models operate.

In this method, the size of the context is more precisely controlled as it works on tokens rather than characters. A helpful rule of thumb is that one token generally corresponds to ~4 characters of text for common English text. This can make avoiding cutting words in the middle a little better than when counting characters, but the problem still persists. It can still sever sentences or thoughts in the middle, which could disrupt the flow of information. Moreover, similar to the character-based method, this approach does not take semantics into account. There's no guarantee that a chunk accurately captures a unique thought or idea, making the chunks potentially semantically inconsistent.

#### Where to Use It

The use cases are similar to the fixed size window based on characters count with one difference - when the count is based on tokens it works better for the tasks where we are limited by the LLM context size. 

#### Summary

**Pros:**
- More precise control over LLM context size as it operates on tokens, not characters.
- Still, relatively easy to implement

**Cons:**
- Can still sever sentences or thoughts in the middle
- Does not take semantics into account, hence no guarantee that a chunk accurately captures a unique thought or idea

**Use cases:**
- For exploratory, initial work with LLMs
- Not recommended for tasks requiring a deep understanding of the semantics and context of the text, like sentiment analysis or text summarization

<a id="recursive-structure-aware-splitting"></a>
### Recursive Structure Aware Splitting

Recursive Structure-aware Aware Splitting is a hybrid approach to text chunking, combining elements of the fixed-size sliding window method and the structure-aware splitting method. This method attempts to create chunks of approximately fixed sizes, either in characters or tokens, while also trying to preserve the original units of text such as words, sentences, or paragraphs.

In this method, the text is recursively split using various separators such as paragraph breaks ("\n\n"), new lines ("\n"), or spaces (" "), moving to the next level of granularity only when necessary. This allows the method to balance the need for a fixed chunk size with the desire to respect the natural linguistic boundaries of the text.

The major advantage of this method is its flexibility. It provides more precise control over context size compared to fixed-size methods, while also ensuring that semantic units of text are not unnecessarily severed.

However, this method also has its drawbacks. The complexity of implementation is higher due to the recursive nature of the splitting. There's also the risk of ending up with chunks of highly variable sizes, especially with texts of varying structural complexity.

> NOTE: [LangChain](https://www.langchain.com/) has an implementation of [Recursively split](https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/recursive_text_splitter)


#### Where to Use It

Recursive Structure Aware Splitting is particularly useful in tasks where both the granularity of tokens and the preservation of semantic integrity are crucial. This includes tasks such as text summarization, sentiment analysis, and document classification.

However, due to its complexity, it might not be the best fit for tasks that require quick and simple text chunking, or for tasks involving texts with inconsistent or unclear structural divisions.

#### Summary

**Pros:**
- Balances the need for fixed chunk sizes with the preservation of natural linguistic boundaries
- Provides more precise control over the context size

**Cons:**
- Higher complexity of implementation due to the recursive nature of the splitting
- Risk of ending up with chunks of highly variable sizes

**Use cases:**
- Useful in tasks where both the granularity of tokens and the preservation of semantic integrity are crucial, such as text summarization, sentiment analysis, and document classification
- Not recommended for tasks requiring quick and simple text chunking, or tasks involving texts with inconsistent or unclear structural divisions

<a id="structure-aware-splitting-by-sentence-paragraph-section-chapter"></a>
### Structure Aware Splitting (by Sentence, Paragraph, Section, Chapter)

Structure Aware Splitting is an advanced approach to text chunking, which takes into account the inherent structure of the text. Instead of using a fixed-size window, this method divides the text into chunks based on its natural divisions such as sentences, paragraphs, sections, or chapters.

This method is particularly beneficial as it respects the natural linguistic boundaries of the text, ensuring that words, sentences, and thoughts are not cut in the middle. This aids in preserving the semantic integrity of the information within each chunk.

However, this method does have certain limitations. Handling text of varying structural complexity might be challenging. For instance, some texts might not have clearly defined sections or chapters, e.g. text extracted from the OCR output, unformatted speech-to-text outputs, text extracted from tables. Also, while it's more semantically aware than the fixed-size methods, it still doesn't guarantee perfect semantic consistency within chunks, especially for larger structural units like sections or chapters.

#### Where to Use It

Structure Aware Splitting is highly effective for tasks that require a good understanding of the context and semantics of the text. It is particularly useful for text summarization, sentiment analysis, and document classification tasks.

However, it might not be the best fit for tasks involving texts that lack defined structural divisions, or for tasks that require a finer granularity, such as word-level Named Entity Recognition (NER).

#### Summary

**Pros:**

- Respects natural linguistic boundaries, avoiding severing words, sentences, or thoughts
- Preserves the semantic integrity of information within each chunk

**Cons:**

- Challenging to handle text with varying structural complexity
- Does not guarantee perfect semantic consistency within chunks, especially for larger structural units
- We don't have control over chunk size. Chunks from given document might significantly vary in the size.

**Use cases:**

- Effective for tasks requiring good understanding of context and semantics, such as text summarization, sentiment analysis, and document classification
- Not recommended for tasks involving texts that lack defined structural divisions, or tasks needing finer granularity, like word-level NER

<a id="nlp-chunking-tracking-topic-changes"></a>
### NLP Chunking: Tracking Topic Changes

NLP Chunking with Topic Tracking is a sophisticated approach to text chunking. This method divides the text into chunks based on semantic understanding, specifically by detecting significant shifts in the topics of sentences. If the topic of a sentence significantly differs from the topic of the previous chunk, this sentence is considered the beginning of a new chunk.

This method has the distinct advantage of maintaining semantic consistency within each chunk. By tracking the changes in topics, this method ensures that each chunk is semantically distinct from the others, thereby capturing the inherent structure and meaning of the text.

However, this method is not without its challenges. It requires advanced NLP techniques to accurately detect topic shifts, which adds to the complexity of implementation. Additionally, the accuracy of chunking heavily depends on the effectiveness of the topic modeling and detection techniques used.

![NLP Chunking](https://vectara.com/wp-content/uploads/2023/09/chunking-blog-post.png)

**Figure 2.** *Example of NLP chunking (source: [^4])*

#### Where to Use It

NLP Chunking with Topic Tracking is highly effective for tasks that require an understanding of the semantic context and topic continuity. It is particularly useful for text summarization, sentiment analysis, and document classification tasks.

This method might not be the best fit for tasks involving texts that have a high degree of topic overlap or for tasks that require simple text chunking without the need for deep semantic understanding.

#### Summary

**Pros:**

- Maintains semantic consistency within each chunk
- Captures the inherent structure and meaning of the text by tracking topic changes

**Cons:**

- Requires advanced NLP techniques, increasing the complexity of implementation
- The accuracy of chunking heavily depends on the effectiveness of the topic modeling and detection techniques used

**Use cases:**
- Highly effective for tasks requiring semantic context and topic continuity, such as text summarization, sentiment analysis, and document classification
- Not recommended for tasks involving texts with high degrees of topic overlap or tasks requiring simple text chunking without the need for deep semantic understanding

<a id="content-aware-splitting-markdown-latex-html"></a>
### Content-Aware Splitting (Markdown, LaTeX, HTML)

Content-Aware Splitting is a method of text chunking that focuses on the type and structure of the content, particularly in structured documents like those written in Markdown, LaTeX, or HTML. This method identifies and respects the inherent structure and divisions of the content, such as headings, code blocks, and tables, to create distinct chunks.

The primary advantage of this method is that it ensures different types of content are not mixed within a single chunk. For instance, a chunk containing a code block will not also contain a part of a table. This helps maintain the integrity and context of the content within each chunk.

However, this method also presents certain challenges. It requires understanding and parsing the specific syntax of the structured document format, which can increase the complexity of implementation. Moreover, it might not be suitable for documents that lack clear structural divisions or those written in plain text without any specific format.

#### Where to Use It

Content Aware Splitting is especially useful when dealing with structured documents or content with clear formatting, such as technical documentation, academic papers, or web pages. It helps ensure that the chunks created are meaningful and contextually consistent.

However, this method might not be the best fit for unstructured or plain text documents, or for tasks that do not require a deep understanding of the content structure.

#### Summary

**Pros:**

- Ensures different types of content are not mixed within a single chunk
- Respects and maintains the integrity and context of the content within each chunk

**Cons:**

- Requires understanding and parsing the specific syntax of the structured document format
- Might not be suitable for unstructured or plain text documents

**Where to Use It:**

- Particularly useful for structured documents or content with clear formatting, such as technical documentation, academic papers, or web pages
- Not recommended for unstructured or plain text documents, or tasks that do not require a deep understanding of the content structure

<a id="adding-extra-context-to-the-chunk-metadata-summaries"></a>
### Adding Extra Context to the Chunk (metadata, summaries)

Adding extra context to the chunks in the form of metadata or summaries can significantly enhance the value of each chunk and improve the overall understanding of the text[^3]. Here are two strategies:

#### Adding Metadata to Each Chunk

This strategy involves adding relevant metadata to each chunk. Metadata could include information such as the source of the text, the author, the date of publication, or even data about the content of the chunk itself, like its topic or keywords. This extra context can provide valuable insights and make the chunks more meaningful and easier to analyze.

> NOTE: In the case of the chunks that are vectorized using text embeddings,  be aware, that vector databases typically allow storage of metadata alongside the embedding vectors.

**Pros:**

- Provides additional information about each chunk
- Enhances the value of each chunk, making them more meaningful and easier to analyze
- Can help to produce more effective embeddings by fixing the broader context for the chunk.

**Cons:**

- Requires additional processing to generate and attach the metadata
- The usefulness of the metadata depends on its relevance and accuracy

**Where to Use It:**

- Especially useful in tasks that involve analyzing the origin, authorship, or content of the chunks, such as text classification, document clustering, or information retrieval
- Can be used to filter the sources used to provide context to LLMs.

#### Passing on Chunk Summaries

In this strategy, each chunk is summarized, and that summary is passed on to the next chunk. This method provides a 'running context' that can enhance the understanding of the text and maintain the continuity of information.
    
**Pros:**

- Enhances the understanding of the text by maintaining a running context
- Helps to ensure the continuity of information across chunks

**Cons:**

- Requires advanced NLP techniques to generate accurate and meaningful summaries
- The effectiveness of this method depends on the quality of the summaries

**Where to Use It:**

- Particularly useful in tasks where understanding the continuity and context of the text is crucial, such as text summarization or reading comprehension tasks

#### Other Experimental Strategies for Adding Context to the Chunks

1. **Keyword Tagging:** This method involves identifying and tagging the most important keywords or phrases in each chunk. These tags then serve as a quick reference or summary of the chunk's content. Advanced NLP techniques can be used to identify these keywords based on their relevance and frequency.
    
2. **Sentiment Analysis:** For text that contains opinions or reviews, performing sentiment analysis on each chunk and attaching the sentiment score (positive, negative, neutral) as metadata can provide valuable context. This can be particularly useful in tasks such as customer feedback analysis or social media monitoring.
    
3. **Entity Recognition:** Applying Named Entity Recognition (NER) techniques to each chunk can identify and label entities such as names of people, organizations, locations, expressions of times, quantities, monetary values, percentages, etc. This entity information can be added to each chunk, providing valuable context, especially in tasks like information extraction or knowledge graph construction.
    
4. **Topic Classification:** Each chunk can be classified into one or more topics using machine learning or NLP techniques. This topic label can provide a quick understanding of what each chunk is about, adding valuable context, especially for tasks like document classification or recommendation.
    
5. **Chunk Linking:** This method involves creating links between related chunks based on shared keywords, entities, or topics. These links can provide a 'map' of the content, showing how different chunks relate to each other. This can be particularly useful in tasks involving large and complex texts, where understanding the overall structure and relations between different parts is important.

## Conclusions

In the field of Natural Language Processing, text chunking emerges as a powerful technique that significantly enhances the performance of semantic search and language models. By breaking down text into manageable, contextually relevant chunks, we can ensure more accurate and meaningful search results.

The choice of chunking method, whether it's fixed-size, structure-aware, or NLP chunking, depends on the specific requirements of the use case and application. Each method has its own strengths and limitations, and understanding these is crucial to implementing an effective chunking strategy.

Moreover, adding extra context to the chunks, such as metadata or summaries, can further enhance the value of each chunk and improve the overall understanding of the text. Experimental strategies like keyword tagging, sentiment analysis, entity recognition, topic classification, and chunk linking offer promising avenues for further exploration.

*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*
<a id="references"></a>
## References
- [^1] [Create a CustomGPT And Supercharge your Company with AI  -  Pick the Best LLM - The Abacus.AI Blog](https://blog.abacus.ai/blog/2023/08/10/create-your-custom-chatgpt-pick-the-best-llm-that-works-for-you/)
- [^2] [Chunking Strategies for LLM Applications | Pinecone](https://www.pinecone.io/learn/chunking-strategies/)
- [^3] [Optimize LLM Enterprise Applications through Embeddings and Chunking Strategy. | by Actalyst | Aug, 2023 | Medium](https://actalyst.medium.com/optimize-llm-enterprise-applications-through-embeddings-and-chunking-strategy-1bbdb03bedae) 
- [^4] [Retrieval Augmented Generation (RAG) Done Right: Chunking - Vectara](https://vectara.com/grounded-generation-done-right-chunking/)

<a id="further-reading"></a>
## Further Reading

- [Simple guide to Text Chunking for Your LLM Applications | by NoCode AI | 𝐀𝐈 𝐦𝐨𝐧𝐤𝐬.𝐢𝐨 | Medium](https://medium.com/aimonks/simple-guide-to-text-chunking-for-your-llm-applications-bddfe8ad7892)
- [[2307.03172] Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [The length of the embedding contents - API - OpenAI Developer Forum](https://community.openai.com/t/the-length-of-the-embedding-contents/111471)
- [Building RAG-based LLM Applications for Production (Part 1)](https://www.anyscale.com/blog/a-comprehensive-guide-for-building-rag-based-llm-applications-part-1)
- expanding context, hierarchical search, ...: [Effects of Chunk Sizes on Retrieval Augmented Generation (RAG) Applications](https://reframe.is/wiki/Effects-of-Chunk-Sizes-on-Retrieval-Augmented-Generation-RAG-Applications-8b728c36d005434dba39ad19be9b82cc/)
- [A novel method for performance evaluation of text chunking | Language Resources and Evaluation](https://dl.acm.org/doi/10.1007/s10579-013-9250-3)
- [Matt Ambrogi](https://www.mattambrogi.com/posts/chunk-size-matters/) "Chunk Size Matters"


X::[[RAG_question_answering_deciding_on_the_strategies_Architecture]]
X::[[context_generation_strategy]]
X::[[2023-10-13-chunking_strategy]]
X::[[embedding_strategy]]
X::[[RAG_evaluation]]



