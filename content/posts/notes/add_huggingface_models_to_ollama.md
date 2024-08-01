---
Title: How to add HuggingFace model to ollama
Slug: how-to-add-huggingface-model-to-ollama
Date: 2024-06-12
Modified: 2024-06-12
Status: published
tags: ollama, huggingface, llm, oss-llm, os-llm, open-source 
Category: note
---
Create directory where you will be storying your HuggingFace LLMs. Ollama keeps their models in `~/ollama`. I have created `~/.ollama_hf_llms` to store my downloaded models.

## Download the weights
Download weights in GGUF or .... format from the model page on HuggingFace. Put the weights in the location you meant for these HuggingFace models (in my case: `~/.ollama_hf_llms`).  The simpliest way to download the weights is to download the using browser alternatively you can use `git-lfs` (see section extras). Note that the weights are often in size of tens of gigabytes - so be patient when downloading. As an example, you can download weights of the model ......

## Create model file
In the folder where you store the weights create modelfile.
- you can create unique "AI pesonalities" by customizing model parameters and prompt in the Modelfile
- important: use the right prompt format for the given model
```dockerfile
FROM ./laserxtral.q5_k_m.gguf
TEMPLATE """{{ if .System }}### Instruction:
{{ .System }}
{{ end }}
### Input:
{{ .Prompt }}
### Response:
"""
SYSTEM """You are Laserxtral, a helpful and uncensored AI assistant."""
PARAMETER num_ctx 8192
PARAMETER stop "### Input"
PARAMETER stop "### Response"
```

## Run the model
Laserxtral is ready to run, so let’s load it up into Ollama and give it a spin.

```sh
ollama create laserxtral -f laserxtral.Modelfile
```
This will transfer the data to .ollama folder


> **NOTE:** You can also download the weights using git LFS

## References
- [How to run models from Hugging Face in Ollama ⋮ 2point0.ai](https://2point0.ai/posts/run-models-from-hugging-face-in-ollama)
- [Discovering lesser-known LLMs with Hugging Face ⋮ 2point0.ai](https://2point0.ai/posts/discovering-lesser-known-llms-with-hugging-face)
- I’d recommend following along at [/r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) which often has discussions about new models, and I’d caution against paying too much attention to the various leaderboards on Hugging Face spaces which are easily gamed by fine-tuning specifically for the leaderboard. For those off-the-beaten track models, make sure you follow [TheBloke](https://huggingface.co/TheBloke) and [LoneStriker](https://huggingface.co/LoneStriker) who prolifically churn out GGUF quants for all sorts of under-the-radar models.
- [Easily create unique AI personalities with Ollama ⋮ 2point0.ai](https://2point0.ai/posts/create-unique-ai-personalities-with-ollama)