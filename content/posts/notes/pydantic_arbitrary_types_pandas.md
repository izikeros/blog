---
title: Alow arbitrary types (such as Pandas Dataframe) in Pydantic
date: 2022-04-21
status: published
tags: pydantic, pandas, type hints
summary: 
slug: allow-arbitrary-types-pandasa-in-pydantic
category: note
citation_needed: false
todo: 
---

```toc
```



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


Hints from: [stackoverflow](https://stackoverflow.com/questions/65412984/using-pandas-data-frame-as-a-type-in-pydantic)
