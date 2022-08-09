---
title: Pandas dataframe schema and data types validation
date: 2022-04-27
status: published
tags: pandas, pandas/schema, pandas/validation, pandera, dataenforce, alternatives, alternative, great-expectations,
slug: pandas-dataframe-validation
category: note
citation_needed: false
---

# Contents
<!-- MarkdownTOC levels='2,3' autolink=True autoanchor=True -->

- [Pandera \(515 stars\) - column validation \(columns, types\), DataFrame Schema](#pandera-515-stars---column-validation-columns-types-dataframe-schema)
- [Dataenforce \(59 stars\) - columns presence validation](#dataenforce-59-stars---columns-presence-validation)
  - [for type hinting \(column names check, dtype check\)](#for-type-hinting-column-names-check-dtype-check)
  - [to enforce validation at runtime](#to-enforce-validation-at-runtime)
- [Great expectations - data validation](#great-expectations---data-validation)
  - [automated expectations from profiling](#automated-expectations-from-profiling)
- [pandas_schema \(135 stars\)](#pandas_schema-135-stars)
- [Other Data Validation Libraries](#other-data-validation-libraries)
  - [Generic Python object data validation](#generic-python-object-data-validation)
  - [pandas-specific data validation](#pandas-specific-data-validation)

<!-- /MarkdownTOC -->

Two things I found most useful and use most are Pandera and Dataenforce.

<a id="pandera-515-stars---column-validation-columns-types-dataframe-schema"></a>
## Pandera (515 stars) - column validation (columns, types), DataFrame Schema
```python
import pandera as pa

schema = pa.DataFrameSchema(
    columns={
        "height_in_cm": pa.Column(pa.Int),
        "age_category": pa.Column(pa.String),
    },
    index=pa.Index(pa.Int, name="person_id"),
)

# Usage for schema check
schema(df_dataset)
```
Medium article ["Validate Your pandas DataFrame with Pandera](
https://towardsdatascience.com/validate-your-pandas-dataframe-with-pandera-2995910e564)

<a id="dataenforce-59-stars---columns-presence-validation"></a>
## Dataenforce (59 stars) - columns presence validation
used for
<a id="for-type-hinting-column-names-check-dtype-check"></a>
### for type hinting (column names check, dtype check)
```python
from dataenforce import Dataset
def process_data(data: Dataset["id": int, "name": object, "latitude": float, "longitude": float])
  pass
```

<a id="to-enforce-validation-at-runtime"></a>
### to enforce validation at runtime
```python
from dataenforce import Dataset, validate

@validate
def process_data(data: Dataset["id", "name"]):
  pass
```
Github Link: [dataenforce](https://github.com/CedricFR/dataenforce)


<a id="great-expectations---data-validation"></a>
## Great expectations - data validation

<a id="automated-expectations-from-profiling"></a>
### automated expectations from profiling
https://greatexpectations.io/blog/pandas-profiling-integration/
great expectations + Pandas Profiling
```python
import pandas as pd
from pandas_profiling import ProfileReport

# Load your dataframe
df = pd.read_csv('yellow_tripdata_sample_2019-01.csv')

# Then run Pandas Profiling
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

# And obtain an Expectation Suite from the profile report
suite = profile.to_expectation_suite(suite_name="my_pandas_profiling_suite")
```

<a id="pandas_schema-135-stars"></a>
## pandas_schema (135 stars)


<a id="other-data-validation-libraries"></a>
## Other Data Validation Libraries
Here are a few other alternatives for validating Python data structures.

<a id="generic-python-object-data-validation"></a>
### Generic Python object data validation
- voloptuous
- schema

<a id="pandas-specific-data-validation"></a>
### pandas-specific data validation
- opulent-pandas
- PandasSchema
- pandas-validator (archived)
- table_enforcer (13 stars)