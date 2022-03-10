Note type: #litnote
Source: [[📖 Effective Python]] item 11

---
# List slicing syntax
The syntax to use for list slicing is `my_list[start:end]`, where *start is inclusive* and *end is exclusive*.
```python
my_list = [1, 2, 3, 4]
sliced = my_list[1:3]

print(my_list)
print(sliced)

>>>
[1, 2, 3, 4]
[2, 3]
```