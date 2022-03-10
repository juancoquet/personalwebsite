Note type: #litnote
Source: [[📖 Effective Python]] item 7

---
# `enumerate` yielded pairs can be unpacked in a `for` statement
When working with `enumerate` and within `for` loops, the yielded values can be unpacked within the `for` statement itself:
```python
my_iter = ('Juan', 'Coquet')

for i, item in enumerate(my_iter):
	print(i, item)

>>>
0 Juan
1 Coquet
```

This makes for much cleaner code than having to use `range`, `len` and indexing into the iterable in order to get indexed pairs:
```python
truncated...

for i in range(len(my_iter)):
	print(i, my_iter[i])

>>>
0 Juan
1 Coquet
```

---
#### See also:
- [[Use multiple assignment unpacking to unpack iterables in loops]]