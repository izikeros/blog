---
Category: note
Date: 2023-02-13
Modified: 2023-07-12
Slug: plotly_transparent_background
Status: published
Tags:
  - plotly
  - transparency
  - transparent-background
  - visualization
Title: How to Set Transparent Background for Plotly Plot?
---
Setting a transparent background for a Plotly plot can be accomplished using different methods depending on the use case. In this answer, I will provide some examples of how to achieve this.

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Method 1: Using the "layout" parameter](#method-1-using-the-layout-parameter)
- [Method 2: Using the "config" parameter](#method-2-using-the-config-parameter)
- [Method 3: Using the "to_image" function](#method-3-using-the-to_image-function)

<!-- /MarkdownTOC -->

<a id="method-1-using-the-layout-parameter"></a>

## Method 1: Using the "layout" parameter

One simple way to set the background of a Plotly plot to transparent is by using the "layout" parameter. In the "layout" parameter, you can set the color of the background to "rgba(0,0,0,0)", which stands for "red, green, blue, alpha", where "alpha" is the opacity level, and setting it to 0 makes the background fully transparent. Here's an example:

```python
import plotly.graph_objects as go

fig = go.Figure()

# Add traces to the figure

fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)

fig.show()

```

In this example, we create an empty figure and add traces to it. Then, we set the `paper_bgcolor` and `plot_bgcolor` parameters to `rgba(0,0,0,0)` to make the background transparent.

<a id="method-2-using-the-config-parameter"></a>

## Method 2: Using the "config" parameter

Another way to set the background of a Plotly plot to transparent is by using the "config" parameter. In the `config` parameter, you can set the `displayModeBar` parameter to `False` to remove the toolbar from the plot, and set the `staticPlot` parameter to `True` to disable interactivity. Here's an example:

```python
import plotly.graph_objects as go

fig = go.Figure()

# Add traces to the figure

fig.show(config={'displayModeBar': False, 'staticPlot': True})

```

In this example, we create an empty figure and add traces to it. Then, we set the `displayModeBar` parameter to `False` to remove the toolbar from the plot, and set the `staticPlot` parameter to True to disable interactivity.

<a id="method-3-using-the-to_image-function"></a>

## Method 3: Using the "to_image" function

Finally, you can also export the Plotly plot to an image format and set the background of the image to transparent. In this case, we can use the `to_image` function from the `plotly.io` module to export the plot to a PNG image format with a transparent background. Here's an example:

```python
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()

# Add traces to the figure

image_bytes = pio.to_image(fig, format='png', engine='kaleido', width=800, height=600, scale=2, transparent=True)

with open('my_plot.png', 'wb') as f:
    f.write(image_bytes)

```

In this example, we create an empty figure and add traces to it. Then, we use the `to_image` function to export the plot to a PNG image format with a transparent background. We set the `transparent` parameter to `True` to make the background transparent.

See also: [python - Setting Background color to transparent in Plotly plots - Stack Overflow](https://stackoverflow.com/questions/29968152/setting-background-color-to-transparent-in-plotly-plots)
