Note type: #litnote
Source: [[📖 Python Cookbook]] ch5.5 p148

---
# Prevent accidentally overwriting files
The `open()` function has a little-known `x` mode for opening files. When opening a file with this mode, it will raise an error if a file of the supplied name already exists, thereby preventing the accidental overwriting of said file.
```python

with open('myfile.txt', 'x') as f:
	f.write('Brand new file, this will succeed!')
	
with open('myfile.txt' 'x') as f:
	f.write('File already exists, this will fail')
```

When the file already exists, the function will raise a `FileExistsError`.