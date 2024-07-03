---
Title: How to Create Animated Gif From Matplotlib Plot in Python?
Slug: how-to-create-animated-gif-from-matplotlib-plot-in-python
Date: 2024-07-03
Modified: 2024-07-03
Status: published
tags: visualization, animation, matplotlib, python
Category: note
---

Animated visualizations can be a powerful way to showcase data trends over time or illustrate dynamic processes. In this tutorial, we'll learn how to create an animated GIF using Matplotlib in Python. We'll walk through the process step-by-step and provide a working code example that you can adapt for your own projects.

## Prerequisites
Before we begin, make sure you have the following libraries installed:
- matplotlib
- numpy
- pillow (PIL)

You can install them using pip:

```sh
pip install matplotlib numpy pillow
```

## Set up the plot

First, we'll create a function that generates our plot. In this example, we'll create a simple sine wave that changes frequency over time.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image
import io

def create_plot(i):
    plt.clf()
    x = np.linspace(0, 10, 1000)
    y = np.sin((i + 1) * x)
    plt.plot(x, y)
    plt.title(f"Sine Wave (Frequency: {i+1})")
    plt.xlim(0, 10)
    plt.ylim(-1.5, 1.5)
```

## Save frames as images

We'll save each frame of the animation as an individual image:

```python
frames = []
for i in range(10):
    create_plot(i)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    frames.append(Image.open(buf))
```

## Create and save the animated GIF

Finally, we'll use Pillow to create the animated GIF from our saved frames:

```python
frames[0].save('sine_wave_animation.gif', 
               save_all=True, 
               append_images=frames[1:], 
               duration=200, 
               loop=0)
```

Putting it all together:

Here's the complete code that combines all the steps:

```python
import io

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from PIL import Image


def create_plot(i):
    plt.clf()
    x = np.linspace(0, 10, 1000)
    y = np.sin((i + 1) * x)
    plt.plot(x, y)
    plt.title(f"Sine Wave (Frequency: {i+1})")
    plt.xlim(0, 10)
    plt.ylim(-1.5, 1.5)


# Create the animation
fig = plt.figure(figsize=(10, 6))

# Save frames as images
frames = []
for i in range(10):
    create_plot(i)
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    frames.append(Image.open(buf))

# Create and save the animated GIF
frames[0].save(
    "sine_wave_animation.gif",
    save_all=True,
    append_images=frames[1:],
    duration=200,
    loop=0,
)

print("Animation saved as 'sine_wave_animation.gif'")

```
(Here, you can download this code from GitHub [Gist](https://gist.github.com/izikeros/61c18539c80ba8fdd83a1048cde3409f))

This code will create an animated GIF showing a sine wave with changing frequency. The resulting GIF will be saved as 'sine_wave_animation.gif' in your current working directory.
