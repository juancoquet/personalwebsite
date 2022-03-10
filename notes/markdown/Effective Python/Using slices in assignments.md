Note type: #litnote
Source: [[📖 Effective Python]] item 11

---
# Using slices in assignments
Values can be assigned to a slice with the assignment operator `=`. A copy is not created in this case; the original list is changed in place.
```python
my_list = [1, 2, 3, 4, 5, 6]
my_list[2:4] = ['a', 'b']

print(my_list)

>>>
[1, 2, 'a', 'b', 5, 6]
```

Unlike in multiple assignment unpacking, both sides of the `=` assignment operator do not need to be the same length—the list will grow or shrink to adapt to the length of the new values.
```python
my_list = [1, 2, 3, 4, 5, 6]
my_list[2:5] = ['a', 'b']	# list shrinks

print(my_list)

>>>
[1, 2, a, b, 6]
```

```python
my_list = [1, 2, 3, 4, 5, 6]
my_list[2:3] = ['a', 'b']	# list grows

print(my_list)

>>>
[1, 2, 'a', 'b', 4, 5 6]
```

---
#### See also:
- [[Multiple assignment unpacking explained]]
- [[List slicing syntax]]