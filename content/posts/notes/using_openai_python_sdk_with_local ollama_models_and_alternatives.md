---
Category: note
Date: 2025-07-29
Modified: 2025-07-29
Slug: openai-python-sdk-with-local-ollama-models-and-alternatives
Status: published
Summary: Learn how to use the official `openai` Python package with local Ollama models and when it's better to opt for LiteLLM as a more unified alternative.
ai_summary: true
Tags:
  - openai
  - openai-sdk
  - ollama
  - litellm
  - langchain
  - llama-index
  - guidance
  - instructor
Title: Using OpenAI Python SDK with Local Ollama Models (and When to Opt for Alternatives)
---
I've been diving into how to use the official `openai` Python package to **talk to local Ollama models**—and when it makes sense to bring in abstraction layers like **LiteLLM**. Let me walk you through what I learned.

### 1. Can I use the OpenAI Python package for local Ollama models?

**Yes!** Since early February 2024, Ollama supports the **OpenAI Chat Completions API**, exposing compatible endpoints locally. You can simply point the OpenAI client at `"http://localhost:11434/v1"`, pass a dummy API key, and call completions just like you would to OpenAI’s hosted API (see [Ollama blog](https://ollama.com/blog/openai-compatibility?utm_source=chatgpt.com "OpenAI compatibility · Ollama Blog")).

```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="unused-key")

response = client.chat.completions.create(
  model="llama2",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What’s the capital of France?"}
  ],
)
print(response.choices[0].message.content)
```

You can also do embeddings similarly:

```python
resp = client.embeddings.create(model="llama2", input="Hello world!")
print(resp.data[0].embedding)
```

So for fairly simple local projects, the OpenAI SDK works perfectly with Ollama.


### 2. When should I use LiteLLM instead?

**LiteLLM** is a lightweight Python SDK (and optional proxy server) that provides a **unified API** for over 100 LLM providers—including OpenAI, Anthropic, HuggingFace—and crucially, **Ollama/local models** ( nice example with minimal Flask app - poem generator [KodeKloud Notes](https://notes.kodekloud.com/docs/Running-Local-LLMs-With-Ollama/Building-AI-Applications/Demo-Creating-an-App-Using-Ollama-OpenAI-Python-Client?utm_source=chatgpt.com "Demo Creating an App Using Ollama OpenAI Python Client")).

Here are some benefits of using LiteLLM:
- It standardizes completions, embeddings, streaming, retries, and fallback logic  
- You can swap providers (e.g. `openai/gpt‑4`, `anthropic/claude`, `ollama/llama2`) with no code changes  
- Proxy server mode offers observability, logging, rate limiting, and cost tracking across providers (see LiteLLM documentation: [LiteLLM](https://docs.litellm.ai/?utm_source=chatgpt.com "LiteLLM - Getting Started | liteLLM"))



### 3. Example: using LiteLLM Python SDK

First install:

```bash
pip install litellm
```

Then in Python:

```python
import os
from litellm import completion, embeddings

os.environ["OPENAI_API_KEY"] = "dummy"
os.environ["LITELLM_OLLAMA_BASE"] = "http://localhost:11434/v1"

# Completion via Ollama
resp = completion(model="ollama/llama2", messages=[{"role":"user","content":"Hello!"}])
print(resp["choices"][0]["message"]["content"])

# Embeddings via Ollama
emb = embeddings(model="ollama/llama2", input="Hello world")
print(emb["data"][0]["embedding"])
```

Later you can just switch to `openai/gpt-4o` or another provider. You keep the same `completion(...)` call. No branching logic in your app ([Langfuse](https://langfuse.com/integrations/frameworks/litellm-sdk?utm_source=chatgpt.com "Open Source Observability for LiteLLM SDK - Langfuse"), [LiteLLM](https://docs.litellm.ai/?utm_source=chatgpt.com "LiteLLM - Getting Started | liteLLM"), [LiteLLM](https://docs.litellm.ai/docs/?utm_source=chatgpt.com "LiteLLM - Getting Started")).

### 5. Alternatives to LiteLLM

There are several other frameworks you may consider:

- **Langchain**, **Llama‑Index**, **Guidance**, **instructor** – great for structured output, chaining, tool-use, agents, prompt templating. Read more in these sources:
	- [4 Proven Ways to Use Ollama Locally & OpenAI APIs in Python: Fast, Flexible, and Scalable \| by Brain Glitch \| Jun, 2025 \| Towards Dev](https://medium.com/towardsdev/4-proven-ways-to-use-ollama-locally-openai-apis-in-python-fast-flexible-and-scalable-216dca893b1c)
	- [Unlocking the Power of LiteLLM: A Lightweight, Unified Interface for LLMs](https://medium.com/%40hajraali730/unlocking-the-power-of-litellm-a-lightweight-unified-interface-for-llms-5dc09cece265)
	- [Top 5 LiteLLM alternatives of 2025](https://www.truefoundry.com/blog/litellm-alternatives)
	- [The best library for structured LLM output – Paul Simmering](https://simmering.dev/blog/structured_output/) - gives different recommendations for four use cases.

- **TrueFoundry** – a more enterprise‑ready orchestration layer with observability, scaling, and deployment support, but heavier than LiteLLM ([truefoundry.com](https://www.truefoundry.com/blog/litellm-alternatives?utm_source=chatgpt.com "Top 5 LiteLLM alternatives of 2025 - TrueFoundry"))


### Summary

I like using the **OpenAI Python SDK** with Ollama—it’s quick, reliable, and simple for local use cases. But as soon as I need to add other providers, handle retries/fallbacks, use embeddings, or manage observability and switching logic, **LiteLLM** becomes more convenient. And if I’m building complex agent pipelines or need structure, then libraries like **Langchain** or **TrueFoundry** fit right in.
