Note type: #litnote
Source: [[📖 Effective Python]] item 8

---
# Using `zip` instead of indexing to handle multiple iterables
When looping through iterables of related items it is much cleaner to use `zip` than to use `range` and index into each iterable.
```python
president = ('Obama', 'Trump')
term_beginning = (2012, 2016)

for name, year in zip(president, term_beginning):
	print(name, year)
	
>>>
Obama 2012
Trump 2016
```

The above code is much less visually noisy and more readable than achieving the same thing through using `range` and indexing.
```python
truncated...

for i in range(len(president)):
	name = president[i]
	year = term_beginning[i]
	print(name, year)

>>>
Obama 2012
Trump 2016
```

---
#### See also:
- [[How `zip` works]]
- [[Use multiple assignment unpacking to unpack iterables in loops]]