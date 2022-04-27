---
title: Pandas dataframe schema and data types validation
date: 2022-04-27
status: published
tags: 
summary: 
slug: pandas-dataframe-validation
category: note
citation_needed: false
todo: 
---
# Contents
<!-- MarkdownTOC levels='1,2,3' autolink=True -->

- [Pandera \(515 stars\) - column validation \(columns, types\), DataFrame Schema](#pandera-515-stars---column-validation-columns-types-dataframe-schema)
- [Dataenforce \(59 stars\) - columns presence validation](#dataenforce-59-stars---columns-presence-validation)
  - [for type hinting \(column names check, dtype check\)](#for-type-hinting-column-names-check-dtype-check)
  - [for validation](#for-validation)
- [Great expectations - data validation](#great-expectations---data-validation)
  - [automated expectations from profiling](#automated-expectations-from-profiling)
- [pandas_schema \(135 stars\)](#pandas_schema-135-stars)
- [Other Data Validation Libraries](#other-data-validation-libraries)
  - [Generic Python object data validation](#generic-python-object-data-validation)
  - [pandas-specific data validation](#pandas-specific-data-validation)

<!-- /MarkdownTOC -->

Two things I found most usefull and use most is Pandera and Dataenforce.

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

## Dataenforce (59 stars) - columns presence validation
used for
### for type hinting (column names check, dtype check)
```python
from dataenforce import Dataset
def process_data(data: Dataset["id": int, "name": object, "latitude": float, "longitude": float])
  pass
```

### for validation
```python
from dataenforce import Dataset, validate

@validate
def process_data(data: Dataset["id", "name"]):
  pass
```
Github Link: [dataenforce](https://github.com/CedricFR/dataenforce)


## Great expectations - data validation

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

## pandas_schema (135 stars)


## Other Data Validation Libraries
Here are a few other alternatives for validating Python data structures.

### Generic Python object data validation
- voloptuous
- schema

### pandas-specific data validation
- opulent-pandas
- PandasSchema
- pandas-validator (archived)
- table_enforcer (13 stars)