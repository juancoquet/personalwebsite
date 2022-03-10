Note type: #litnote
Source: [[📖 Effective Python]] item 11

---
# Slices do not modify the original list
When a slice is created, the original `list` object is preserved and a new `list` object is created.
```python
my_list = [1, 2, 3, 4]
sliced = my_list[1:20]

print(my_list)	# unchanged
print(sliced)	# new list object

>>>
[1, 2, 3, 4]
[2, 3, 4]
```