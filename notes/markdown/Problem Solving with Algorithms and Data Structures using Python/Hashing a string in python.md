Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.5.1
Date: 2021-11-02

---
# Hashing a string in python
In order to perform a hash function on a string, we mush first convert the string to numerical values. This is easy to do in python by using the `ord()` function on each character of the string, which returns the integer representation of the unicode character provided to it as an argument.

We can implement the [[Folding method hash function]] in python in the following way:

```python
def fold_hash(a_string, num_slots):
	sum = 0
	for ch in a_string:
		sum += ord(ch)
	
	return sum % num_slots
```

The `fold_hash` function takes two arguments – the string to hash, and the total number of slots, i.e the size of the [[What is a hash table?|hash table]]. It then sums the integer value of each unicode character in the string, and returns the modulus of the sum modulo the number of slots which is the resulting hash.

A drawback of this implementation is that anagrams will always hash to the same value. This can be fixed by applying a positional weighting for each character in the string.

```python
def fold_hash_weighted(a_string, num_slots):
	sum = 0
	for weight, ch in enumerate(a_string, start=1):
		sum += ord(ch) * weight
	
	return sum % num_slots
```

In this slightly more complex implementation, we use `enumerate` to loop through a pairing of each character in the string and its positional value, starting from 1 and incrementing with each loop. We use this positional value as a weight value to multiply the result of `ord(ch)` by its position in the string, ensuring that anagrams result in differing values of `sum` and thus they don't map to the same hash.