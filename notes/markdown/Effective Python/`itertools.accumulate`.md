Note type: #litnote
Source: [[📖 Effective Python]] item 36

---
# `itertools.accumulate`
This function can return running totals:
```python
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
running_totals = itertools.accumulate(values)

print(list(running_totals))

>>>
[1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
```