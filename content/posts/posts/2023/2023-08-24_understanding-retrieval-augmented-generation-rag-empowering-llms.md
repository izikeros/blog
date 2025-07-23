---
Title: Understanding Retrieval-Augmented Generation (RAG) empowering LLMs
Slug: understanding-retrieval-augmented-generation-rag-empowering-llms
Date: 2023-08-24
Modified: 2023-10-23
Start: 2023-08-24
tags: llm, nlp, question-answering, rag, re-ranking, embeddings, Transformers, seq2seq, prompt, pretrained-dense-retrieval
Category: Generative AI
Image: /images/head/rag_futuristic_library_640px.jpg
banner: "/images/head/rag_futuristic_library_640px.jpg"
Summary: Understand innovative artificial intelligence framework that empower large language models (LLMs) by anchoring them to external knowledge sources with accurate, current information.
Status: published
note: see RAG.excalidraw
---
## TLDR

Retrieval augmented generation refers to the method of enhancing a user's input to a large language model (LLM) such as ChatGPT by incorporating extra information obtained from an external source. This additional data can then be utilized by the LLM to enrich the response it produces.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Introduction: Understanding Retrieval-Augmented Generation \(RAG\)](#introduction-understanding-retrieval-augmented-generation-rag)
- [The Need for RAG in Large Language Models](#the-need-for-rag-in-large-language-models)
- [The 'Open Book' Approach of RAG](#the-open-book-approach-of-rag)
- [Personalized and Verifiable Responses with RAG](#personalized-and-verifiable-responses-with-rag)
- [Challenges and Future Directions](#challenges-and-future-directions)
- [Conclusion](#conclusion)
- [References](#references)

<!-- /MarkdownTOC -->

<a id="introduction-understanding-retrieval-augmented-generation-rag"></a>

## Introduction: Understanding Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation, commonly referred to as RAG, and sometimes called Grounded Generation (GG), represents an ingenious integration of pretrained dense retrieval (DPR) and [sequence-to-sequence](https://en.wikipedia.org/wiki/Seq2seq) models.

> Transformer architecture (used in GPT models) is a member of sequence-to-sequence (Seq2Seq) architectures. Seq2Seq models are designed to handle tasks that involve transforming an input sequence into an output sequence, such as machine translation, text summarization, and dialogue generation.

The process involves retrieving documents using DPR and subsequently transmitting them to a seq2seq model. Through a process of marginalization, these models then produce desired outputs. The retriever and seq2seq modules commence their operations as pretrained models, and through a joint fine-tuning process, they adapt collaboratively, thus enhancing both retrieval and generation for specific downstream tasks. **This innovative artificial intelligence framework serves as a means to empower large language models (LLMs) by anchoring them to external knowledge sources.** Consequently, this strategic approach ensures the availability of accurate, current information, thereby granting users valuable insights into the generative mechanisms of these models. For a comprehensive understanding of the RAG technique, we offer an in-depth exploration, commencing with a simplified overview and progressively delving into more intricate technical facets.

![Data processing in RAG](https://learn.microsoft.com/en-us/azure/machine-learning/media/concept-retrieval-augmented-generation/retrieval-augmented-generation-walkthrough.png?view=azureml-api-2#lightbox)

Figure 1. Data processing, storage and referencing in RAG method. Source: [Microsoft](https://learn.microsoft.com/en-us/azure/machine-learning/concept-retrieval-augmented-generation?view=azureml-api-2)

<a id="the-need-for-rag-in-large-language-models"></a>

## The Need for RAG in Large Language Models

Large language models, while powerful, can sometimes be inconsistent in their responses. They may provide accurate answers to certain questions but struggle with others, often regurgitating random facts from their training data. This inconsistency stems from the fact that LLMs understand the statistical relationships between words but not their actual meanings.

To address this issue, researchers have developed the RAG **framework, which improves the quality of LLM-generated responses by grounding the model in external sources of knowledge.** This approach not only ensures access to the most current and reliable facts but also allows users to verify the model's claims for accuracy and trustworthiness.

<a id="the-open-book-approach-of-rag"></a>

## The 'Open Book' Approach of RAG

RAG operates in **two main phases: retrieval and content generation**. During the retrieval phase, algorithms search for and retrieve relevant snippets of information based on the user's prompt or question. These facts can come from various sources, such as indexed documents on the internet or a closed-domain enterprise setting for added security and reliability.

In the generative phase, the LLM uses the retrieved information and its internal representation of training data to synthesize a tailored answer for the user.

> This approach is akin to an "open book" exam, where the model can browse through content in a book rather than relying solely on its memory.

![RAG Operation](/images/retrieval_augmented_generation/RAG.png)
Figure 2. RAG operation. Information preparation and storage. Augmenting prompt with external information.

<a id="personalized-and-verifiable-responses-with-rag"></a>

## Personalized and Verifiable Responses with RAG

RAG allows LLM-powered chatbots to provide more personalized answers without the need for human-written scripts. By reducing the need to continuously train the model on new data, RAG can lower the computational and financial costs of running LLM-powered chatbots in an enterprise setting.

Moreover, RAG enables LLMs to generate more specific, diverse, and factual language compared to traditional parametric-only seq2seq models. This feature is particularly useful for businesses that require up-to-date information and verifiable responses.

<a id="challenges-and-future-directions"></a>

## Challenges and Future Directions

Despite its advantages, RAG is not without its challenges. For instance, **LLMs may struggle to recognize when they don't know the answer** to a question, leading to incorrect or misleading information. To address this issue, researchers are working on fine-tuning LLMs to recognize unanswerable questions and probe for more detail until they can provide a definitive answer.

Furthermore, there is ongoing research to improve both the retrieval and generation aspects of RAG. This includes **finding and fetching the most relevant information possible and structuring that information** to elicit the richest responses from the LLM.

<a id="conclusion"></a>

## Conclusion

Retrieval-Augmented Generation offers a promising solution to the limitations of large language models by grounding them in external knowledge sources. By adopting RAG, businesses can achieve customized solutions, maintain data relevance, and optimize costs while harnessing the reasoning capabilities of LLMs. As research continues to advance in this area, we can expect even more powerful and efficient language models in the future.

*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*

<a id="references"></a>

## References

- Original paper [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) by Patrick Lewis et al. (available as [paper with code](https://paperswithcode.com/method/rag))
- Exemplary notebooks on amazon Sagemaker:
  - [Retrieval-Augmented Generation: Question Answering based on Custom Dataset](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/question_answering_jumpstart_knn.html)
  - [Retrieval-Augmented Generation: Question Answering based on Custom Dataset with Open-sourced LangChain Library](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/question_answering_langchain_jumpstart.html)
- Python library with RAG implementation: [GitHub - llmware-ai/llmware: Providing enterprise-grade LLM-based development framework, tools and fine-tuned models.](https://github.com/llmware-ai/llmware)
- Analytics: [Vectorview](https://www.vectorview.ai/)
- Deep-dive into specific use-case of RAG with scaling in mind: [Building RAG-based LLM Applications for Production (Part 1)](https://www.anyscale.com/blog/a-comprehensive-guide-for-building-rag-based-llm-applications-part-1)
- Good section on possible improvements to RAG: [Retrieval Augmented Generation (RAG): What, Why and How? | LLMStack](https://llmstack.ai/blog/retrieval-augmented-generation)
- General intro to RAG: [How do domain-specific chatbots work? An Overview of Retrieval Augmented Generation (RAG) | Scriv](https://scriv.ai/guides/retrieval-augmented-generation-overview/)
- Optimization, async, using summaries: [Secrets to Optimizing RAG LLM Apps for Better Performance, Accuracy and Lower Costs! | by Madhukar Kumar | madhukarkumar | Sep, 2023 | Medium](https://madhukarkumar.medium.com/secrets-to-optimizing-rag-llm-apps-for-better-accuracy-performance-and-lower-cost-da1014127c0a)
- Check the GitHub for the RAG-related projects: [retrieval-augmented-generation · GitHub Topics](https://github.com/topics/retrieval-augmented-generation?l=python)
- [Yet another RAG system - implementation details and lessons learned : r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/16cbimi/yet_another_rag_system_implementation_details_and/)
- [Building and Evaluating Advanced RAG Applications - DeepLearning.AI](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) - recent course from deeplearning.ai (Andrew Ng). Instructors: Jerry Liu and Anupam Datta.
  - In this course, we’ll explore:
    - Two advanced retrieval methods: Sentence-window retrieval and auto-merging retrieval that perform better compared to the baseline RAG pipeline.
    - Evaluation and experiment tracking: A way evaluate and iteratively improve your RAG pipeline’s performance.
    - The RAG triad: Context Relevance, Groundedness, and Answer Relevance, which are methods to evaluate the relevance and truthfulness of your LLM’s response.

X::[[2023-11-01-boosting_RAG]]

**Edits:**

- 2023-10-23: Added link to LLMStack
- 2023-11-06: Added TLDR section
- 2023-11-06: Added ToC
