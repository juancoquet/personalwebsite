Note type: #litnote
Source: [[📖 Effective Python]] item 36

---
# `itertools.filterfalse`
This function executes a negative filter—it includes all results *outside* of the filter criteria:
```python
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = lambda x: x % 2 == 0
filter_false = itertools.filterfalse(evens, values)

print(list(filter_false))

>>>
[1, 3, 5, 7, 9]
```