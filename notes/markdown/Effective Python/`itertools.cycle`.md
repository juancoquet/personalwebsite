Note type: #litnote
Source: [[📖 Effective Python]] item 36

---
# `itertools.cycle`
Use this function to repeat an iterator's items forever:
```python
it = itertools.cycle([1, 2])
result = [next(it) for _ in range(10)]
print(result)

>>>
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
```