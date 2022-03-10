Note type: #litnote
Source: [[📖 Python Cookbook]] ch5.13 p158

---
# List all files and directories
```python

import os

names = os.listdir('somedir')
```

The above code will list all files and sub-directories inside `somedir`. Consider combining this with comprehensions to get the name of particular files or directories.
```python

files = [file for file in os.listdir('somedir') if os.path.isfile(os.path.join('somedir', file))]

dirs = [dir for dir in os.listdir('somedir') if os.path.isdir(os.path.join('somedir', dir))]

py_files = [file for file in os.listdir('somedir') if file.endswith('.py')]
```