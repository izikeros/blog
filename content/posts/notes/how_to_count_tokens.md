---
Category: note
Date: 2023-06-08
Modified: 2023-07-12
Slug: how-to-count-tokens
Status: published
Summary: Learn how to accurately count tokens in text using OpenAI's `tiktoken` library, essential for controlling prompt length and managing costs in natural language processing projects.
ai_summary: true
Title: How to Count Tokens - Tokenization With Tiktoken.
tags:
  - tokenizers
  - token
  - tokenization
  - tiktoken
  - openai
  - NLP
up: "[[MOC_Generative_AI]]"
---
Counting tokens is a useful task in natural language processing (NLP) that allows us to measure the length and complexity of a text. The two important use cases for counting the tokens are:

- **controlling the length of the prompt** -  models has limit on the number of input tokens - it is good to have control if you don't exceed the limits for the model
- **cost awareness**  - when you know how many tokens you pass as input, you know the cost related to the prompt.

In this blog post, we will explore how to count the number of tokens in a given text using OpenAI's tokenizer, called `tiktoken`. Whether you're a seasoned Python developer or just getting started with NLP, this guide will provide you with a step-by-step process to accurately determine the token count of your text.

### Introduction to `tiktoken`

To begin with, we need to install the `tiktoken` library, which is a powerful tokenizer developed by OpenAI. It offers efficient tokenization capabilities and supports a wide range of languages. You can find the library on GitHub at [this link](https://github.com/openai/tiktoken).

### Code Example

Let's dive into a code example that demonstrates how to count tokens using `tiktoken`:

```python
import tiktoken

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

num_tokens_from_string("tiktoken is great!", "cl100k_base")
```

In the example above, we import the `tiktoken` library and define a function called `num_tokens_from_string`. This function takes a text string and an encoding name as input parameters. It returns the number of tokens in the given text string.

To count the tokens, we first obtain the encoding using `tiktoken.get_encoding(encoding_name)`. The `encoding_name` specifies the type of encoding we want to use. In this case, we use the `cl100k_base` encoding, which is suitable for second-generation embedding models like `text-embedding-ada-002`.

Next, we encode the input string using `encoding.encode(string)` and calculate the number of tokens by taking the length of the encoded sequence. The final result is the total number of tokens in the text string.

`tiktoken` supports three encodings used by OpenAI models:

|Encoding name|OpenAI models|
|---|---|
|`cl100k_base`|`gpt-4`, `gpt-3.5-turbo`, `text-embedding-ada-002`|
|`p50k_base`|Codex models, `text-davinci-002`, `text-davinci-003`|
|`r50k_base` (or `gpt2`)|GPT-3 models like `davinci`|

### OpenAI Cookbook Guide

For a more detailed explanation and additional examples, you can refer to the OpenAI Cookbook guide on [how to count tokens with tiktoken](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb). The guide provides comprehensive instructions on token counting and offers insights into various use cases.

### Tokenization Sandbox

If you're looking to experiment with text tokenization, OpenAI provides a convenient web application called the Tokenization Sandbox. You can access it [here](https://platform.openai.com/tokenizer). The sandbox allows you to input text and observe the resulting tokens, helping you better understand the tokenization process.

### Text splitter module

A Python script for splitting text into parts with controlled (limited) length in tokens. This script utilizes the `tiktoken` library for encoding and decoding text.:
<https://gist.github.com/izikeros/17d9c8ab644bd2762acf6b19dd0cea39>

### Count tokens cli tool

Check this simple CLI tool that have one purpose - count tokens in a text file:

[izikeros/count\_tokens: Count tokens in a text file.](https://github.com/izikeros/count_tokens)

### Rule of thumb

OpenAI on the [website](https://platform.openai.com/tokenizer) with the tokenizer sandbox provides rule of thumb that helps to estimate approximate number of tokens in given text.

> A helpful rule of thumb is that one token generally corresponds to ~4 characters of text for common English text. This translates to roughly ¾ of a word (so 100 tokens ~= 75 words).

### References

To develop this guide, we drew inspiration from the token counting instructions provided by OpenAI. You can find additional information in the [OpenAI documentation](https://platform.openai.com/docs/guides/embeddings/limitations-risks), where they discuss the limitations and risks associated with embeddings.

Token counting is essential when working with NLP, enabling us to analyze and process text effectively. By leveraging OpenAI's `tiktoken` library and following the guidelines outlined in this blog post, you'll be well-equipped to count tokens accurately and efficiently.

See also: [Tokens, the secret language of AI | Omar Kamali](https://omarkama.li/blog/tokens-the-secret-language-of-ai)
