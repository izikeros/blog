---
Title: How to count tokens?
Slug: how-to-count-tokens
Date: 2023-06-08
Modified: 2023-06-08
Status: published
Tags: tokenizers, token, tokenization, tiktoken, openai, NLP 
Category: note
---
#tokenizers #openai #tiktoken 


## Counting Tokens: A Guide to Text Tokenization

Counting tokens is a useful task in natural language processing (NLP) that allows us to measure the length and complexity of a text. The two important use cases for counting the tokens are:
- **controlling the length of the prompt** - the models has limit on number of input tokens - it is good to have control if you don't exceed the limits for the model
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

### OpenAI Cookbook Guide

For a more detailed explanation and additional examples, you can refer to the OpenAI Cookbook guide on [how to count tokens with tiktoken](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb). The guide provides comprehensive instructions on token counting and offers insights into various use cases.

### Tokenization Sandbox

If you're looking to experiment with text tokenization, OpenAI provides a convenient web application called the Tokenization Sandbox. You can access it [here](https://platform.openai.com/tokenizer). The sandbox allows you to input text and observe the resulting tokens, helping you gain a deeper understanding of the tokenization process.

### References

To develop this guide, we drew inspiration from the token counting instructions provided by OpenAI. You can find additional information in the [OpenAI documentation](https://platform.openai.com/docs/guides/embeddings/limitations-risks), where they discuss the limitations and risks associated with embeddings.

Token counting is an essential task when working with NLP, enabling us to analyze and process text effectively. By leveraging OpenAI's `tiktoken` library and following the guidelines outlined in this blog post, you'll be well-equipped to count tokens accurately and efficiently.