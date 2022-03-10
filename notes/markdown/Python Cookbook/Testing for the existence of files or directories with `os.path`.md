Note type: #litnote
Source: [[📖 Python Cookbook]] ch5.12 p157

---
# Testing for the existence of files or directories with `os.path`
The `os` module has functions to test for the existence of files and directories which can be used as follows.
```python

import os


os.path.exists('/foo/bar')	# returns True or False

# Test what kind of file it is
os.path.isfile('/foo/bar')	# True or False
os.path.isdir('/foo/bar')	# True or False
```

You can also retrieve metadata about the file in question.
```python

import time


os.path.getsize('/foo/bar')		# Returns size in int

# Get last modified time as timestamp, convert to time object
time.ctime(os.path.getmtime('/foo/bar'))
# Sat Apr 24 21:04:34 2021
```