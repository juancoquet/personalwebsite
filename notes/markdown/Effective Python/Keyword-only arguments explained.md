Note type: #litnote
Source: [[📖 Effective Python]] item 25

---
# Keyword-only arguments explained
Keyword-only arguments are arguments that can only be passed in by keyword, not by position. To employ keyword-only arguments within a function definition, you can use the `*` symbol to indicate the end of the positional arguments and the beginning of keyword-only arguments.
```python
def my_function(first, last, *, middle=None):
	if middle:
		print(f'{first} {middle} {last}')
	else:
		print(f'{first} {last})
```