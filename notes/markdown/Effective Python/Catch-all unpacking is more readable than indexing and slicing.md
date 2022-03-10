Note type: #litnote
Source: [[📖 Effective Python]] item 13

---
# Catch-all unpacking is more readable than indexing and slicing
Unpacking the items of an iterator into multiple variables can easily be done by indexing and slicing the iterator:
```python
my_list = [1, 2, 3, 4, 5, 6]
first = my_list[0]
second = my list[1]
others = my_list[2:]

print(first)
print(second)
print(others)

>>>
1
2
[3, 4, 5, 6]
```

However, this is visually noisy and takes multiple lines. A cleaner, more readable way of achieving the same thing is through the use of catch-all unpacking:
```python
my_list = [1, 2, 3, 4, 5, 6]

first, second, *others = my_list

print(first)
print(second)
print(others)

>>>
1
2
[3, 4, 5, 6]
```

This also means that unpacking variables can be added and removed without having to worry about updating slicing indexes of all other unpacking variables:
```python
my_list = [1, 2, 3, 4, 5, 6]

first, second,  third, *others = my_list

print(first)
print(second)
print(third)
print(others)

>>>
1
2
3
[4, 5, 6]
```

Above, when the variable `third` is added, `*others` is automatically filled with all remaining values after `first`, `second` and `third` have been filled. This would have to be done manually with a slicing approach, which can be very error-prone and time consuming.

---
#### See also:
- [[Catch-all unpacking syntax explained]]