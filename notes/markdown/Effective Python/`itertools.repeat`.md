Note type: #litnote
Source: [[📖 Effective Python]] item 36

---
# `itertools.repeat`
Use this function to repeat a given value forever, or provide a second argument to state a maximum number of repetitions:
```python
it = itertools.repeat('hello', 3)
print(list(it))

>>>
['hello', 'hello', 'hello']
```