Note type: #litnote
Source: [[📖 Effective Python]] item 8

---
# Use `zip_longest` as an alternative when necessary
`zip_longest` can be imported from the `itertools` built-in module. It will keep yielding tuples for the length of the longest iterable involved within the function, yielding `None` where blanks are found.
```python
name = ('Donald', 'Joe', 'Obama')
surname = ('Trump', 'Biden')

for first, last in zip(name, surname):
	print(first, last)

>>>
Donald Trump
Joe Biden
Obama None
```

---
#### See also:
- [[How `zip` works]]