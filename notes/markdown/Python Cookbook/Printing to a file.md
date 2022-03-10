Note type: #litnote
Source: [[📖 Python Cookbook]] ch5.2 p144

---
# Printing to a file
You can print to a file instead of the console by specifying a `file` argument for the `print` function.
```python

with open('printfile.txt', 'w') as f:
	print("Hello, World!", file=f)
```