Note type: #litnote
Source: [[📖 Effective Python]] item 12

---
# Simplifying striding and slicing for readability
Striding and slicing in the same expression can become very confusing because of the density of the expression. It isn't always obvious how the start and end values interact with the slicing value, especially when using negative indexes and slicing values.
```python
my_list = [1, 2, 3, 4, 5, 6]

my_list[2::2]		# [2, 4, 6]
my_list[-2::-2]		# [5, 3, 1]
my_list[-2:2:-2]	# [5, 3]
my_list[2:2:-2]		# []
```

The examples above can be a little too dense to decipher. Instead of utilising such a dense expression, consider separating the slicing step and the striding step into two separate, simpler expressions:
```python
my_list = [1, 2, 3, 4, 5, 6]

stride = my_list[::-2]	# [6, 4, 2]
slice = stride[1:]		#[4, 2]
```

---
#### See also:
- [[Striding syntax explained]]