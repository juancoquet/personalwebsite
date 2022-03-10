Note type: #litnote
Source: [[📖 Effective Python]] item 11

---
# Negative indexing slices
Negative slicing can be used to make selections relative to the *end* of a list:
```python
my_list = [1, 2, 3, 4]
sliced = my_list[:-1]

print(my_list)
print(sliced)

>>>
[1, 2, 3, 4]
[1, 2, 3]
```

```python
my_list = [1, 2, 3, 4]
sliced = my_list[-2:]

print(my_list)
print(sliced)

>>>
[1, 2, 3, 4]
[3, 4]
```

---
#### See also:
- [[Slicing from and to list boundaries]]
- [[List slicing syntax]]