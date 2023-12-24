---
Category: note
Date: '2023-02-12'
Modified: '2023-07-12'
Slug: how-to-select-rows-from-DataFrame-based-on-column-values
Status: published
Tags: python, pandas, pandas/indexing, dataframe
Title: How to Select Rows From a DataFrame Based on Column Values
prompt: Give me long, stacoverflow-style text with snippets of code, analyse various use cases and various methods how to achieve this. Give me response as pre-formatted text (do not render tables and code fences)
---
To select rows from a pandas DataFrame based on column values, you can use various methods. Here are some of the most common ones:

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [1.  Using Boolean indexing](#1-using-boolean-indexing)
- [2.  Using the query\(\) method](#2-using-the-query-method)
- [3.  Using the loc\(\) method](#3-using-the-loc-method)
- [4.  Using the iloc\(\) method](#4-using-the-iloc-method)

<!-- /MarkdownTOC -->

<a id="1-using-boolean-indexing"></a>

## 1.  Using Boolean indexing

This involves creating a Boolean condition based on the values in a specific column, and then passing that condition to the DataFrame to select only the rows that meet the condition. For example:

```python
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Gender': ['F', 'M', 'M', 'M']
})

# Select only the rows where Gender is 'M'
male_df = df[df['Gender'] == 'M']
print(male_df)

```

This will output:

```
      Name  Age Gender
1      Bob   30      M
2  Charlie   35      M
3    David   40      M

```

<a id="2-using-the-query-method"></a>

## 2.  Using the query() method

This method allows you to select rows based on a more complex condition using a string expression. For example:

```python
# Select only the rows where Age is greater than 30
over_30_df = df.query('Age > 30')
print(over_30_df)

```

This will output:

```
      Name  Age Gender
2  Charlie   35      M
3    David   40      M

```

<a id="3-using-the-loc-method"></a>

## 3.  Using the loc() method

This method allows you to select rows based on a specific label or index. For example:

```python
# Set the Name column as the index
df.set_index('Name', inplace=True)

# Select only the row for Bob
bob_df = df.loc['Bob']
print(bob_df)

```

This will output:

```
Age       30
Gender     M
Name: Bob, dtype: object

```

<a id="4-using-the-iloc-method"></a>

## 4.  Using the iloc() method

This method allows you to select rows based on their integer position in the DataFrame. For example:

```python
# Select the first two rows
first_two_df = df.iloc[:2]
print(first_two_df)

```

This will output:

```
      Age Gender
Name            
Alice   25      F
Bob     30      M

```

There are some other methods, see stackoverflow answers to question: [How do I select rows from a DataFrame based on column values?](https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values)
