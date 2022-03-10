Note type: #litnote
Source: [[📖 Effective Python]] item 22

---
# Using `*args` to accept a variable number of positional arguments
Sometimes, accepting a variable number of positional arguments can make for  clearer code. This can be done with the `*args` syntax—any starred variable defined in the function definition will accept a variable number of arguments (including 0), much like multiple assignment unpacking.
```python
def my_function(person, *pets):
	if not pets:
		print(f'{person} has no pets)
	else:
		pets_str = ','.join(pet for pet in pets)
		print(f'{person} has: {pets_str})

my_function('hristo')
my_function('victoria', 'salem', 'ziggy')

>>>
hristo has no pets
victoria has: salem, ziggy
```

This works because python packs all values after the `*args` into a tuple that the function can then use and process.

Be careful when introducing new positional arguments to the function definition, as this will subtly break existing callers of the function causing hard-to-detect bugs. In the example above if we were to add a new variable at the start, 'victoria' would be assigned to the new variable while 'salem' would be assigned to the `person` variable with all remaining values being assigned to `*pets`. This would not raise any errors, hence the subtlety.

---
#### See also:
- [[Multiple assignment unpacking explained]]