---
Category: note
Date: 2023-07-03
Modified: 2023-07-12
Slug: token-split-text
Status: published
Summary: Learn how to efficiently split text into parts based on token limits using the Tiktoken library and a custom Python module, ensuring meaningful splits without breaking words.
ai_summary: true
Tags:
  - tokenization
  - tiktoken
  - prompt-chunking
  - split-text
  - text-partitioning
  - openai
  - gpt-4
Title: Introducing a Python Module for Splitting Text Into Parts Based on Token Limit
---
up::[[tokenizer]]

## Introduction

In the realm of natural language processing and text analysis, it is often necessary to split a large piece of text into smaller parts while ensuring that the split does not break words or disrupt the meaning of the text. This task can be challenging, especially when dealing with the tokenization. However, with the help of the Tiktoken library and a custom Python module, splitting text based on a specified number of tokens can be an easy task.

## Understanding the Tiktoken Library

Tiktoken is a powerful Python library for tokenization, which is the process of splitting text into individual tokens such as words or subwords. The library provides various tokenization encodings and functions that enable developers to process text data in a tokenized format. It offers support for different languages and tokenization models, making it a versatile tool for a wide range of text processing tasks. Tiktoken is a fast [BPE](https://en.wikipedia.org/wiki/Byte_pair_encoding) tokeniser for use with OpenAI's models.

## Introducing the Python Module: split_string_with_limit

The provided Python module: [split_string_with_limit.py](https://gist.github.com/izikeros/17d9c8ab644bd2762acf6b19dd0cea39) (GitHub Gist), leverages the capabilities of the Tiktoken library to split a string into parts with a specified limit on the number of tokens per part. The module takes three parameters: `text`, `limit`, and `encoding`.

- `text`: The input string that needs to be split.
- `limit`: The maximum number of tokens allowed per part.
- `encoding`: The tokenization encoding to be used, which determines how the text is tokenized.

The module proceeds as follows:

1. It tokenizes the input text using the specified encoding from Tiktoken.
2. It creates an empty list, `parts`, to store the tokenized parts.
3. It initializes a `current_part` list and a `current_count` variable to keep track of the tokens in the current part.
4. It iterates over each token in the tokenized text.
5. For each token, it appends it to the `current_part` list and increments the `current_count` by 1.
6. If the `current_count` exceeds the specified limit, it adds the `current_part` to the `parts` list, resets the `current_part` and `current_count` to empty values, and continues with the next tokens.
7. Once all the tokens have been processed, the module checks if there is any remaining `current_part` and adds it to the `parts` list.
8. Finally, it converts each tokenized part back into text format by decoding the individual tokens and joins them together. The resulting text parts are stored in the `text_parts` list.
9. The module returns the `text_parts` list as the output.

## Example Usage

To demonstrate the usage of the `split_string_with_limit` module, let's consider an example:

```sh
python split_string_with_limit.py input_file.txt 100 cl100k_base
```

In this example, we provide three arguments:

1. `input_file.txt`: The path to the input text file that contains the text to be split.
2. `100`: The maximum number of tokens allowed per part. You can adjust this value based on your requirements.
3. `cl100k_base`: The encoding name. This determines how the text will be tokenized. Tiktoken provides various encoding options, and you can experiment with different encodings to achieve the desired results.

The module reads the text from the input file, tokenizes it using the specified encoding, and splits it into parts based on the token limit. The resulting text parts are then printed in a JSON format, providing a structured representation of the split text.

## Approximate approach

While the `split_string_with_limit` module offers a convenient solution for splitting text based on a token limit, it's worth mentioning alternative algorithms or approaches that can achieve similar results. One of these can be a **Fixed-Length Split**: instead of splitting based on the number of tokens, we could split the text into fixed-length segments based on counting words or characters. One can use [rule of thumb](https://platform.openai.com/tokenizer):

> A helpful rule of thumb is that one token generally corresponds to ~4 characters of text for common English text. This translates to roughly ¾ of a word (so 100 tokens ~= 75 words).

to have approximate of the split into parts of equal length without doing actual tokenization.

## Conclusion

In this blog post, we introduced the `split_string_with_limit` Python module, which leverages the power of the Tiktoken library to split a string into parts based on a specified token limit. We discussed the functionality of the module, its parameters, and how it can be used in practice. Furthermore, we explored alternative algorithms and approaches for splitting text based on the number of tokens. By combining the flexibility of Tiktoken and the convenience of the `split_string_with_limit` module, developers can efficiently process and analyze text data without compromising on accuracy or readability.
