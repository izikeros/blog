---
Title: How to Convert Pandas DataFrame to Markdown Table?
Slug: how-to-convert-pandas-dataframe-to-markdown-table
Date: 2022-07-05
Modified: 2023-12-27
Status: published
tags:
  - pandas
  - table
  - markdown
  - conversion
Category: note
---

up: [[MOC_Pandas]]

<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Method 1: Directly from pandas](#method-1-directly-from-pandas)
- [Method 2: Direct use of tabulate package](#method-2-direct-use-of-tabulate-package)
- [Method 3: Generate a Styled HTML Table](#method-3-generate-a-styled-html-table)
- [References](#references)

<!-- /MarkdownTOC -->
Generating an ASCII table from a pandas DataFrame can be accomplished in several ways. In this post, we will explore three convenient methods to help you convert pandas DataFrame to a markdown table. 

<a id="method-1-directly-from-pandas"></a>
## Method 1: Directly from pandas

The Pandas library since version 1.0 supports markdown conversion by relying on `tabulate` package as optional dependency. So, remember to `pip install tabulate` or `conda install tabulate` before using `to_markdown()` method. Here is an example of how it works:

```python
import pandas as pd

# prepare some data for demonstration
df = pd.DataFrame({
    "weekday": ["Monday", "Thursday", "Wednesday"],
    "temperature": [20, 30, 25],
    "precipitation": [100, 200, 150],
}).set_index("weekday")

print(df.to_markdown())
```

This produces the following output:

```
| weekday   |   temperature |   precipitation |
|:----------|--------------:|----------------:|
| Monday    |            20 |             100 |
| Thursday  |            30 |             200 |
| Wednesday |            25 |             150 |
```

You can also see similar example in the [Pandas documentation](https://pandas.pydata.org/pandas-docs/version/1.0.0/whatsnew/v1.0.0.html#converting-to-markdown).

<a id="method-2-direct-use-of-tabulate-package"></a>
## Method 2: Direct use of tabulate package

The `tabulate` Python package is an excellent tool for generating markdown tables from `pandas.DataFrame`.

Here is how you can use it:

```python
from tabulate import tabulate

print(tabulate(df, tablefmt="pipe", headers="keys"))
```

The output should looks identical as above:

```
| weekday   |   temperature |   precipitation |
|:----------|--------------:|----------------:|
| Monday    |            20 |             100 |
| Thursday  |            30 |             200 |
| Wednesday |            25 |             150 |
```

<a id="method-3-generate-a-styled-html-table"></a>
## Method 3: Generate a Styled HTML Table

You can also create a nicely styled table like this:

```python
styled_df = df.style.background_gradient(subset=['temperature'],
			  cmap='BuGn')
```

This outputs a stylized DataFrame `styled_df` which you can then export to html and include in your markdown document:

```python
print(styled_df.to_html())
```

This will produce output that you can paste to the markdown file:
```html
<style type="text/css">
#T_7a378_row0_col0 {
  background-color: #f7fcfd;
  color: #000000;
}
#T_7a378_row1_col0 {
  background-color: #00441b;
  color: #f1f1f1;
}
#T_7a378_row2_col0 {
  background-color: #65c2a3;
  color: #000000;
}
</style>
<table id="T_7a378">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_7a378_level0_col0" class="col_heading level0 col0" >temperature</th>
      <th id="T_7a378_level0_col1" class="col_heading level0 col1" >precipitation</th>
    </tr>
    <tr>
      <th class="index_name level0" >weekday</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_7a378_level0_row0" class="row_heading level0 row0" >Monday</th>
      <td id="T_7a378_row0_col0" class="data row0 col0" >20</td>
      <td id="T_7a378_row0_col1" class="data row0 col1" >100</td>
    </tr>
    <tr>
      <th id="T_7a378_level0_row1" class="row_heading level0 row1" >Thursday</th>
      <td id="T_7a378_row1_col0" class="data row1 col0" >30</td>
      <td id="T_7a378_row1_col1" class="data row1 col1" >200</td>
    </tr>
    <tr>
      <th id="T_7a378_level0_row2" class="row_heading level0 row2" >Wednesday</th>
      <td id="T_7a378_row2_col0" class="data row2 col0" >25</td>
      <td id="T_7a378_row2_col1" class="data row2 col1" >150</td>
    </tr>
  </tbody>
</table>
```

<a id="references"></a>
## References
[How to programmatically convert pandas dataframe to markdown table](https://stackoverflow.com/questions/33181846/programmatically-convert-pandas-dataframe-to-markdown-table)
