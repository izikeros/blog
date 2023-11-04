---
Title: Problems with Langchain and how to minimize their impact
Slug: problems-with-Langchain-and-how-to-minimize-their-impact
Date: 2023-09-01
Modified: 2023-10-19
Start: 2023-09-01
tags: machine-learning, python, langchain, prompt-engineering, tokens, llm, gpt, openai
Category: Generative AI
Image: /images/head/langchain_problems.jpg
banner: "/images/head/langchain_problems.jpg"
Summary: Beyond the Hype - LangChain's Hidden Flaws and How to Master AI Development.
Status: published
prompt:
---

## Introduction

[LangChain](https://docs.langchain.com/docs/), a popular framework for building applications with [large language models](https://en.wikipedia.org/wiki/Large_language_model) (LLMs), has been touted as a game-changer in the world of AI-driven development. However, as more users dive into the library and its capabilities, some have found that it falls short of expectations. In this section, we'll discuss ten issues with LangChain that have left users underwhelmed and questioning its value proposition.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Problems](#problems)
	- [1. Overly complex and unnecessary abstractions](#1-overly-complex-and-unnecessary-abstractions)
	- [2. Easy breakable and unreliable](#2-easy-breakable-and-unreliable)
	- [3. Poor documentation](#3-poor-documentation)
	- [4. A high level of abstraction hinders customization](#4-a-high-level-of-abstraction-hinders-customization)
	- [5. Inefficient token usage](#5-inefficient-token-usage)
	- [6. Difficult integration with existing tools](#6-difficult-integration-with-existing-tools)
	- [7. Limited value proposition](#7-limited-value-proposition)
	- [8. Inconsistent behavior and hidden details](#8-inconsistent-behavior-and-hidden-details)
	- [9. Better alternatives available](#9-better-alternatives-available)
	- [10. Primarily optimized for demos](#10-primarily-optimized-for-demos)
- [Takeaways - How to Use the LangChain Right Way?](#takeaways---how-to-use-the-langchain-right-way)
- [Conclusion](#conclusion)

<!-- /MarkdownTOC -->

<a id="problems"></a>
## Problems

<a id="1-overly-complex-and-unnecessary-abstractions"></a>
### 1. Overly complex and unnecessary abstractions
LangChain has been criticized for having too many layers of abstraction, making it difficult to understand and modify the underlying code. These layers can lead to confusion, especially for those who are new to LLMs or LangChain itself. The complexity can also make it challenging to adapt the library to specific use cases or integrate it with existing tools and scripts. In some cases, users have found that they can achieve their goals more easily by using simpler, more straightforward code.

<a id="2-easy-breakable-and-unreliable"></a>
### 2. Easy breakable and unreliable
Some users have found LangChain to be unreliable and difficult to fix due to its complex structure. The framework's fragility can lead to unexpected issues in production systems, making it challenging to maintain and scale applications built with LangChain. Users have reported that the deeper and more complex their application becomes, the more LangChain seems to become a risk to its maintainability.

<a id="3-poor-documentation"></a>
### 3. Poor documentation
LangChain's documentation has been described as confusing and lacking in key details, making it challenging for users to fully understand the library's capabilities and limitations. The documentation often omits explanations of default parameters and important details, leaving users to piece together information from various sources. This lack of clarity can hinder users' ability to effectively leverage LangChain in their projects.

<a id="4-a-high-level-of-abstraction-hinders-customization"></a>
### 4. A high level of abstraction hinders customization
Users have reported that LangChain's high level of abstraction makes it difficult to modify and adapt the library for specific use cases. This can be particularly problematic when users want to make small changes to the default behavior of LangChain or integrate it with other tools and scripts. In these cases, users may find it easier to bypass LangChain altogether and build their own solutions from scratch.

<a id="5-inefficient-token-usage"></a>
### 5. Inefficient token usage
LangChain has been criticized for inefficient token usage in its API calls, which can result in higher costs. This can be particularly problematic for users who are trying to minimize their expenses while working with LLMs. Some users have found that they can achieve better results with fewer tokens by using custom Python code or other alternative libraries.

<a id="6-difficult-integration-with-existing-tools"></a>
### 6. Difficult integration with existing tools
Users have reported difficulties integrating LangChain with their existing Python tools and scripts. This can be especially challenging for those who have complex analytics or other advanced functionality built into their applications. The high level of abstraction in LangChain can make it difficult to interface with these existing tools, forcing users to build workarounds or abandon LangChain in favor of more compatible solutions.

<a id="7-limited-value-proposition"></a>
### 7. Limited value proposition
Some users feel that LangChain does not provide enough value compared to the effort required to implement and maintain it. They argue that the library's primary use case is to quickly create demos or prototypes, rather than building production-ready applications. In these cases, users may find it more efficient to build their own solutions or explore alternative libraries that offer a better balance of ease of use and functionality.

<a id="8-inconsistent-behavior-and-hidden-details"></a>
### 8. Inconsistent behavior and hidden details
LangChain has been criticized for hiding important details and having inconsistent behavior, which can lead to unexpected issues in production systems. Users have reported that LangChain's default settings and behaviors are often undocumented or poorly explained, making it difficult to predict how the library will behave in different scenarios. This lack of transparency can lead to frustration and wasted time troubleshooting issues that could have been avoided with better documentation.

<a id="9-better-alternatives-available"></a>
### 9. Better alternatives available
Users have mentioned other libraries, such as [Semantic Kernel](https://github.com/microsoft/semantic-kernel), [LlamaIndex](https://github.com/jerryjliu/llama_index), [Deepset Haystack](https://haystack.deepset.ai/) , or [SuperAGI](https://github.com/TransformerOptimus/SuperAGI), as more suitable alternatives to LangChain. These alternatives often provide clearer documentation, more flexible customization options, and better integration with existing tools and scripts. In some cases, users have found that they can achieve their goals more easily and efficiently by using these alternative libraries instead of LangChain. See [awesome-langchain](https://github.com/kyrolabs/awesome-langchain#other-llm-frameworks) for a list of LLM frameworks.

<a id="10-primarily-optimized-for-demos"></a>
### 10. Primarily optimized for demos
LangChain has been described as being primarily optimized for quickly creating demos, rather than for building production-ready applications. [Partnership](https://blog.streamlit.io/langchain-streamlit/) with [Streamlit](https://streamlit.io/generative-ai?ref=blog.streamlit.io) should ease demo creation even more. While this can be useful for those who want to quickly experiment with LLMs or showcase their ideas, it can be limiting for users who want to build more robust, scalable applications. In these cases, users may find that LangChain's focus on demos and prototypes hinders their ability to build high-quality, production-ready applications.

<a id="takeaways---how-to-use-the-langchain-right-way"></a>
## Takeaways - How to Use the LangChain Right Way?
Based on the community comments and experiences shared, here are some pieces of advice on how to create apps using LangChain that will be reliable, easy to maintain and debug:

1. **Use LangChain for prototyping and experimentation**: LangChain can be useful for quickly creating prototypes and validating ideas. However, for more complex and production-level applications, you might want to consider implementing the functionality you need yourself.

2. **Understand the underlying concepts**: Before using LangChain, make sure to understand the core concepts of LLMs, prompts, and how the different components of the framework interact. This will help you make informed decisions about which parts of LangChain to use and which to replace with custom implementations.

3. **Focus on the value of the ecosystem**: LangChain provides integrations with various tools, indexes, and prompt templates. Leverage these resources to build your application, but be aware of the limitations and potential issues that might arise from using the default settings and abstractions.

4. **Be prepared to write custom code**: LangChain might not cover all use cases or provide the level of control and customization you need for your application. Be prepared to write custom code to better suit your specific requirements and use case.

5. **Keep an eye on alternative tools and libraries**: As the field of LLMs is rapidly evolving, new tools and libraries are being developed that might better suit your needs. Stay informed about the latest developments and consider using alternative libraries like [Deepset Haystack](https://haystack.deepset.ai/), [DSPy](https://github.com/stanfordnlp/dspy) , or Microsoft tools like [semantic-kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/) and [AutoGen](https://github.com/microsoft/autogen) if they better align with your project requirements. The [list](https://github.com/kyrolabs/awesome-langchain#other-llm-frameworks) is huge and growing!

6. **Learn from LangChain's source code**: If you find that LangChain's abstractions and documentation are not sufficient for your needs, you can learn from the source code itself. Use the provided prompts and implementation details as inspiration and adapt them to your own project.

7. **Consider local LLM models**: While LangChain primarily focuses on using OpenAI's models, you might want to explore using local LLM models like Llama, Galpaca, Vicuna, or Koala. These models can offer benefits in terms of cost, privacy, and offline capabilities. However, be aware that they might not be as powerful or accurate as GPT-3.5 Turbo.

8. **Integrate with existing tools and scripts**: If you need to interface with existing Python tools or scripts, make sure to understand how LangChain interacts with them and how you can best integrate them into your application.

9. **Test and measure the performance of your application**: When using LangChain, ensure that you thoroughly test your application and measure its performance against different prompts and configurations. This will help you identify potential issues and areas for improvement.

10. **Keep an eye on the costs**: Be mindful of the API costs associated with using LangChain and consider optimizing your application to reduce the number of API calls and tokens used.

My favourite choice from this list would be #6 - to learn from the LangChain implemented tools and techniques by looking into the code.

*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*

<a id="conclusion"></a>
## Conclusion
In considering LangChain, it's vital to acknowledge its limitations and challenges before embracing it enthusiastically. Although LangChain has garnered significant attention and investment, users have pinpointed various drawbacks that could impede its effectiveness in more intricate, production-ready applications. To make well-informed decisions about LangChain's suitability for their projects, developers should gain an understanding of these issues.
In the ever-evolving landscape of LLM-driven development, assessing the available tools and libraries is crucial to determining which aligns best with your specific needs and requirements. It's worth noting that the ideal solution might not yet exist, necessitating adaptation or customization of existing tools or even the creation of your own to realize your vision for AI-driven applications.

**edits:**

- 2023-10-19: Added AutoGen and semantic-kernel, removed GPTi,
- 2023-10-19: Added link to list of alternative frameworks