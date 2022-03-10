Note type: #litnote
Source: [[📖 Effective Python]] item 11

---
# Slicing from and to list boundaries
When slicing from the beginning of a list, there is no need to include the 0 in the slicing index:
```python
my_list = [1, 2, 3, 4]
sliced = my_list[:3]	# instead of [0:3]

print(my_list)
print(sliced)

>>>
[1, 2, 3, 4]
[1, 2, 3]
```

The opposite applies for slicing to the end of a list:
```python
my_list = [1, 2, 3, 4]
sliced = my_list[2:]

print(my_list)
print(sliced)

>>>
[1, 2, 3, 4]
[3, 4]
```

Slicing beyond the boundaries of a list will simply slice to the end of the list; no exceptions will be raised.
```python
my_list = [1, 2, 3, 4]
sliced = my_list[1:20]

print(my_list)
print(sliced)

>>>
[1, 2, 3, 4]
[2, 3, 4]
```
---
#### See also:
- [[List slicing syntax]]