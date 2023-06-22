---
Title: How to count tokens
Slug: 
Date: 2023-06-08
Modified: 2023-06-08
Status: draft
Tags: tag1, tag2
Category: note
---
#tokenizers #openai 

copy-paste from: https://platform.openai.com/docs/guides/embeddings/limitations-risks

### How can I tell how many tokens a string has before I embed it?

](https://platform.openai.com/docs/guides/embeddings/how-can-i-tell-how-many-tokens-a-string-has-before-i-embed-it)

In Python, you can split a string into tokens with OpenAI's tokenizer [`tiktoken`](https://github.com/openai/tiktoken).

Example code:

```python
import tiktoken

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

num_tokens_from_string("tiktoken is great!", "cl100k_base")
```

For second-generation embedding models like `text-embedding-ada-002`, use the `cl100k_base` encoding.

More details and example code are in the OpenAI Cookbook guide [how to count tokens with tiktoken](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb).