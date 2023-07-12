---
Category: note
Date: '2023-02-13'
Modified: '2023-07-12'
Slug: plotly-how-to-set-y-axis-range
Status: published
Tags: plotly, y-axis-range, set-range, axis, data-visualization, python, scatter-plot, data-analysis, data-interpretation, manual-range-setting, automatic-range-scaling, maximum-value-in-data-set, data-range-control
Title: How to Set the Range of the Y Axis in Plotly?
---

## Setting the Range of the Y Axis in Plotly

When it comes to visualizing data using Plotly, one of the most important aspects is setting the range of the Y axis. By setting the Y axis range, you can control the vertical scale of your graph and make it easier to interpret your data. In this post, we’ll explore the various use cases and methods for setting the range of the Y axis in Plotly.

### Use Cases

There are many different scenarios in which you might want to set the range of the Y axis in Plotly. For example, you might want to:

-   Zoom in on a specific range of data
-   Focus on a specific data point or cluster of data points
-   Compare the relative sizes of different data sets
-   Ensure that your data fits within a specific range of values

### Method 1: Setting the Range Manually

One of the most straightforward ways to set the range of the Y axis is to do so manually. To accomplish this, you can use the `layout` object and set the `yaxis.range` property to an array of two values. For example:

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Scatter(y=[1, 3, 2])],
    layout=go.Layout(yaxis=dict(range=[0, 5]))
)

fig.show()

```
This code will create a simple scatter plot with Y values of 1, 3, and 2. The `yaxis.range` property is set to `[0, 5]`, which will ensure that the Y axis ranges from 0 to 5.

### Method 2: Automatically Scaling the Y Axis

Another way to set the range of the Y axis is to allow Plotly to do it automatically. By default, Plotly will scale the Y axis based on the values in your data set. This can be useful if you want to ensure that your entire data set is visible, but it can also result in a skewed or misleading graph. To enable automatic scaling, simply omit the `yaxis.range` property from your layout object:

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Scatter(y=[1, 3, 2])],
    layout=go.Layout()
)

fig.show()

```
This code will create the same scatter plot as before, but with the Y axis automatically scaled based on the values in the data set.

### Method 3: Setting the Range Based on Data

Finally, you can set the range of the Y axis based on specific data values. For example, you might want to ensure that your Y axis ranges from 0 to the maximum value in your data set. To do this, you can use the `max` function to find the maximum value in your data set and set the `yaxis.range` property accordingly:

```python
import plotly.graph_objects as go

y_values = [1, 3, 2]
y_max = max(y_values)

fig = go.Figure(
    data=[go.Scatter(y=y_values)],
    layout=go.Layout(yaxis=dict(range=[0, y_max]))
)

fig.show()

```

This code will create the same scatter plot as before, but with the Y axis ranging from 0 to the maximum value in the data set (in this case, 3).

See also: [python - Plotly: How to set the range of the y axis? - Stack Overflow](https://stackoverflow.com/questions/55704058/plotly-how-to-set-the-range-of-the-y-axis)

up::[[MOC_Visualization]]