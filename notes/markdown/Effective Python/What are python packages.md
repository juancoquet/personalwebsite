Note type: #litnote
Source: [[📖 Effective Python]] item 85

---
# What are python packages
Python packages are modules that contain other modules. A module is a file consisting of python code. The way to define a package is to insert an empty file named `__init__.py` into a directory. Once this file is present, other python files within that directory (and within any nested directories) will be available for import using a path relative to that directory.