Note type: #litnote
Source: [[📖 Effective Python]] item 11

---
# Slicing a copy of a list
You can use slicing to create a full copy of a list, simply by including all the list items in the slice by using `[:]` as your slicing index.
```python
my_list = [1, 2, 3, 4]
slice_copy = my_list[:]	# includes all list indexes

print(my_list)
print(slice_copy)

>>>
[1, 2, 3, 4]
[1, 2, 3, 4]
```

---
#### See also:
- [[Slicing from and to list boundaries]]
- [[List slicing syntax]]