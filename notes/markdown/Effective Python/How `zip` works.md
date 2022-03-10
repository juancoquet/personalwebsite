Note type: #litnote
Source: [[📖 Effective Python]] item 8

---
# How `zip` works
The `zip` function takes two or more iterables as arguments and yields tuples containing the next item from each iterable.
```python
president = ('Obama', 'Trump')
term_beginning = (2012, 2016)

for name, year in zip(president, term_beginning):
	print(name, year)
	
>>>
Obama 2012
Trump 2016
```

`zip` will keep yielding tuples until any of the involved iterables have been exhausted, meaning it's output will be limited to the length of its shortest input.