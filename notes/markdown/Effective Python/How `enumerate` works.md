Note type: #litnote
Source: [[📖 Effective Python]] item 7

---
# How `enumerate` works
`enumerate` pairs each item in an iterable with an index number and yields them together in a tuple.
```python
my_iter = ('Juan', 'Coquet')
numbered = enumerate(my_iter)

print(next(numbered))
print(next(numbered))

>>>
(0, 'Juan')
(1, 'Coquet')
```