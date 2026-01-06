---
Category: note
Date: 2022-04-21
Modified: 2023-07-12
Slug: allow-arbitrary-types-pandas-in-pydantic
Status: published
Summary: None
Tags:
  - pydantic
  - pandas
  - type-hints
Title: Allow Arbitrary Types (Such as Pandas Dataframe) in Pydantic
citation_needed: false
---

<!-- MarkdownTOC levels='2,3' autolink=True autoanchor=True -->

- [Solution 1 - allow arbitrary types](#solution-1---allow-arbitrary-types)
- [Solution 2 - create a pythonic type hint for a pd.Dataframe](#solution-2---create-a-pythonic-type-hint-for-a-pddataframe)
- [See also](#see-also)

<!-- /MarkdownTOC -->

## Solution 1 - allow arbitrary types

```python
import pandas as pd
from pydantic import BaseModel


class SubModelInput(BaseModel):
    a: pd.DataFrame
    b: pd.DataFrame

    class Config:
        arbitrary_types_allowed = True
```

## Solution 2 - create a pythonic type hint for a pd.Dataframe

```python
import pandas as pd
from pydantic import BaseModel

from typing import TypeVar

PandasDataFrame = TypeVar('pandas.core.frame.DataFrame')


class SubModelInput(BaseModel):
    a: PandasDataFrame
    b: PandasDataFrame
```

## See also

[Pandas DataFrame Validation with Pydantic](
https://www.inwt-statistics.com/read-blog/pandas-dataframe-validation-with-pydantic.html)

Hints from: [python - Using Pandas Data Frame as a Type in Pydantic - Stack Overflow](https://stackoverflow.com/questions/65412984/using-pandas-data-frame-as-a-type-in-pydantic)
