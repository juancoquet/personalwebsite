Note type: #litnote
Source: [[📖 Python Cookbook]] ch10.3 p399

---
# Using relative imports
Rather than hardcoding a directory structure into your import statements which can make your code brittle if the structure changes, it is better to use import statements using `.`.

Assume we have the following tree structure:
```
project/
	__init__.py
	main.py
	A/
		__init__.py
		foo.py
	B/
		__init__.py
		bar.py
		spam.py
```

The `spam.py` module could import from the modules surrounding it by using the following code.
```python
# project/B/spam.py

from . import bar
```

The dot is used to import from the same package (directory) that the current module exists in. To import from a package that exists on the same level as the current containing package, `..` can be used.
```python
# project/B/spam.py

from ..A import foo
```

The above code looks inside the `A` package for the `foo.py` module.

Relative import behaviour will only work when importing from proper python packages—directories inside which `__init__.py` has been declared. No code needs to be present inside `__init__.py`, it just has to exist inside the directory to establish it as a python package.