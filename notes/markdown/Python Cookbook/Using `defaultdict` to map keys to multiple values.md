Note type: #litnote
Source: [[📖 Python Cookbook]] ch1.7 p12

---
# Using `defaultdict` to map keys to multiple values
Manually mapping a key to multiple values seems trivial, but it can make for clunky, error-prone code—you have to define the key, assign a list/set to it, and then append or add values to that container.

Using `defaultdict` dict simplifies this process and makes for terser code.
```python
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
```

Default dict will automatically create a new empty list (or any provided callable) for each new key that is indexed, so the programmer doesn't have to.

---
### See also:
- [[`defaultdict` automatically sets a default value to missing keys]]