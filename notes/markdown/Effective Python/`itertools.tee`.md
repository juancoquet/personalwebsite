Note type: #litnote
Source: [[📖 Effective Python]] item 36

---
# `itertools.tee`
Use this function to split a single iterator into a number of parallel iterators specified by the second parameter value:
```python
it1, it2, it3 = itertools.tee(['first', 'second'], 3)
print(list(it1))
print(list(it2))
print(list(it3))

>>>
['first', 'second']
['first', 'second']
['first', 'second']
```