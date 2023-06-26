---
title: Plotting histogram with 5 different python libraries
date: 2023-02-18
modified: 2023-02-18
status: draft
tags: tag1, tag2
summary: summary
category: note
citation_needed: false
---
#blog/post-idea 

How to plot histogram using  matplotlib, plotly, seaborn, altair, bokeh and let-plot libraries. Show me python code snippets for each library. Include all necessary imports, use 5 bins and the same single serie of random numbers in the examples.  Add title and axis labels to the exemplary plot. Ensure all field has specified with a type for altair. Ensure that the plot will be properly displayed in the Jupyter notebook.


## 1.  matplotlib

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
data = np.random.randn(1000)

# Plot the histogram
plt.hist(data, bins=5, histtype='bar')

# Add title and axis labels
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Show the plot
plt.show()

```

## 2. plotly

```python
import plotly.graph_objects as go

# Generate some random data
data = [np.random.randn(1000) for _ in range(5)]

# Plot the histogram
fig = go.Figure(data=[go.Histogram(x=data[i]) for i in range(5)])
fig.show()

```


## 3.  bokeh

```python
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Generate some random data
data = [np.random.randn(1000) for _ in range(5)]

# Convert the data to a ColumnDataSource
source = ColumnDataSource(data=dict(x=data))

# Create the plot
p = figure(plot_height=400)

# Add histograms for each data set
for i, col in enumerate(data):
    p.quad(bottom=0, top=col, left=i+0.9, right=i+1.1, alpha=0.6)

# Show the plot
show(p)

```

## 4.  altair

```python
import altair as alt

# Generate some random data
data = [np.random.randn(1000) for _ in range(5)]

# Convert the data to a Altair data object
alt_data = alt.Data(values=[alt.X(field=f'data_{i}', type='quantitative') for i in range(5)])

# Create the plot
hist = alt.Chart(alt_data).mark_bar().encode(
    alt.X("data_0", bin=alt.Bin(maxbins=20)),
    y='count()'
)

# Show the plot
hist.show()

```

## 5.  lets-plot

```python
import numpy as np
import pandas as pd
import lets_plot as lp

# Generate some random data
data = [np.random.randn(1000) for _ in range(5)]

# Convert the data to a Pandas dataframe
df = pd.DataFrame({f'data_{i}': data[i] for i in range(5)})

# Create the plot
hist = lp.ggplot(df) + lp.geom_histogram(lp.aes(x='data_0'), bins=20)

# Show the plot
hist.show()
```