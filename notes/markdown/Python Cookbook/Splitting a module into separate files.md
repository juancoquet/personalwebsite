Note type: #litnote
Source: [[📖 Python Cookbook]] ch10.4 p401

---
# Splitting a module into separate files
It is possible to split a module into separate files if it gets too bloated, and still import its separated components from a single namespace to avoid breaking existing `import` statements. This is also a good way of organising code.

Assume you have the following module that you wish to split into separate files:
```python
# mymodule.py
class A:
	def foo(self):
		print('A.foo')


class B(A):
	def bar(self):
		print('B.bar')
```

To split this module, first create a package with the same name as the current module and create a new file inside this package to contain the separated elements. Here is the tree structure:
```
mymodule/
	__init__.py
	a.py
	b.py
```

The contained files are populated as follows:
```python
# a.py

class A:
	def foo(self):
		print('A.foo')
```

```python
# b.py

from .a import A


class B(A):
	def bar(self):
		print('B.bar')
```

With the code now split up into separate files, it can all be stitched together into one namespace (the name of the containing module `mymodule`) within the package's `__init__.py` file:
```python
# __init__.py

from .a import A
from .b import B
```

A separate module can now import both `A` and `B` from `mymodule` without any need for special syntax:
```python
# other module elsewhere

import mymodule

a = mymodule.A()		# Works
b = mymodule.B()		# Works
```