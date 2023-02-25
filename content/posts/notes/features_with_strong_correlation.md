---
Title: List of features with strongest correlation
Slug: features-with-strong-correlation
Date: 2023-02-21
Modified: 2023-02-21
Status: published
Tags: pandas, dataframe, correlation, python, data-analysis, machine-learning, AI, decorrelation
Category: note
prompt: I have dataframe with features in columns. The number of features is large - more than 1000. How to get list of the features that has the stongest correlation? Give me python code for that.
---

The code from this note is useful in case when there is a lot of features (e.g 1k+). In such case it is difficult to analyse visually heatmap of correlation matrix (e.g. plotted with sns.heatmap(), see beautiful example [here](https://seaborn.pydata.org/examples/many_pairwise_correlations.html)). Instead we extract pairs with the strongest correlation.

To get a list of features with the strongest correlation in a pandas DataFrame, you can use the `corr()` method to calculate the correlation between all pairs of columns. Here is the Python code to do so:

```python
import pandas as pd
import seaborn as sns

# Load the dataset
df = sns.load_dataset('tips')

# Calculate the correlation matrix
corr_matrix = df.corr()

# Get the top n pairs with the highest correlation
n = 5 # change this to the number of pairs you want to get
top_pairs = corr_matrix.unstack().sort_values(ascending=False)[:n*2]

# Create a list to store the top pairs without duplicates
unique_pairs = []

# Iterate over the top pairs and add only unique pairs to the list
for pair in top_pairs.index:
    if pair[0] != pair[1] and (pair[1], pair[0]) not in unique_pairs:
        unique_pairs.append(pair)

# Create a dataframe with the top pairs and their correlation coefficients
top_pairs_df = pd.DataFrame(columns=['feature_1', 'feature_2', 'corr_coef'])
for i, pair in enumerate(unique_pairs[:n]):
    top_pairs_df.loc[i] = [pair[0], pair[1], corr_matrix.loc[pair[0], pair[1]]]

# Print the top pairs as a dataframe
display(top_pairs_df)
```

In this code, we use the `unstack()` method to transform the correlation matrix into a Series of pairs of column names and their correlation values. We then sort the Series in descending order and get the top `2*n` pairs (in correlation matrix pairs appear twice, except correlation of the feature with itself). 

up::[[MOC_AI]]