Note type: #litnote
Source: [[📖 Effective Python]] item 14

---
# Tuples are sorted left to right
When tuples are being compared for sorting, they are sorted by comparing items in order of index value—from left to right.
```python
me = (1995, 'juan')			# year then name
pupi = (1991, 'victoria')	# year then name

both = [me, pupi]

year_order = both.sort()

print(year_order)	# smallest year first (1991)

>>>
[(1991, 'victoria'), (1995, 'juan')]
```
```python
me = ('juan', 1995)			# name then year
pupi = ('vicotira, 1991')	# name then year

both = [me, pupi]

year_order = both.sort()

print(year_order)	# 'smallest' name first ('juan')

>>>
[('juan', 1995), ('victoria', 1991)]
```

In the top example, the `sort` function looks at the year first as it's at the first index position of the tuple, and compares to find the smallest value. 1991 < 1995, so the `pupi` object is sorted before the `me` object.

In the second example, the `sort` function looks at the name first as it's at the first index position of the tuple, and compares to find the smallest value. 'juan' is alphabetically lesser than 'victoria', so the `me` object is sorted before the `pupi` object.