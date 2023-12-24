---
Category: Generative AI
Date: '2023-07-04'
Image: /images/head/text_vectorization.jpg
Modified: '2023-07-04'
Slug: text-vectorization-with-vectorhub-and-sentence-transformers
Status: published
Summary: Learn how to use Sentence Transformers for text vectorization with different models using consistent API.
Tags: embeddings, nlp, vectorhub, bert, sentence-transformers
Title: Easy Text Vectorization With VectorHub and Sentence Transformers
banner: "/images/head/text_vectorization.jpg"
prompt: null
---
up::[[embeddings]]
X::[[vector_embeddings_search]]
X::[[dont_use_openai_embeddings]]

Text is heavily inspired by part of the e-book: [Semantic NLP search with FAISS and VectorHub - Guide To Vectors (getvectorai.com)](https://learn.getvectorai.com/vector-ai-documentation/semantic-nlp-search-with-faiss-and-vectorhub) - which was using VectorHub as an interface to the models.

> **NOTE**: VectorHub is deprecated and no longer maintained. The authors of VectorHub recommend using [Sentence Transformers](https://www.sbert.net/), TFHub, and Huggingface directly for text vectorization.

This article demonstrates a similar process as the original article but uses a sentence transformers package.

### Encoding Data Using Sentence Transformers

To encode models easily, we will utilize the [Sentence Transformers](https://www.sbert.net/) library. SentenceTransformers is a Python framework for state-of-the-art sentence, text, and image embeddings. It provides a variety of pre-trained models that can convert sentences into meaningful numerical representations.

First, we need to install the `sentence-transformers` package, which includes the necessary dependencies for using Sentence Transformers. This library offers a wide range of pre-trained models, such as [BERT](<https://en.wikipedia.org/wiki/BERT_(Language_model)>), [RoBERTa](https://huggingface.co/docs/transformers/model_doc/roberta), and [MiniLM](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2), that can be used for text encoding. More information about Sentence Transformers can be found [here](https://www.sbert.net/).

```sh
pip install sentence-transformers
```

Next, we will instantiate our model and start the encoding process. In this example, we will use the "all-MiniLM-L6-v2" model, which is a variant of the MiniLM model.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

# Sentences to be encoded
sentences = [
    'This framework generates embeddings for each input sentence',
    'Sentences are passed as a list of strings.',
    'The quick brown fox jumps over the lazy dog.'
]

# Encode sentences using the Sentence Transformers model
embeddings = model.encode(sentences)

# Print the embeddings
for sentence, embedding in zip(sentences, embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding)
    print("")
```

In the code snippet above, we begin by installing the `sentence-transformers` package, which provides the necessary tools for working with Sentence Transformers. This library offers various pre-trained models that can convert sentences into meaningful vector representations.

After the installation, we import the `SentenceTransformer` class from the `sentence_transformers` module. We instantiate the model using the `all-MiniLM-L6-v2` variant, which will be used for encoding our sentences.

We define a list of sentences that we want to encode using the Sentence Transformers model. In this case, we have three exemplary sentences: "This framework generates embeddings for each input sentence," "Sentences are passed as a list of strings," and "The quick brown fox jumps over the lazy dog."

To perform the encoding, we use the `encode` method of the `model` object, passing in the `sentences` list. This method returns the corresponding embeddings for each sentence, which we store in the `embeddings` variable.

Finally, we iterate over the `sentences` and `embeddings` lists together using `zip`. For each sentence and its corresponding embedding, we print them out to visualize the results.

Please note that the code snippet above uses the "all-MiniLM-L6-v2" model as an example. You can explore and choose from a wide range of models provided by Sentence Transformers according to your specific requirements.

## References

- [GitHub - RelevanceAI/vectorhub: Vector Hub - Library for easy discovery, and consumption of State-of-the-art models to turn data into vectors. (text2vec, image2vec, video2vec, graph2vec, bert, inception, etc)](https://github.com/RelevanceAI/vectorhub)
- [Introduction - Guide To Vectors](https://learn.getvectorai.com/)

*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*
