Note type: #litnote
Source: [[📖 Effective Python]] item 85

---
# Making a public API
To make a public API, you must import any names that you wish to make public into the `__init__.py` module in the package that will be released, and add each name to the `__all__` attribute.
```python
# __init__.py
__all__ = []
from my_package import *

__all__ += my_package.__all__
```

---
#### See also:
- [[Using `__all__` to provide stable APIs]]
- [[Importing python packages]]