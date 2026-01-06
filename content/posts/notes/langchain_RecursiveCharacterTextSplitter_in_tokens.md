---
Category: note
Date: 2023-09-27
Modified: 2023-09-27
Slug: langchain-recursivecharactertextsplitter-split-by-tokens-instead-of-characters
Status: published
Summary: Learn how to use LangChain's RecursiveCharacterTextSplitter to split text into chunks based on tokens, suitable for LLM context limits, and discover the steps to implement this in your natural language processing tasks.
ai_summary: true
Tags:
  - text-splitting
  - text-chunking
  - langchain
  - RecursiveCharacterTextSplitter
  - Tokens
  - Characters
  - natural-language-processing
  - language-modeling
  - chunk-size
Title: LangChain RecursiveCharacterTextSplitter - Split by Tokens instead of characters
---
up::[[MOC_LangChain]]

# LangChain RecursiveCharacterTextSplitter - Split by Tokens instead of Characters

The LangChain [RecursiveCharacterTextSplitter](https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/recursive_text_splitter) is a tool that allows you to split text on predefined characters that are considered as a potential division points. By default, the size of the chunk is in characters but by using `from_tiktoken_encoder()` method you can easily split to achieve given size of the chunk in tokens instead of characters. This is especially useful since LLMs have context limits expressed in tokens not in characters. This split can be useful in various natural language processing tasks, such as language modeling or text classification.

To use the RecursiveCharacterTextSplitter, follow these steps:

1. Import the required module: `from langchain.text_splitter import RecursiveCharacterTextSplitter`

2. Set the desired chunk size (in tokens): `CHUNK_SIZE_TOKENS = 1_500`

3. Instantiate the RecursiveCharacterTextSplitter using the `from_tiktoken_encoder` method and provide the chunk size and overlap values:

```python
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=CHUNK_SIZE_TOKENS,
    chunk_overlap=0,
)
```

4. Once the text_splitter object is created, you can use the `create_documents` method to split your text into documents. Make sure to pass the text to be split as a parameter in a list format:

```python
docs = text_splitter.create_documents([text])
```

For alternative solutions and further discussion, you can refer to the following GitHub issue: [LangChain Issue #4678](https://github.com/langchain-ai/langchain/issues/4678#issuecomment-1704305645).
