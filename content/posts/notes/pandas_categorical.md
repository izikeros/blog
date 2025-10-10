---
Title: Pandas Categorical - Benefits and Use Cases
Slug: pandas-categorical-benefits-and-use-cases
Date: 2024-10-01
Modified: 2024-10-01
Status: published
tags:
  - pandas
Category: note
---

## TL;DR

1. **Memory efficiency**: Uses less memory for data with limited unique values.
2. **Improved performance**: Faster computations and aggregations, especially for large datasets.
3. **Meaningful order**: Allows custom ordering of categories for sorting and plotting.
4. **Type safety**: Ensures only predefined categories can be assigned, preventing errors.
5. **Faster groupby operations**: Improves performance when grouping data.

These benefits are most noticeable with large datasets and columns having a limited number of unique values that repeat frequently.

Using pandas categorical data type instead of int or string can be beneficial in several scenarios. Here are some reasons and examples where using categorical is better:

## 1. Memory efficiency

For datasets with a limited number of unique values that repeat frequently, categorical data uses less memory than int or string.

Example:
```python
import pandas as pd
import numpy as np

# Create a large DataFrame with repeated values
df = pd.DataFrame({'status': np.random.choice(['active', 'inactive', 'pending'], 1000000)})

# Compare memory usage
print(f"String dtype: {df['status'].memory_usage(deep=True) / 1e6:.2f} MB")
print(f"Categorical dtype: {df['status'].astype('category').memory_usage(deep=True) / 1e6:.2f} MB")
```

Outcome:
```
String dtype: 64.00 MB
Categorical dtype: 1.00 MB
```

## 2. Improved performance

Categorical data can lead to faster computations and aggregations, especially for large datasets.

Example:
```python
import pandas as pd
import numpy as np
import time

# Create a large DataFrame with repeated values
df = pd.DataFrame({'color': np.random.choice(['red', 'green', 'blue', 'yellow'], 1000000)})

# Compare performance for value_counts()
start = time.time()
df['color'].value_counts()
print(f"String dtype: {time.time() - start:.4f} seconds")

df['color'] = df['color'].astype('category')
start = time.time()
df['color'].value_counts()
print(f"Categorical dtype: {time.time() - start:.4f} seconds")
```

Outcome:
```
String dtype: 0.0779 seconds
Categorical dtype: 0.0090 seconds
```

## 3. Meaningful order

Categorical data allows you to specify a custom order for the categories, which is useful for sorting and plotting.

Example:
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'size': ['small', 'medium', 'large', 'small', 'large', 'medium']})

# Create an ordered categorical column
df['size_cat'] = pd.Categorical(df['size'], categories=['small', 'medium', 'large'], ordered=True)

# Sort by the categorical column
print(df.sort_values('size_cat'))

# Plot with a meaningful order
df['size_cat'].value_counts().plot(kind='bar')
plt.show()
```

## 4. Type safety

Categorical data ensures that only predefined categories can be assigned, preventing data entry errors.

Example:
```python
import pandas as pd

df = pd.DataFrame({'fruit': ['apple', 'banana', 'cherry']})
df['fruit'] = pd.Categorical(df['fruit'], categories=['apple', 'banana', 'cherry'])

# This will raise a ValueError
try:
    df.loc[3] = 'orange'
except ValueError as e:
    print(f"Error: {e}")
```

## 5. Improved groupby operations

Categorical data can speed up groupby operations, especially when there are many groups.

Example:
```python
import pandas as pd
import numpy as np
import time

# Create a large DataFrame with repeated values
df = pd.DataFrame({
    'group': np.random.choice(['A', 'B', 'C', 'D', 'E'], 1000000),
    'value': np.random.randn(1000000)
})

# Compare performance for groupby operation
start = time.time()
df.groupby('group')['value'].mean()
print(f"String dtype: {time.time() - start:.4f} seconds")

df['group'] = df['group'].astype('category')
start = time.time()
df.groupby('group')['value'].mean()
print(f"Categorical dtype: {time.time() - start:.4f} seconds")
```

```
String dtype: 0.1000 seconds 
Categorical dtype: 0.0198 seconds
```
