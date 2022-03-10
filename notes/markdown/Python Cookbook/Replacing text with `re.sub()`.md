Note type: #litnote
Source: [[📖 Python Cookbook]] ch2.11 p54

---
# Replacing text with `re.sub()`
There are some cases where the `sub()` function from the `re` library is more useful than the `.replace()` string method. For example, say you need to replace repeated blank space in the middle of a string.
```python
import re

s = 'hello      world'
replaced = re.sub('\s+', ' ', s)	# replace multiple spaces with 1
# 'hello world'
```