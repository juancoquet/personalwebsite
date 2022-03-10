Note type: #litnote
Source: [[📖 Effective Python]] item 12

---
# Negative stride values
Negative stride values can be used to stride through a list in reverse order:
```python
my_list = [1, 2, 3, 4, 5, 6]
stride_list = my_list[::-1]

print(stride_list)

>>>
[6, 5, 4, 3, 2, 1]
```

This can also be combined with specific start and end slice values:
```python
my_list = [1, 2, 3, 4, 5, 6]
stride_list = my_list[-2::-2]	# start at -2 and copy every 2nd item

print(stride_list)

>>>
[5, 3, 1]
```

---
#### See also:
- [[Striding syntax explained]]