Note type: #litnote
Source: [[📖 Python Cookbook]] ch13.8 p549

---
# Creating and unpacking archive files
The `shutil` module has the functions `make_archive()` and `unpack_archive()`.
```python
import shutil


shutil.unpack_archive('myfile.zip')		# Unarchive
shutil.make_archive('archived-name', 'zip', 'to-archive')
```

The first argument passed to `make_archive()` is the name of the file to be created. The second argument is the format of the file to be created (full list of supported formats can be found by running `shutil.get_archive_formats()`) and the third argument is the name of the directory to be archived.