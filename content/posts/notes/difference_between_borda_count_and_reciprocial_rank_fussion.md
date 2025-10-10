---
Title: Borda Count vs. Reciprocal Rank - Choosing the Right Ranking Method for Your Data
Slug: borda-count-vs-reciprocal-rank
Date: 2024-07-15
Modified: 2024-07-15
Status: published
tags:
  - borda
  - rank
  - rank-combining
  - rank-fussion
  - reciprocal-rank-fussion
  - reciprocal-rank-combining
Category: note
---

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Borda count and Reciprocal Rank Combining - approach and calculation](#borda-count-and-reciprocal-rank-combining---approach-and-calculation)
    - [Borda Count](#borda-count)
    - [Reciprocal Rank](#reciprocal-rank)
- [Key differences](#key-differences)
- [Example](#example)
    - [Key observations](#key-observations)
    - [The main differences](#the-main-differences)
- [Which one to use and when?](#which-one-to-use-and-when)
    - [Borda Count is better when...](#borda-count-is-better-when)
    - [Reciprocal Rank is better when...](#reciprocal-rank-is-better-when)
    - [Additional considerations](#additional-considerations)
- [Summary](#summary)

<!-- /MarkdownTOC -->

<a id="borda-count-and-reciprocal-rank-combining---approach-and-calculation"></a>

## Borda count and Reciprocal Rank Combining - approach and calculation

Borda count and Reciprocal Rank are both methods used in information retrieval and voting systems to combine rankings, but they differ in their approach and calculation. For details of the calculation see [[borda_count_python]] and [[implementing_reciprocal_rank_fusion_in_python]]. In this blog post we will focus on comparison of both algorithms and key differences.

<a id="borda-count"></a>

### Borda Count

- Assigns points to each item based on its position in each ranking
- Typically gives n points to the top-ranked item, n-1 to the second, and so on, where n is the number of items
- Sums up the points across all rankings
- Final ranking is determined by the total points, with higher scores ranking better

<a id="reciprocal-rank"></a>

### Reciprocal Rank

- Focuses on the position of each item in the rankings
- Calculates the reciprocal of the rank for each item (1/rank)
- Averages these reciprocal ranks across all rankings
- Final ranking is determined by the average reciprocal rank, with higher values ranking better

<a id="key-differences"></a>

## Key differences

1. **Scale**: Borda count uses a linear scale, while Reciprocal Rank uses a non-linear scale that emphasizes top rankings more heavily.
2. **Sensitivity**: Reciprocal Rank is more sensitive to high rankings and less affected by lower rankings compared to Borda count.
3. **Range**: Borda count scores depend on the number of items, while Reciprocal Rank scores are always between 0 and 1.
4. **Interpretation**: Borda count provides a cumulative score, while Reciprocal Rank gives an average of inverse rankings.

<a id="example"></a>

## Example

This is example that demonstrates both the Borda Count and Reciprocal Rank methods, highlighting their differences. This example will use six different rankings of six items.

Here's a Python script that will demonstrate this:

```python
import numpy as np

def borda_count(rankings):
    n_items = len(rankings[0])
    scores = np.zeros(n_items)
    for ranking in rankings:
        scores += np.array(range(n_items, 0, -1))[np.argsort(ranking)]
    return scores

def reciprocal_rank(rankings):
    n_items = len(rankings[0])
    scores = np.zeros(n_items)
    for ranking in rankings:
        scores += 1 / (np.array(ranking) + 1)  # +1 because ranks start from 0
    return scores / len(rankings)

# New rankings (0-indexed) designed to produce different results
rankings = [
    [0, 1, 2, 3, 4, 5],  # Ranking 1
    [1, 0, 2, 3, 4, 5],  # Ranking 2
    [2, 3, 0, 1, 4, 5],  # Ranking 3
    [0, 2, 1, 3, 4, 5],  # Ranking 4
    [3, 1, 2, 0, 4, 5],  # Ranking 5
    [1, 2, 3, 0, 4, 5],  # Ranking 6
]

borda_scores = borda_count(rankings)
rr_scores = reciprocal_rank(rankings)

print("Borda Count Scores:")
for i, score in enumerate(borda_scores):
    print(f"Item {i}: {score}")

print("\nReciprocal Rank Scores:")
for i, score in enumerate(rr_scores):
    print(f"Item {i}: {score:.4f}")

print("\nBorda Count Ranking:")
print(np.argsort(borda_scores)[::-1])

print("\nReciprocal Rank Ranking:")
print(np.argsort(rr_scores)[::-1])
```

Here's the output:

```
Borda Count Scores:
Item 0: 27.0
Item 1: 29.0
Item 2: 28.0
Item 3: 24.0
Item 4: 12.0
Item 5: 6.0

Reciprocal Rank Scores:
Item 0: 0.5972
Item 1: 0.4861
Item 2: 0.4583
Item 3: 0.5417
Item 4: 0.2000
Item 5: 0.1667

Borda Count Ranking:
[1 2 0 3 4 5]

Reciprocal Rank Ranking:
[0 3 1 2 4 5]

```

<a id="key-observations"></a>

### Key observations

1. Borda Count Ranking: [1 2 0 3 4 5]
   - Item 1 has the highest score, followed by 2, 0, 3, 4, and 5.

2. Reciprocal Rank Ranking: [0 3 1 2 4 5]
   - Item 0 has the highest score, followed by 3, 1, 2, 4, and 5.

<a id="the-main-differences"></a>

### The main differences

#### Top Ranking

   - Borda Count ranks item 1 first, while Reciprocal Rank ranks item 0 first.
   - This is because Reciprocal Rank gives more weight to the first-place rankings, which item 0 has more of (item 1 has 2 times rank 0, two times rank 1, and item 0 has also 2 times rank 0 but only once rank 1).

#### Score Distribution

   - In Borda Count, (typically) the scores are more evenly distributed, especially among the top items.
   - In Reciprocal Rank, (typically) there's a larger gap between the top-ranked items and the rest.

#### Sensitivity to Top Rankings

   - Reciprocal Rank is more sensitive to first-place rankings, which benefits item 0.
   - Borda Count considers all positions more equally, which benefits item 1 due to its consistent high (but not always first) rankings.

This example clearly demonstrates how Borda Count and Reciprocal Rank can produce different final rankings based on their different approaches to scoring. Borda Count tends to favor consistent performance across all ranks, while Reciprocal Rank gives more weight to top rankings, especially first-place finishes.

<a id="which-one-to-use-and-when"></a>

## Which one to use and when?

The choice between Borda Count and Reciprocal Rank Combining depends on the specific context and goals of your ranking task. Here are some practical recommendations for when to use each method:

<a id="borda-count-is-better-when"></a>

### Borda Count is better when...

1. **Equal importance across all ranks**: You want to give equal weight to all positions in the ranking.

2. **Comprehensive evaluation**: The goal is to reward consistent performance across all ranks, not just top positions.

3. **Large number of items**: Dealing with a large set of items where distinguishing between lower ranks is important.

4. **Transparency**: You need a method that's easy to explain to stakeholders or users.

5. **Voting systems**: In scenarios like political elections where fairness across all options is crucial.

<a id="reciprocal-rank-is-better-when"></a>

### Reciprocal Rank is better when...

1. **Emphasis on top rankings**: The top few positions are significantly more important than lower ones.

2. **Information retrieval**: Particularly useful in search engine result evaluation where the first few results matter most.

3. **User behavior modeling**: When modeling scenarios where users typically focus on top results (e.g., web search, recommendations).

4. **Sparse data**: In cases where you have incomplete rankings or only care about the position of relevant items.

5. **Normalization**: You need scores that are always between 0 and 1, regardless of the number of items.

<a id="additional-considerations"></a>

### Additional considerations

1. If you're dealing with expert opinions where being consistently in the top few ranks is crucial, Reciprocal Rank might be more appropriate.

2. For competitions or evaluations where performance across all levels matters, Borda Count could be more suitable.

3. In scenarios where you want to balance between rewarding top performance and consistent overall performance, you might consider using a combination of both methods or a modified version.

4. If your ranking problem involves a mix of complete and partial rankings, Reciprocal Rank might be more flexible.

<a id="summary"></a>

## Summary

These tables summarize the main properties and key differences between Borda Count and Reciprocal Rank, highlighting how they differ in their approach to combining rankings and the resulting implications for their use in various scenarios.

**Table 1:** *Main Properties of Borda Count and Reciprocal Rank*

| Property       | Borda Count                                                               | Reciprocal Rank                                          |
| -------------- | ------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Scoring Method** | Assigns points based on position (n points for top, n-1 for second, etc.) | Uses reciprocal of rank (1/rank)                         |
| **Calculation**    | Sums points across all rankings                                           | Averages reciprocal ranks across all rankings            |
| **Score Range**    | Depends on number of items and rankings                                   | Always between 0 and 1                                   |
| **Final Ranking**  | Determined by total points (higher is better)                             | Determined by average reciprocal rank (higher is better) |

**Table 2:** *Key Differences between Borda Count and Reciprocal Rank.*

| Aspect                      | Borda Count                                       | Reciprocal Rank                |
| --------------------------- | ------------------------------------------------- | ------------------------------ |
| **Scale**                       | Linear                                            | Non-linear                     |
| **Sensitivity to Top Rankings** | Treats all positions with equal weight difference | More sensitive to top rankings |
| **Lower Ranking Impact**        | Significant impact                                | Less impact                    |
| **Ties Handling**               | Can often result in ties                          | Less likely to produce ties    |
| **Interpretation**              | Cumulative score across all rankings              | Average of inverse rankings    |
