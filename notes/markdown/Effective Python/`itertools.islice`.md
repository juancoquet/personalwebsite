Note type: #litnote
Source: [[📖 Effective Python]] item 36

---
# `itertools.islice`
Use this function to slice an iterable in place—without creating a copy. You can provide start, end and stride values (in that order):
```python
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_five = itertools.islice(values, 5)
print('First five: ', list(first_five))

middle_odds = itertools.islice(values, 2, 8, 2)
print('Middle odds: ', list(middle_odds))

>>>
First five: [1, 2, 3, 4, 5]
Middle odds: [3, 5, 7]
```