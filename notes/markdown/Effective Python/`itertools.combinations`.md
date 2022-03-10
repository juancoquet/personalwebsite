Note type: #litnote
Source: [[📖 Effective Python]] item 36

---
# `itertools.combinations`
This function returns all unordered combinations of the items within an iterator of the length prescribed by the second input parameter:
```python
it = itertools.combinations([1, 2, 3, 4], 2)
print(list(it))

>>>
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```