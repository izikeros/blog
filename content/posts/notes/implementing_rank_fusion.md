---
Title: Implementing Rank Fusion in Python
Slug: implementing-rank-fusion-in-python
Date: 2023-07-28
Modified: 2023-10-09
Status: published
tags: rank-fusion, hybrid-search, rank, search
Category: note
---

In the world of Information Retrieval, ranking is one of the most crucial aspects. It prioritizes the matching information according to its relevancy. In many cases, having a single ranking model may not satisfy the diverse needs of users. This is where the idea of Rank Fusion comes in; combining various ranking models to enhance the retrieval performance.
Let's learn how to implement a simple rank fusion approach in Python.

## Installation
First of all, we need to install the required libraries. If not already installed, use pip to install the following libraries:
```sh
pip install numpy pandas
```

## Importing Libraries
We will be using Pandas for handling data and Numpy for mathematical computations.
```python
import pandas as pd
import numpy as np
```

## Sample Data
For the demonstration, let's consider we have three ranking models and their rankings for 5 different items/documents.

```python
# Creating a dataframe for the sample data
rankings = pd.DataFrame({
    'Item': ['Item1', 'Item2', 'Item3', 'Item4', 'Item5'],
    'Rank_Model_1': [1, 2, 3, 4, 5],
    'Rank_Model_2': [5, 1, 3, 2, 4],
    'Rank_Model_3': [4, 5, 1, 3, 2]
})
```

## Implementing Rank Fusion

### Borda Count method
In our example, we will use the simple Borda Count method. The rank positions from each ranking model are summed for every item and the items are arranged in ascending order of their final scores.

```python
def perform_rank_fusion(data):
    data['Fused_Rank'] = data.drop('Item', axis=1).sum(axis=1)
    data = data.sort_values(by='Fused_Rank').reset_index(drop=True)
    return data

# Fuse the ranks and print the final rankings
fuse = perform_rank_fusion(rankings)
print(fuse[['Item', 'Fused_Rank']])
```

The output is the final ranking of the items after performing the fusion.

### Reciprocal rank fusion

The [Reciprocal Rank Fusion (RRF)](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf) is an advanced algorithmic technique designed to amalgamate multiple result sets, each having distinct relevance indicators, into a unified result set. One of the key advantages of RRF is its ability to deliver high-quality results without the necessity for any tuning. Moreover, it does not mandate the relevance indicators to be interconnected or similar in nature.

RRF uses the following formula to determine the score for ranking each document:

```python
score = 0.0
for q in queries:
    if d in result(q):
        score += 1.0 / ( k + rank( result(q), d ) )
return score

# where
# k is a ranking constant
# q is a query in the set of queries
# d is a document in the result set of q
# result(q) is the result set of q
# rank( result(q), d ) is d's rank within the result(q) starting from 1
```
(code from [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/rrf.html))

## Conclusion
In this post, we learned a simple method to fuse rankings from different models using the Borda Count algorithm. This methodology can be extended to more complex rank fusion algorithms and larger data sets.
Remember, the objective is not just to get automated rankings from the machine, but to provide the most relevant and helpful information to the end users. To meet this, experimenting with different fusion methods, or even creating a unique one that suits your requirements, is key to successful information retrieval.
This post is a simple introduction to rank fusion concept in Python. There are packages out there like rank_aggregation providing other advanced rank fusion methods to use!

X::[[rank_fusion_algorithms]]
X::[[hybrid_search__keyword_and_semantic]]
X::[[hybrid_search_re_ranking]]
X::[[rank_fussion_borda]]
