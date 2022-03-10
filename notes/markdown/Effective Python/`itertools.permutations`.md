Note type: #litnote
Source: [[📖 Effective Python]] item 36

---
# `itertools.permutations`
This function returns all the unique ordered permutations of the length prescribed by the second parameter:
```python
it = itertools.permutations([1, 2, 3, 4], 2)
print(list(it))

>>>
[(1, 2),
 (1, 3),
 (1, 4),
 (2, 1),
 (2, 3),
 (2, 4),
 (3, 1),
 (3, 2),
 (3, 4),
 (4, 1),
 (4, 2),
 (4, 3)]
```