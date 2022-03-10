Note type: #litnote
Source: [[📖 Effective Python]] item 36

---
# `itertools.zip_longest`
This variation of the `zip` function zips according to the length of the longest iterator provided, filling missing values with a placeholder value that can be passed in to the `fillvalue` parameter:
```python
keys = ['one', 'two', 'three']
values = [1, 2]

normal = list(zip(keys, values))
print('normal zip: ', normal)

it = itertools.zip_longest(keys, values, fillvalue='nope')
longest = list(it)
print('zip_longest: ', longest)

>>>
normal zip: [('one', 1), ('two', 2)]
zip_longest: [('one', 1), ('two', 2), ('three', 'nope')]
```

---
#### See also:
- [[How `zip` works]]
- [[Use `zip_longest` as an alternative when necessary]]