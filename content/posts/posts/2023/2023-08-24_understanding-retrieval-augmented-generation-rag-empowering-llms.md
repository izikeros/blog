---
Title: Understanding Retrieval-Augmented Generation (RAG) empowering LLMs
Slug: understanding-retrieval-augmented-generation-rag-empowering-llms
Date: 2023-08-24
Modified: 2023-08-24
Start: 2023-08-24
Tags: llm, nlp, question-answering 
Category: Machine Learning
Image: /images/head/abstract_9.jpg
banner: "/images/head/abstract_9.jpg"
Summary: Understand innovative artificial intelligence framework that empower large language models (LLMs) by anchoring them to external knowledge sources with accurate, current information.
Status: published
note: see RAG.excalidraw
---
## Introduction: Understanding Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation, commonly referred to as RAG, and sometimes called Grounded Generation (GG), represents an ingenious integration of pretrained dense retrieval (DPR) and [sequence-to-sequence](https://en.wikipedia.org/wiki/Seq2seq) models. 

> Transformer architecture (used in GPT models) is a member of sequence-to-sequence (Seq2Seq) architectures. Seq2Seq models are designed to handle tasks that involve transforming an input sequence into an output sequence, such as machine translation, text summarization, and dialogue generation.


The process involves retrieving documents using DPR and subsequently transmitting them to a seq2seq model. Through a process of marginalization, these models then produce desired outputs. The retriever and seq2seq modules commence their operations as pretrained models, and through a joint fine-tuning process, they adapt collaboratively, thus enhancing both retrieval and generation for specific downstream tasks. **This innovative artificial intelligence framework serves as a means to empower large language models (LLMs) by anchoring them to external knowledge sources.** Consequently, this strategic approach ensures the availability of accurate, current information, thereby granting users valuable insights into the generative mechanisms of these models. For a comprehensive understanding of the RAG technique, we offer an in-depth exploration, commencing with a simplified overview and progressively delving into more intricate technical facets.

![Data processing in RAG](https://learn.microsoft.com/en-us/azure/machine-learning/media/concept-retrieval-augmented-generation/retrieval-augmented-generation-walkthrough.png?view=azureml-api-2#lightbox)

Figure 1. Data processing, storage and referencing in RAG method. Source: [Microsoft](https://learn.microsoft.com/en-us/azure/machine-learning/concept-retrieval-augmented-generation?view=azureml-api-2)

## The Need for RAG in Large Language Models

Large language models, while powerful, can sometimes be inconsistent in their responses. They may provide accurate answers to certain questions but struggle with others, often regurgitating random facts from their training data. This inconsistency stems from the fact that LLMs understand the statistical relationships between words but not their actual meanings.

To address this issue, researchers have developed the RAG **framework, which improves the quality of LLM-generated responses by grounding the model in external sources of knowledge.** This approach not only ensures access to the most current and reliable facts but also allows users to verify the model's claims for accuracy and trustworthiness.

## The 'Open Book' Approach of RAG

RAG operates in **two main phases: retrieval and content generation**. During the retrieval phase, algorithms search for and retrieve relevant snippets of information based on the user's prompt or question. These facts can come from various sources, such as indexed documents on the internet or a closed-domain enterprise setting for added security and reliability.

In the generative phase, the LLM uses the retrieved information and its internal representation of training data to synthesize a tailored answer for the user. 

> This approach is akin to an "open book" exam, where the model can browse through content in a book rather than relying solely on its memory.

![RAG Operation](/images/retrieval_augmented_generation/RAG.png)
Figure 2. RAG operation. Information preparation and storage. Augmenting prompt with external information.

## Personalized and Verifiable Responses with RAG

RAG allows LLM-powered chatbots to provide more personalized answers without the need for human-written scripts. By reducing the need to continuously train the model on new data, RAG can lower the computational and financial costs of running LLM-powered chatbots in an enterprise setting.

Moreover, RAG enables LLMs to generate more specific, diverse, and factual language compared to traditional parametric-only seq2seq models. This feature is particularly useful for businesses that require up-to-date information and verifiable responses.

## Challenges and Future Directions

Despite its advantages, RAG is not without its challenges. For instance, **LLMs may struggle to recognize when they don't know the answer** to a question, leading to incorrect or misleading information. To address this issue, researchers are working on fine-tuning LLMs to recognize unanswerable questions and probe for more detail until they can provide a definitive answer.

Furthermore, there is ongoing research to improve both the retrieval and generation aspects of RAG. This includes **finding and fetching the most relevant information possible and structuring that information** to elicit the richest responses from the LLM.

## Conclusion

Retrieval-Augmented Generation offers a promising solution to the limitations of large language models by grounding them in external knowledge sources. By adopting RAG, businesses can achieve customized solutions, maintain data relevance, and optimize costs while harnessing the reasoning capabilities of LLMs. As research continues to advance in this area, we can expect even more powerful and efficient language models in the future.

## References
- Original paper [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) by Patrick Lewis et al. (available as [paper with code](https://paperswithcode.com/method/rag))
- Exemplary notebooks on amazon Sagemaker:
	- [Retrieval-Augmented Generation: Question Answering based on Custom Dataset](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/question_answering_jumpstart_knn.html)
	- [Retrieval-Augmented Generation: Question Answering based on Custom Dataset with Open-sourced LangChain Library](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/question_answering_langchain_jumpstart.html)
- Python library with RAG implementation: [GitHub - llmware-ai/llmware: Providing enterprise-grade LLM-based development framework, tools and fine-tuned models.](https://github.com/llmware-ai/llmware)
- Analytics: [Vectorview](https://www.vectorview.ai/)
- Deep-dive into specific use-case of RAG with scaling in mind: [Building RAG-based LLM Applications for Production (Part 1)](https://www.anyscale.com/blog/a-comprehensive-guide-for-building-rag-based-llm-applications-part-1)


