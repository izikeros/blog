import altair as alt
import numpy as np
import pandas as pd

# Generate some random data
data = np.random.randn(1000)

# create dataframe
df = pd.DataFrame({"value": data})

# Create a histogram with x axis labeled "Value" and y axis labeled "Frequency".
# Plot has title "Histogram"
alt.Chart(df).mark_bar().encode(
    alt.X("value", bin=alt.Bin(maxbins=30), title="Value"),
    y="count()"
).properties(title="Histogram", ytitle="Frequency")
