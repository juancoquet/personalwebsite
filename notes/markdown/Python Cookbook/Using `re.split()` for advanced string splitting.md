Note type: #litnote
Source: [[📖 Python Cookbook]] ch2.1 p37

---
# Using `re.split()` for advanced string splitting
The built in `split()` string method is good only for simple use cases. It can only split by one delimiter. Should you need to split by more than one type of delimiter, use `re.split()`
```python

import re

s = 'asdf fjdk; afed, fjek,asdf,    foo'
text = re.split(r'[;,/s]\s*', s)
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
```

`re.split()` uses a regular expression to match multiple delimiters. In this case, it looks for a semi-colon, a comma, or a space, followed by any number of spaces.

Note that when grouping regular expression search terms with parentheses, the delimiters will also be included in the return value as part of the output list.
```python

all = re.split(r'(;|,|\s)\s*', s)
#  ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
```

This behaviour could be useful in some cases, for example if you later need to reform the original string but without any white space. If you need to group an expression but don't want the delimiters returned, precede the group of search terms with `(?:...)` to specify that it is a non-capture group.