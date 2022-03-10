Note type: #litnote
Source: [[📖 Python Cookbook]] ch5.11 p156

---
# Manipulating path names with `os.path`
The `os` module has some helpful functions for working with path names.
```python

import os
my_path = '/Users/foo/Bar/bar.csv'

# Get the last componenet of path
os.path.basename(my_path)	# bar.csv

# Get the directory name
os.path.dirname(my_path)	# /Users/foo/Bar

# Join path componenets together
os.path.join('other', 'dir', os.path.basename(my_path))
# other/dir/bar.csv

# Expand the user's home directory
my_path = '~/Bar/bar.csv'
os.path.expanduser(my_path)	# '/Users/foo/Bar/bar.csv'

# Split the file extension
os.path.splittext(my_path)	# ('~/Bar/bar', '.csv')
```