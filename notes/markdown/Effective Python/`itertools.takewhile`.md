Note type: #litnote
Source: [[📖 Effective Python]] item 36

---
# `itertools.takewhile`
This function takes a function and an iterator as arguments, and returns items from the iterator until the function evaluated to `False`:
```python
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7

it = itertools.takewhile(less_than_seven, values)
print(list(it))

>>>
[1, 2, 3, 4, 5, 6]
```