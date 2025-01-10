---
Title: How does QLoRA works?
Slug: how-does-qlora-works
Date: 2024-07-03
Modified: 2024-07-03
Status: published
tags: qlora, lora, low-rank-adaptation, quantisation, weights, adapters,4-bit-normal-float, double-quantisation, training, fine-tuning 
Category: note
---

## TL;DR

> **QLoRA** (Quantized Low-Rank Adaptation) is a memory-efficient fine-tuning method for large language models. It uses a frozen 4-bit quantized base model with trainable adapters. During fine-tuning, only the adapters are updated, with gradients backpropagated through the quantized weights. Key innovations include 4-bit NormalFloat quantization, paged optimizers, and double quantization, all of which significantly reduce memory usage. This allows fine-tuning of large models on consumer hardware without compromising performance.
>

This article outline in brief idea of QLoRA. For the deeper understanding of QLoRA, I highly recommend reading [blog post](https://huggingface.co/blog/4bit-transformers-bitsandbytes) by the QLoRA authors explaining the QLoRA idea in a clear way.

## Understanding QLoRA: Efficient Fine-tuning for Large Language Models

QLoRA (Quantized Low-Rank Adaptation) is an innovative technique that enables efficient fine-tuning of large language models. It combines several key components to reduce memory usage and computational costs without sacrificing performance. Let's break down how QLoRA works:

### Core Components

1. **4-bit Quantized Base Model**: QLoRA starts with a pre-trained language model quantized to 4-bit precision. This dramatically reduces memory requirements compared to full-precision models.
2. **Low-Rank Adapters**: Small, trainable modules are added on top of the frozen base model. These adapters capture task-specific information during fine-tuning.
3. **4-bit NormalFloat**: A novel quantization data type that maintains a normal distribution of values, preserving model quality better than traditional integer quantization.
4. **Paged Optimizers**: A memory management technique that efficiently swaps optimizer states between CPU and GPU memory.
5. **Double Quantization**: Further compresses the quantization constants, reducing memory usage even more.

### How It Works?

1. The base model is quantized to 4-bit precision and frozen.
2. Low-rank adapters are added to each layer of the model.
3. During fine-tuning, only the adapters are updated.
4. Backpropagation occurs through the 4-bit weights into the adapters.
5. Paged optimizers manage memory usage during training.
6. Double quantization further reduces memory requirements.

This approach allows for fine-tuning of very large models on consumer-grade hardware, opening up new possibilities for researchers and developers working with state-of-the-art language models.

![Full Fine Tuning, LoRA and QLoRA fine tuning compared](/images/qlora/qlora_fine_tuning.png)
*Figure from: [QLoRA paper by Dettmers et al](https://arxiv.org/abs/2305.14314)*

## Three Innovative Techniques for Memory Efficiency

### 4-bit NormalFloat (NF4)

The QLoRA paper introduces the concept of 4-bit NormalFloat (NF4), a novel **data type** that is information theoretically **optimal for normally distributed weights**.
NF4 is used for quantization in QLoRA, which aims to make large language models more accessible by reducing memory usage during fine-tuning. Unlike traditional 4-bit integer or 4-bit floating-point representations, NF4 is specifically designed for normally distributed weights, making it more efficient for certain tasks.

### Paged Optimizers

In the context of QLoRA, paged optimizers are introduced to manage memory spikes during fine-tuning. These optimizers help mitigate memory usage by **efficiently handling memory transfers between the GPU and CPU**. While the specifics of paged optimizers are not covered extensively in the QLoRA paper, they play a crucial role in achieving memory efficiency.

### Double Quantization

Double quantization is a technique used to reduce the average memory footprint in QLoRA. It involves **quantizing** not only the **model parameters** but also the **quantization constants themselves**. By applying double quantization, QLoRA achieves memory savings without compromising performance.

These innovations collectively contribute to QLoRA’s ability to fine-tune large language models efficiently while maintaining performance.

# Further Reading

- [Making LLMs even more accessible with bitsandbytes, 4-bit quantization and QLoRA](https://huggingface.co/blog/4bit-transformers-bitsandbytes) - blog post by the QLoRA authors explaining the QLoRA idea in a clear way.
- [Original QLoRA paper by Dettmers et al](https://arxiv.org/abs/2305.14314) (2023)
