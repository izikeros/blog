---
Title: Implementing Reciprocal Rank Fusion (RRF) in Python
Slug: implementing-rank-fusion-in-python
Date: 2023-07-28
Modified: 2023-10-09
Status: published
tags: rank-fusion, hybrid-search, rank, search
Category: note
---

X::[[borda_count_python]]

In the world of Information Retrieval, ranking is one of the most crucial aspects. It prioritizes the matching information according to its relevancy. In many cases, having a single ranking model may not satisfy the diverse needs of users. This is where the idea of Rank Fusion comes in; combining various ranking models to enhance the retrieval performance.
Let's learn how to implement a simple rank fusion approach in Python.

## Understanding the RRF Ranking Process

The Reciprocal Rank Fusion (RRF) operates by collecting search outcomes from various strategies, assigning each document in the results a reciprocal rank score, and subsequently merging these scores to generate a new ranking. The underlying principle is that documents that consistently appear in top positions across diverse search strategies are likely more pertinent and should thus receive a higher rank in the consolidated result.

### A simplified breakdown of the RRF process

1. **Collect ranked search outcomes** from multiple simultaneous queries. E.g. one query to semantic search and one query to text search.

2. **Assign reciprocal rank scores to each result in the ranked lists.** The RRF process generates a new search score for each match in each result set. For each document in the search results, the algorithm assigns a reciprocal rank score based on its position in the list. This score is computed as $1/(rank + k)$, where $rank$ is the document's position in the list, and $k$ is a constant. 

> **Choosing the k constant**
> Empirical observation suggests that $k$ performs best when set to a small value, such as `60`. Note that this $k$ value is a constant in the RRF algorithm and is entirely distinct from the `k` that regulates the number of nearest neighbours.

4. **Combine scores.** The algorithm adds up the reciprocal rank scores acquired from each search strategy for each document, thereby generating a combined score for each document.

5. The algorithm ranks documents based on the combined scores and arranges them accordingly. The resulting list constitutes the fused ranking.

To depict the Reciprocal Rank Fusion (RRF) process, we can use a flowchart.
![Reciprocal Rank Fusion (RRF) process flow chart](/images/Reciprocal_Rank_Fusion/Reciprocal_Rank_Fusion.png)

***Figure 1:** Reciprocal Rank Fusion (RRF) Process Flowchart. The diagram illustrates the steps involved in the RRF ranking process.

## Implementing Reciprocal Rank Fusion

The [Reciprocal Rank Fusion (RRF)](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf) is an advanced algorithmic technique designed to amalgamate multiple result sets, each having distinct relevance indicators, into a unified result set. One of the key advantages of RRF is its ability to deliver high-quality results without the necessity for any tuning. Moreover, it does not mandate the relevance indicators to be interconnected or similar in nature.

RRF uses the following formula to determine the score for ranking each document:

```python
score = 0.0
for q in queries: # loop over queries send to different search engines 
    if d in result(q):
        score += 1.0 / ( k + rank(result(q), d))
return score

# where
# k is a ranking constant
# q is a query in the set of queries
# d is a document in the result set of q
# result(q) is the result set of q
# rank( result(q), d ) is d's rank within the result(q) starting from 1
```

(code from [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/rrf.html))

You could significantly improve performance by using maps and list comprehensions -  referred to as "vectorizing" in overlapping contexts.

```python
def reciprocal_rank_fusion(queries, d, k, result_func, rank_func):
    return sum([1.0 / (k + rank_func(result_func(q), d)) if d in result_func(q) else 0 for q in queries])
```

This function takes as arguments:

- A collection of queries
- A document `d`
- A ranking constant `k`
- A function `result_func` that represents the `result(q)` operation in your original code.
- A function `rank_func` that represents the `rank(result(q), d)` operation in your original code.

> **NOTE:** list comprehension is used to perform the operations that for-loop did, allowing Python to compute the results in a more optimized way. However, this isn't truly "vectorized" computing as you would find in libraries like NumPy or in languages like R, where computations are performed concurrently rather than sequentially.

The `result_func` function takes a query `q`, and returns a list of documents that are the results of the query. For simplicity, let's assume that each query corresponds to a list of documents in a dictionary called `database`.

The `rank_func` function takes a list of documents (results of a query) and a specific document `d`, and returns the rank of `d` in the list.

```python
database = {   # assuming your queries and results are stored in a dictionary
    'query1': ['doc1', 'doc2', 'doc3'],
    'query2': ['doc3', 'doc1', 'doc2'],
    # more queries and their document results...
}

def result_func(q):
    return database[q]

def rank_func(results, d):
    return results.index(d) + 1 # adding 1 because ranks start from 1
```

Then, the `reciprocal_rank_fusion` function can be called like this:

```python
k = 5 
d = 'doc1'
queries = ['query1', 'query2'] # fill this with your actual query keys

print(reciprocal_rank_fusion(queries, d, k, result_func, rank_func))
```

This assumes that queries and their corresponding results are uniquely stored in a dictionary, and that your document ranks are determined by their order in the list of results.

Please modify the functions `result_func`, `rank_func`, and `database` to fit your specific application details and data.

## Conclusion

The concept of Rank Fusion, particularly the Reciprocal Rank Fusion (RRF) method, offers a promising approach to amalgamate multiple result sets into a unified one. This article has demonstrated how to implement a simple RRF in Python.

While the example provided in this article is simplified, it provides a solid foundation for understanding the RRF process and how to implement it in Python. Depending on the specific application and data, the functions and database structure may need to be modified. However, the core concept and approach remain the same.

The RRF method is a powerful tool in the field of Information Retrieval, providing a robust and efficient way to combine multiple ranking models to enhance retrieval performance. By understanding and implementing this method, one can significantly improve the quality and relevance of search results, thereby enhancing user satisfaction and system effectiveness.

## See also
- Condorcet Fuse (Montague, M., and Aslam, J. A. Condorcet fusion for improved retrieval. In CIKM (2002).)
- CombMNZ

**Edits:**

- 2023-11-06: changed title to: Implementing Reciprocal Rank Fusion and Borda Count in Python
- 2023-11-06: added RRF description
- 2023-11-06: added optimized implementation

X::[[rank_fusion_algorithms]]
X::[[dups/hybrid_search]]
X::[[dups/hybrid_search_re_ranking]]
X::[[dups/rank_fussion_borda]]
