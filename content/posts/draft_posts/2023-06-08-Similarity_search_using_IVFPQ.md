---
Title: Similarity search using IVFPQ
Slug: similarity-search-using-ivfpq
Date: 2023-06-08
Modified: 2023-06-08
Start: 2023-06-08
Tags: machine-learning, python
Category: Machine Learning
Image: /images/head/ivfpq.jpg
banner: "/images/head/ivfpq.jpg"
Summary: Explore the powerful technique of Inverted File Product Quantization (IVFPQ) for similarity search. By combining the benefits of product quantization and an inverted file system.
Status: published
prompt:
---

# Unlocking the Power of Similarity Search using IVFPQ (Inverted File Product Quantization)

## Introduction

As the world generates more data than ever before, the need for efficient search algorithms has become indispensable. The field of similarity search focuses on finding the most similar elements in a large dataset, given a query element. Applications of similarity search range from image and video retrieval, to recommendation systems, and even natural language processing.

One particularly powerful technique for similarity search is Inverted File Product Quantization (IVFPQ). IVFPQ allows us to handle large-scale datasets by compressing the data and using an inverted file system for efficient indexing and retrieval. In this blog post, we'll dive into the details of how IVFPQ works, its advantages, and how to implement it in Python using the popular Faiss library.

## Understanding Inverted File Product Quantization (IVFPQ)

> **Product Quantization (PQ)** is a vector quantization technique that allows us to compress high-dimensional vectors into a compact form, while preserving the relative distances between them. In a nutshell, PQ works by dividing a high-dimensional vector into subvectors and quantizing each subvector independently.

Inverted File Product Quantization (IVFPQ) is an extension of PQ that adds an inverted file system on top of the basic PQ structure. 

> The **inverted file system** is essentially an index that maps each quantized vector to a list of database vectors that fall in the same quantization cell.

The key advantage of IVFPQ is that it allows us to perform similarity search with a reduced number of distance computations, making it a highly efficient technique for large-scale datasets.

## Implementing IVFPQ in Python using Faiss

Now that we have a basic understanding of IVFPQ, let's see how to implement it in Python using the Faiss library. Faiss is a popular library developed by Facebook AI Research that provides efficient implementations of several similarity search techniques, including IVFPQ.

Let's start by installing the Faiss library:

```sh
pip install faiss
```

Next, let's generate some random data to work with. For this example, we'll create a dataset of 10,000 128-dimensional vectors:

```python
import numpy as np

dimension = 128
num_vectors = 10000

# Generate random data
data = np.random.random((num_vectors, dimension)).astype(np.float32)
```

Now, let's create an IVFPQ index using Faiss:

```python
import faiss

# Initialize the IVFPQ index
quantizer = faiss.IndexFlatL2(dimension)
index = faiss.IndexIVFPQ(quantizer, dimension, 100, 16, 8)

# Train the index
index.train(data)

# Add data to the index
index.add(data)
```

In the code above, we first create a quantizer using Faiss's IndexFlatL2. This is a basic L2 distance index that will be used for coarse quantization. Next, we create the IVFPQ index by passing the quantizer, the dimension of the vectors, the number of coarse quantization cells (100), the number of subquantizers (16), and the number of bits per subquantizer (8).

We then train the index using our dataset and add the data to the index.

Finally, let's perform a similarity search using our IVFPQ index. We'll generate a random query vector and find the top 10 most similar vectors in our dataset:

```python
# Generate a random query vector
query = np.random.random((1, dimension)).astype(np.float32)

# Perform the similarity search
k = 10
distances, indices = index.search(query, k)

# Print the results
print("Top 10 most similar vectors:")
for i, (distance, index) in enumerate(zip(distances[0], indices[0])):
    print(f"{i+1}. Index: {index}, Distance: {distance}")
```

The search method returns two arrays: one containing the distances between the query vector and the closest vectors in the dataset, and another containing the indices of those vectors. We can then print the results to see the top 10 most similar vectors.
```
Top 10 most similar vectors: 
1. Index: 1548, Distance: 12.515710830688477 
2. Index: 3764, Distance: 14.528205871582031 
3. Index: 5173, Distance: 14.70742416381836 
4. Index: 5930, Distance: 14.80669116973877 
5. Index: 9472, Distance: 15.031980514526367 
6. Index: 5696, Distance: 15.204572677612305 
7. Index: 587, Distance: 15.735445022583008 
8. Index: 816, Distance: 15.76244831085205 
9. Index: 3032, Distance: 15.773483276367188 
10. Index: 3776, Distance: 16.045366287231445
```

## Conclusion

In this blog post, we've explored the powerful technique of Inverted File Product Quantization (IVFPQ) for similarity search. By combining the benefits of product quantization and an inverted file system, IVFPQ provides a highly efficient method for searching large-scale datasets. We also demonstrated how to implement IVFPQ in Python using the Faiss library, showcasing its ease of use and effectiveness.

If you're working with large-scale datasets and need an efficient way to perform similarity search, give IVFPQ a try and see the benefits for yourself!

## Related reading
- [Similarity Search with IVFPQ. Find out how the inverted file index… | by Peggy Chang | Towards Data Science](https://towardsdatascience.com/similarity-search-with-ivfpq-9c6348fd4db3)
- [Faiss: The Missing Manual | Pinecone](https://www.pinecone.io/learn/series/faiss)
- D. Baranchuk, et al., [Revisiting the Inverted Indices for Billion-Scale Approximate Nearest Neighbors](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/1802.02422.pdf) (2018), _ECCV_
- Y. Matsui, et al., [A Survey of Product Quantization](https://link.zhihu.com/?target=https%3A//www.jstage.jst.go.jp/article/mta/6/1/6_2/_pdf) (2018), _ITE Trans. on MTA_
- T. Ge, et. al., [Optimized Product Quantization](https://link.zhihu.com/?target=http%3A//kaiminghe.com/publications/pami13opq.pdf) (2014), _TPAMI_
- H. Jégou, et al., [Product quantization for nearest neighbor search](https://link.zhihu.com/?target=https%3A//lear.inrialpes.fr/pubs/2011/JDS11/jegou_searching_with_quantization.pdf) (2010), _TPAMI_
- A. Babenko, V. Lempitsky, The Inverted Multi-Index (2012), CVPR
- H. Jégou, et al., Searching in One Billion Vectors: Re-rank with Source Coding (2011), ICASSP
- Y. Malkov, D. Yashunin, Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs (2016), IEEE Transactions on Pattern Analysis and Machine Intelligence
- Y. Malkov et al., Approximate Nearest Neighbor Search Small World Approach (2011), International Conference on Information and Communication Technologies & Applications
- Y. Malkov et al., Scalable Distributed Algorithm for Approximate Nearest Neighbor Search Problem in High Dimensional General Metric Spaces (2012), Similarity Search and Applications, pp. 132-147
- Y. Malkov et al., Approximate nearest neighbor algorithm based on navigable small world graphs (2014), Information Systems, vol. 45, pp. 61-68
