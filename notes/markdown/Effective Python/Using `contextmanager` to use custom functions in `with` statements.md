Note type: #litnote
Source: [[📖 Effective Python]] order 66

---
# Using `contextmanager` to use custom functions in `with` statements
Any time that repeated use of `try/finally` clauses is needed, consider using the `contextmanager` decorator from the `contextlib` module. This decorator allows you to specify the setup behaviour that will be executed when the `with` statement is declared (the `try` block) and the tear-down behaviour that will be executed when the `with` block ends.
```python
import os
from contextlib import contextmanager

def change_directory(destination):
	try:
		original_dir = os.getcwd()
		os.chdir(destination)
		yield
	finally:
		os.chdir(original_dir)

with change_directory('my_dir_1'):
	# do some stuff

```

The above function can now be used to jump in and out of different directories without needing to remember to change back to the original directory. Not only is this cleaner to read, but it is also safer as it ensures that resources are properly managed and nothing is left open after it is no longer needed for processing within the code, as it will automatically be closed by the `finally` block at the time that the `with` block ends.

---
#### See also:
- [[Generator expressions explained]]