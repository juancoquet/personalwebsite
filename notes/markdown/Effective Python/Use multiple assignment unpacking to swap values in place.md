Note type: #litnote
Source: [[📖 Effective Python]] item 6

---
# Use multiple assignment unpacking to swap values in place
Python's multiple assignment unpacking allows you to swap values in place without the need to involve a temporary variable, like in other languages.
```python
dog_breed_1 = 'labrador'
dog_breed_2 = 'pug'

dog_breed_1, dog_breed_2 = dog_breed_2, dog_breed_1		# swap

print(dog_breed_1, dog_breed_2)

>>>
pug labrador
```

This works because python evaluates the right side of the assignment first (everything to the right of the `=` assignment operator) and stores those values in a temporary tuple. It then unpacks this tuple into the variables on the left side of the assignment operator. The temporary tuple is then automatically deleted, meaning that the programmer doesn't need to manually create a temporary variable which would clutter the code.

---
See also:
- [[Multiple assignment unpacking explained]]