---
Title: Open Source LLM Observability Tools and Platforms
Slug: open-source-llm-observability-tools-and-platforms
Date: 2024-02-22
Modified: 2024-06-26
Start: 2024-02-22
tags: observability, mlops, llmops, llm, monitoring, model-monitoring, prompt-management, data-logging, model-logging
Category: Generative AI
Image: /images/head/observability_998_cr_640px.jpg
banner: "/images/head/observability_998_cr_640px.jpg"
Summary: Managing and monitoring the complex behavior of Large Language Models (LLMs) becomes increasingly crucial. LLMOps and LLM Observability provide essential tools for understanding and controlling these models, ensuring their safe and effective deployment. This article delves into the critical aspects of LLM Observability in the realm of generative AI.
Status: published
prompt:
---
<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [LLM Observability in the Context of LLMOps for Generative AI](#llm-observability-in-the-context-of-llmops-for-generative-ai)
- [What is LLM Observability?](#what-is-llm-observability)
- [Expected Functionalities of an LLM Observability Solution](#expected-functionalities-of-an-llm-observability-solution)
- [Open Source LLM Observability Tools and Platforms](#open-source-llm-observability-tools-and-platforms)
- [Non-open source](#non-open-source)
- [Other - related](#other---related)
- [References](#references)

<!-- /MarkdownTOC -->

<a id="llm-observability-in-the-context-of-llmops-for-generative-ai"></a>
## LLM Observability in the Context of LLMOps for Generative AI

AI is transforming the world, and one area where it has made significant strides is in generative models, particularly in the field of Large Language Models (LLMs) like GPT-3 and transformer models. However, as impressive as these models are, managing, monitoring, and understanding their behavior and output remains a challenge. Enter LLMOps, a new field focusing on the management and deployment of LLMs, and a key aspect of this is LLM Observability. 

- [LLM Observability in the Context of LLMOps for Generative AI](#llm-observability-in-the-context-of-llmops-for-generative-ai)
- [What is LLM Observability?](#what-is-llm-observability)
- [Expected Functionalities of an LLM Observability Solution](#expected-functionalities-of-an-llm-observability-solution)
- [Open Source LLM Observability Tools and Platforms](#open-source-llm-observability-tools-and-platforms)
- [Other - related](#other---related)
- [References](#references)

<!-- /MarkdownTOC -->

<a id="what-is-llm-observability"></a>
## What is LLM Observability?

LLM Observability is the ability to understand, monitor, and infer the internal state of an LLM from its external outputs. It encompasses several areas including model health monitoring, performance tracking, debugging, and evaluating model fairness and safety. 

In the context of LLMOps, LLM Observability is critical. LLMs are complex and can be unpredictable, producing outputs that range from harmless to potentially harmful or biased. It's therefore essential to have the right tools and methodologies for observing and understanding these models' behaviors in real-time, during training, testing, and after deployment.

<a id="expected-functionalities-of-an-llm-observability-solution"></a>
## Expected Functionalities of an LLM Observability Solution

1. **Model Performance Monitoring**: An observability solution should be able to track and monitor the performance of an LLM in real-time. This includes tracking metrics like accuracy, precision, recall, and F1 score, as well as more specific metrics like perplexity or token costs in the case of language models.

2. **Model Health Monitoring**: The solution should be capable of monitoring the overall health of the model, identifying and alerting on anomalies or potentially problematic patterns in the model's behavior.

3. **Debugging and Error Tracking**: If something does go wrong, the solution should provide debugging and error tracking functionalities, helping developers identify, trace, and fix issues.

4. **Fairness, Bias, and Safety Evaluation**: Given the potential for bias and ethical issues in AI, any observability solution should include features for evaluating fairness and safety, helping ensure that the model's outputs are unbiased and ethically sound.

5. **Interpretability**: LLMs can often be "black boxes", producing outputs without clear reasoning. A good observability solution should help make the model's decision-making process more transparent, providing insights into why a particular output was produced.

6. **Integration with Existing LLMOps Tools**: Finally, the solution should be capable of integrating with existing LLMOps tools and workflows, from model development and training to deployment and maintenance.

> LLM Observability is a crucial aspect of LLMOps for generative AI. It provides the **visibility** and **control** needed **to effectively manage, deploy, and maintain Large Language Models**, ensuring they **perform as expected, are free from bias, and are safe to use**.

<a id="open-source-llm-observability-tools-and-platforms"></a>
## Open Source LLM Observability Tools and Platforms

1. [Azure OpenAI Logger](https://github.com/aavetis/azure-openai-logger) - ![github stars shield](https://img.shields.io/github/stars/aavetis/azure-openai-logger.svg?logo=github) - "Batteries included" logging solution for your Azure OpenAI instance.

![Azure OpenAI Logger](https://github.com/aavetis/azure-openai-logger/raw/main/images/demo.gif)


2. [Deepchecks](https://github.com/deepchecks/deepchecks) - ![github stars shield](https://img.shields.io/github/stars/deepchecks/deepchecks.svg?logo=github) - Tests for Continuous Validation of ML Models & Data. Deepchecks is a Python package for comprehensively validating your machine learning models and data with minimal effort.
3. [Evidently](https://github.com/evidentlyai/evidently) - ![github stars shield](https://img.shields.io/github/stars/evidentlyai/evidently.svg?logo=github) - Evaluate and monitor ML models from validation to production.
4. [Giskard](https://github.com/Giskard-AI/giskard) - ![github stars shield](https://img.shields.io/github/stars/Giskard-AI/giskard.svg?logo=github) - Testing framework dedicated to ML models, from tabular to LLMs. Detect risks of biases, performance issues and errors in 4 lines of code.
5. [whylogs](https://github.com/whylabs/whylogs) - ![github stars shield](https://img.shields.io/github/stars/whylabs/whylogs.svg?logo=github) - The open standard for data logging
6. [lunary](https://github.com/lunary-ai/lunary) - ![github stars shield](https://img.shields.io/github/stars/lunary-ai/lunary.svg?logo=github) - The production toolkit for LLMs. observability, prompt management, and evaluations.
7. [openllmetry](https://github.com/traceloop/openllmetry) - ![github stars shield](https://img.shields.io/github/stars/traceloop/openllmetry.svg?logo=github) - Open-source observability for your LLM application, based on OpenTelemetry
8. [phoenix (Arize Ai)](https://github.com/Arize-ai/phoenix) - ![github stars shield](https://img.shields.io/github/stars/Arize-ai/phoenix.svg?logo=github) - AI Observability & Evaluation - Evaluate, troubleshoot, and fine-tune your LLM, CV, and NLP models in a notebook.
9. [langfuse](https://github.com/langfuse/langfuse) - ![github stars shield](https://img.shields.io/github/stars/langfuse/langfuse.svg?logo=github) - Open source LLM engineering platform. observability, metrics, evals, prompt management  SDKs + integrations for Typescript, Python
10. [LangKit](https://github.com/whylabs/langkit) - ![github stars shield](https://img.shields.io/github/stars/whylabs/langkit.svg?logo=github) - An open-source toolkit for monitoring Large Language Models (LLMs).  Extracts signals from prompts & responses, ensuring safety & security. Features include text quality, relevance metrics, & sentiment analysis. Comprehensive tool for LLM observability.
11. [agentops](https://github.com/AgentOps-AI/agentops) - ![github stars shield](https://img.shields.io/github/stars/AgentOps-AI/agentops.svg?logo=github) - Python SDK for agent evals and observability
12. [pezzo](https://github.com/pezzolabs/pezzo) - ![github stars shield](https://img.shields.io/github/stars/pezzolabs/pezzo.svg?logo=github) - Open-source, developer-first LLMOps platform designed to streamline prompt design, version management, instant delivery, collaboration, troubleshooting, observability and more.
13. [Fiddler AI](https://github.com/fiddler-labs/fiddler-auditor) - ![github stars shield](https://img.shields.io/github/stars/fiddler-labs/fiddler-auditor.svg?logo=github) - Evaluate, monitor, analyse, and improve machine learning and generative models from pre-production to production. Ship more ML and LLMs into production, and monitor ML and LLM metrics like hallucination, PII, and toxicity.
14. [OmniLog](https://github.com/Theodo-UK/OmniLog) - ![github stars shield](https://img.shields.io/github/stars/Theodo-UK/OmniLog.svg?logo=github) - Observability tool for your LLM prompts.

<a id="non-open-source"></a>
## Non-open source
- [Generative AI Studio - Galileo](https://docs.rungalileo.io/galileo/galileo-gen-ai-studio/llm-studio)

<a id="other---related"></a>
## Other - related
- [Great Expectations](https://github.com/great-expectations/great_expectations) - Always know what to expect from your data.
- [AgentOps-AI/tokencost](https://github.com/AgentOps-AI/tokencost) - Easy token price estimates for LLMs
- [observability prompts](https://github.com/YANG-DB/observability-prompots) - LLM observability related prompts
- [LLM Observability](https://github.com/AstronomerAmber/LLM_Observability) 
- [baml](https://github.com/BoundaryML/baml)  - A programming language to build strongly-typed LLM functions. Testing and observability included
- [aperture](https://github.com/fluxninja/aperture) - Rate limiting, caching, and request prioritization for modern workloads


<a id="references"></a>
## References
- [LLM Monitoring and Observability — A Summary of Techniques and Approaches for Responsible AI | by Josh Poduska | Towards Data Science](https://towardsdatascience.com/llm-monitoring-and-observability-c28121e75c2f)
- [Monitoring LLMs: Metrics, challenges, & hallucinations](https://www.aporia.com/learn/how-to-monitor-large-language-models/)
- [mattcvincent/intro-_llm_-_observability_](https://github.com/mattcvincent/intro-llm-observability) - Intro to LLM Observability
- [Demystifying Perplexity: An AI Expert‘s Comprehensive Guide - 33rd Square](https://www.33rdsquare.com/what-is-perplexity-ai/)
- [Perplexity - a Hugging Face Space by evaluate-metric](https://huggingface.co/spaces/evaluate-metric/perplexity)
- [List of top LLM Observability Tools](https://drdroid.io/engineering-tools/list-of-top-llm-observability-tools) - good intro


**Edits:**

- 2024-12-19: Added reference to list of top observability tools
- 2024-06-26: Added summary