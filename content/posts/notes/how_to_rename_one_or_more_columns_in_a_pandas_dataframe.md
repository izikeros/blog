---
Category: note
Date: 2023-02-12
Modified: 2023-07-12
Slug: how-to-rename-one-or-more-columns-in-pandas-dataframe
Status: published
Summary: Learn how to rename one or more columns in a pandas DataFrame using the `rename` function, including renaming single and multiple columns, performing in-place modifications, and using functions for dynamic renaming.
ai_summary: true
Tags:
  - pandas
  - rename-column
Title: How to Rename One or More Columns in Pandas Dataframe?
---
To rename one or more columns in a pandas DataFrame, you can use the `rename` function. Here are some examples of how to use it:

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [1.  Rename a single column](#1-rename-a-single-column)
- [2.  Rename multiple columns](#2-rename-multiple-columns)
- [3.  Rename columns in place](#3-rename-columns-in-place)
- [4.  Rename columns with a function](#4-rename-columns-with-a-function)
- [5.  Rename columns by index](#5-rename-columns-by-index)

<!-- /MarkdownTOC -->

## 1.  Rename a single column

To rename a single column, you can use a dictionary to map the old column name to the new one. Here's an example:

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

df = df.rename(columns={'A': 'new_column_name'})

print(df)

```

This will rename the column "A" to "new_column_name".

## 2.  Rename multiple columns

To rename multiple columns, you can use a dictionary to map the old column names to the new ones. Here's an example:

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

df = df.rename(columns={'A': 'new_column_name_1', 'B': 'new_column_name_2'})

print(df)

```

This will rename the columns "A" and "B" to "new_column_name_1" and "new_column_name_2", respectively.

## 3.  Rename columns in place

By default, the `rename` function returns a new DataFrame with the columns renamed. However, you can use the `inplace` parameter to modify the dataframe in place. Here's an example:

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

df.rename(columns={'A': 'new_column_name'}, inplace=True)

print(df)

```

This will rename the column "A" to "new_column_name" in place.

## 4.  Rename columns with a function

You can also use a function to rename the columns. The function will be applied to each column name, and the result will be used as the new column name. Here's an example:

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

df = df.rename(columns=lambda x: x.lower())

print(df)

```

This will rename the columns to lowercase.

## 5.  Rename columns by index

You can also rename columns by their index using the `set_axis` method. Here's an example:

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

df = df.set_axis(['new_column_name_1', 'new_column_name_2'], axis=1)

print(df)

```

This will rename the columns by their index.

Overall, there are several ways to rename one or more columns in a pandas DataFrame. You can use a dictionary to map the old column names to the new ones, use a function to rename the columns, or rename the columns by index using the `set_axis` method. Choose the method that best fits your needs depending on your specific use case.
