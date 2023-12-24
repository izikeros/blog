---
Title: Azure OpenAI Langchain configuration 
Slug: azure-openai-langchain-configuration
Date: 2023-08-02
Modified: 2023-10-23
Status: published
Tags: langchain, azure, openai 
Category: note
---
This note contains a recipe for how to configure LangChain to use Azure OpenAI.

NOTE: requires `python-dotenv` python package installed

## create `.env` with configuration and secrets

```
OPENAI_API_TYPE="azure"
OPENAI_API_KEY="***"
OPENAI_API_BASE="***"
OPENAI_API_VERSION="***"
```

## initialize langchain

```python
from dotenv import load_dotenv,find_dotenv
from langchain.llms import AzureOpenAI

load_dotenv(find_dotenv())

deployment_name = "text-davinci-003"
model_name = "text-davinci-003"

llm = AzureOpenAI(deployment_name=deployment_name, model_name=model_name)

# check if it works
print(llm("What is the capital of France?"))
```

NOTE: `find_dotenv` -  its purpose is to locate the `.env` file in your project directory or its parent directories. It starts the search from the current working directory and recursively moves up the directory tree until it finds the `.env` file. If no `.env` file is found, it returns the path of the current working directory. This function is beneficial because it ensures your code can locate the `.env` file regardless of the directory from which your script is executed.
