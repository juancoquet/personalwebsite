Note type: #litnote
Source: [[📖 Effective Python]] item 36

---
# `itertools.combinations_with_replacement`
This function is the same as [[`itertools.combinations`]], but items from the iterator are also combined with themselves:
```python
it = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
print(list(it))

>>>
[(1, 1),
 (1, 2),
 (1, 3),
 (1, 4),
 (2, 2),
 (2, 3),
 (2, 4),
 (3, 3),
 (3, 4),
 (4, 4)]
```

---
#### See also:
- [[`itertools.combinations`]]