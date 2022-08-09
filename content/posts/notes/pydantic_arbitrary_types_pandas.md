---
title: Allow arbitrary types (such as Pandas Dataframe) in Pydantic
date: 2022-04-21
status: published
tags: pydantic, pandas, type-hints
summary: 
slug: allow-arbitrary-types-pandas-in-pydantic
category: note
citation_needed: false
todo: 
---

<!-- MarkdownTOC levels='2,3' autolink=True autoanchor=True -->

- [Solution 1 - allow arbitrary types](#solution-1---allow-arbitrary-types)
- [Solution 2 - create a pythonic type hint for a pd.Dataframe](#solution-2---create-a-pythonic-type-hint-for-a-pddataframe)
- [See also](#see-also)

<!-- /MarkdownTOC -->


<a id="solution-1---allow-arbitrary-types"></a>
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

<a id="solution-2---create-a-pythonic-type-hint-for-a-pddataframe"></a>
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

<a id="see-also"></a>
## See also
[Pandas DataFrame Validation with Pydantic](
https://www.inwt-statistics.com/read-blog/pandas-dataframe-validation-with-pydantic.html)


Hints from: [python - Using Pandas Data Frame as a Type in Pydantic - Stack Overflow](https://stackoverflow.com/questions/65412984/using-pandas-data-frame-as-a-type-in-pydantic)

