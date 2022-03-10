Note type: #litnote
Source: [[📖 Effective Python]] item 36

---
# `itertools.chain`
This function can be used to combine multiple iterators into one sequential iterator:
```python
it = itertools.chain([1, 2, 3], [4, 5, 6])
print(list(it))

>>>
[1, 2, 3, 4, 5, 6]
```