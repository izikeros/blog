---
Title: Pandas Schema Validation
Slug: pandas-schema-validation
Date: 2021-01-16
modified: 2023-01-16
Start: 2023-01-16
Tags: pandas, python, schema-validation, pandas-schema, great_expectations, pandera, data-enforce, data-manipulation, data-analysis, tools-for-schema-validation, methods-for-schema-validation, dataframe-validation, dtype-validation, leading-whitespace-validation, trailing-whitespace-validation, in-list-validation
Category: Machine Learning
Image: /images/head/elegant_panda.jpg
banner: "/images/head/elegant_panda.jpg"
Summary: Overview of the available tools and methods for schema validation in pandas, examplary code snippets and recommendation for when to use given tool.
Status: published
prompt:
todo: validate the text for libraries, validate code snippets, consider adding errors, mention decorators
---
<!-- MarkdownTOC levels="2,3" autolink="true" autoanchor="true" -->

- [Overview of Available Tools and Methods](#overview-of-available-tools-and-methods)
    - [Built-in Attributes](#built-in-attributes)
    - [Pandas Schema](#pandas-schema)
    - [Great Expectations](#great-expectations)
    - [Pandera](#pandera)
    - [Data-enforce](#data-enforce)
- [Comparison and Discussion](#comparison-and-discussion)

<!-- /MarkdownTOC -->

Pandas is a widely used library for data manipulation and analysis in Python. To ensure the data is in the correct format and conforms to certain constraints, schema validation is crucial. This process can be useful in various situations such as when importing data from external sources or before performing further analysis or machine learning tasks.

There are several tools and methods available for schema validation in pandas such as `pandas_schema`, `great_expectations`, `pandera` and `data-enforce`. [pandas_schema](https://github.com/multimeric/PandasSchema) and [great_expectations](https://docs.greatexpectations.io/en/latest/index.html)  are widely used libraries for pandas data validation. [pandera](https://github.com/unionai-oss/pandera)  and [data-enforce](https://github.com/CedricFR/dataenforce)  are also popular libraries for pandas data validation.

In this article, we will overview the available tools and methods for schema validation in pandas and provide example code snippets and links to further resources. We will also discuss the advantages and disadvantages of each tool and provide recommendations for when to use them.

<a id="overview-of-available-tools-and-methods"></a>
## Overview of Available Tools and Methods

The tools and methods discussed below accompanying exemplary code snippets. You can use the following contents of a `data.csv` that comply with the schema used in this article:
```
name,age,gender,col1,col2,col3,col4,col5
Alice,25,female,1,2.5,text1,True,2022-01-01
Bob,30,male,2,3.5,text2,False,2022-02-01
Charlie,35,male,3,4.5,text3,True,2022-03-01
```

This file contains a dataframe with 8 columns: name, age, gender, col1, col2, col3, col4 and col5.

-   `name` and `gender` are of type object
-   `age` is of type int
-   `col1`,`col2` are of type int and float respectively
-   `col3` is of type object
-   `col4` is of type boolean
-   `col5` is of type datetime

This file can be used in the examples above to perform data validation using different libraries and methods.

Here is an example of the contents of a `data2.csv` file that does not comply with the schema used in the article:

```
name,age,gender,col1,col2,col3,col4,col5
Alice,25,female,1,2.5,text1,True,2022-01-01
Bob,30,male,2,3.5,text2,False,2022-02-01
Charlie,35,male,3,4.5,text3,True,2022-03-01
David,170,male,4,5.5,text4,True,2022-04-01
```

This file contains a dataframe with 8 columns: name, age, gender, col1, col2, col3, col4 and col5.

-   The age of David is 170 which is out of range of the schema defined in the article which is range(0, 150)
-   This file will not comply with the schema defined in the article and will raise an error when trying to validate it using the code provided in the article
-   This file can be used to demonstrate the validation process and how it will raise errors for invalid data.

<a id="built-in-attributes"></a>
### Built-in Attributes

Pandas provides built-in attributes such as `.dtypes` and `.shape` that can be used to check the data types and dimensions of a DataFrame. Here's an example of using these attributes to check that a DataFrame has the expected number of rows and columns, and that the columns have the expected data types:

```python
import pandas as pd

df = pd.read_csv("data.csv")

# Check that the DataFrame has the expected number of rows and columns
assert df.shape == (100, 5)

# Check that the columns have the expected data types
assert df.dtypes == {"col1": int, "col2": float, "col3": object, "col4": bool, "col5": datetime}

```

<a id="pandas-schema"></a>
### Pandas Schema

`pandas_schema` is a library that allows you to specify constraints on a DataFrame and then validate that the DataFrame conforms to those constraints. Here's an example of using the `pandas_schema` library to define a schema for a DataFrame and then validate that the DataFrame conforms to the schema:

```python
from pandas_schema import Column, Schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation, IsDtypeValidation, InListValidation

schema = Schema([
    Column('name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('age', [IsDtypeValidation(int), InListValidation(range(0, 150))]),
    Column('gender', [InListValidation(['male', 'female'])])
])

errors = schema.validate(df)

```

<a id="great-expectations"></a>
### Great Expectations

[Great Expectations](https://docs.greatexpectations.io/docs/) is a library that allows you to define and validate schemas using a more human-readable syntax. Here's an example of using the `great_expectations` library to define a schema for a DataFrame and then validate that the DataFrame conforms to the schema:

```python
import great_expectations as ge

df = ge.read_csv("data.csv")

# Define the schema
schema = {
    "columns": {
        "col1": {"expect_type": "int"},
        "col2": {"expect_type": "float"},
        "col3": {"expect_type": "string"},
        "col4": {"expect_type": "bool"},
        "col5": {"expect_type": "datetime"}
    }
}

# Validate the DataFrame against the schema
validation_result = df.expect(schema)

# Check for any validation errors
if validation_result.success:
    print("Data validation successful")
else:
    print("Validation errors:", validation_result.result)

```

<a id="pandera"></a>
### Pandera

`pandera` is a library that allows you to define and validate schemas using a more human-readable syntax and more functionality. Here's an example of using the `pandera` library to define a schema for a DataFrame and then validate that the DataFrame conforms to the schema:

```python
import pandera as pa

df = pd.read_csv("data.csv")

# Define the schema
schema = pa.DataFrameSchema({
    "col1": pa.Column(pa.Int),
    "col2": pa.Column(pa.Float),
    "col3": pa.Column(pa.String),
    "col4": pa.Column(pa.Boolean),
    "col5": pa.Column(pa.Datetime)
})

# Validate the DataFrame against the schema
schema.validate(df)

```

<a id="data-enforce"></a>
### Data-enforce

`data-enforce` is a library that allows you to define and validate schemas using a more human-readable syntax and more functionality. Here's an example of using the `data-enforce` library to define a schema for a DataFrame and then validate that the DataFrame conforms to the schema:

```python
import data_enforce as de

df = pd.read_csv("data.csv")

# Define the schema
schema = {
    "col1": de.Integer(),
    "col2": de.Float(),
    "col3": de.String(),
    "col4": de.Boolean(),
    "col5": de.Datetime()
}

# Validate the DataFrame against the schema
de.enforce(df, schema)
```

<a id="comparison-and-discussion"></a>
## Comparison and Discussion

Each of these tools has its own advantages and disadvantages depending on the specific use case.

The built-in attributes such as `.dtypes` and `.shape` may be sufficient for simple validation tasks, but they lack advanced functionality such as custom validation logic and integration with other data pipeline tools.

`pandas_schema` and `great_expectations` libraries offer more advanced functionality such as custom validation logic and integration with other data pipeline tools, and they have a more human-readable syntax. `pandera` and `data-enforce` libraries also offer more advanced functionality than the built-in attributes and they have a more human-readable syntax.

The choice of tool will depend on the complexity of the schema and the specific requirements of the project. **If the schema is simple** and you only need to check data types and dimensions, the **built-in attributes** may be sufficient. However, if you need **more advanced functionality** such as custom validation logic or integration with other data pipeline tools, `pandas_schema`, `great_expectations`, `pandera` or `data-enforce` libraries are better choices.

Overall, it is recommended to use `great_expectations` for more complex projects, as it has more functionality and a more human-readable syntax. However, if you're looking for a more lightweight solution `pandas_schema`, `pandera` and `data-enforce` are also good options.

*Any comments or suggestions? [Let me know](mailto:ksafjan@gmail.com?subject=Blog+post).*
