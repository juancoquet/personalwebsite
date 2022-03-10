Note type: #litnote
Source: [[📖 Effective Python]] item 36

---
# `itertools.product`
This function returns the Cartesian product of multiple iterators:
```python
output = itertools.product([1, 2], ['a', 'b'])
print(list(output))

>>>
[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```