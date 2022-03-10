Note type: #litnote
Source: [[📖 Effective Python]] item 25

---
# Positional-only arguments explained
Positional-only arguments can be passed in only by position, not by keyword. You can employ these in function definitions by using the `/` symbol to indicate when positional-only arguments *end*.
```python
def my_function(first, last, /, middle=None):
	if middle:
		print(f'{first} {middle} {last})
	else:
		print(f'{first} {last}')
```

When calling the above functions, any attempt to provide the `first` or `last` arguments by keyword will raise an exception.

---
#### See also:
- [[Keyword-only arguments explained]]