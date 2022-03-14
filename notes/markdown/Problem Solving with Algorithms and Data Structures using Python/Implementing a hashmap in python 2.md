Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.5.3
Date: 2021-11-03

---
# Implementing a hashmap in python
We can use a combination of python's `list` type and hashing utility methods to implement a hashmap class.

```python
class HashTable:

	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def _hash_function(self, key):
		return key % self.size

	def _rehash(self, old_hash):
		return (old_hash + 1) % self.size

	def put(self, key, data):
		hash_val = self.hash_function(key)
		if self.slots[hash_val] is None:
			self.slots[hash_val] = key
			self.data[hash_val] = data
		elif self.slots[hash_val] == key:
			self.data[hash_val] = data
		else:
			while self.slots[hash_val] is not None and self.slots[hash_val] != key:
			hash_val = self.rehash(hash_val) # infinite loop if table is full
			if self.slots[hash_val] is None:
				self.slots[hash_val] = key
				self.data[hash_val] = data

	def get(self, key):
		start_slot = self.hash_function(key)
		hash_val = self.hash_function(key)
		while self.slots[hash_val] is not None and self.slots[hash_val] != key:
			hash_val = self.rehash(hash_val)
			if hash_val == start_slot:
				return None
		return self.data[hash_val]
```

- `__init__` defines a size for the [[What is a hash table?|hash table]] and instantiates two lists – one for the hash slots, and one for the corresponding data. It sets all the values to `None` initially. Notice that it sets the size of the table to 11 slots, a prime number so that all slots will eventually be checked in the event of rehashing.
- `_hash_function` an internal method to hash keys. This hash function uses the simple remainder method, but any type of hash function can be used to suit the needs of the data.
- `_rehash` an internal method to create another hash if a slot collision occurs. This implementation uses linear probing, but any rehashing method can be applied.
- `put` adds a new key/value pair to the hashmap, or replaces the existing data if the key is already a member of the hashmap. This method calls the `_rehash` method to resolve collisions if they occur. This is a simplistic implementation that assumes an empty slot will eventually be found, so it results in an infinite loop if all slots are populated.
- `get` retrieves the data associated with an existing key, or `None` if the key is not found. It remembers the first slot checked (the initial hash value) inside `start_slot` so that the subsequent `while` loop can detect when the rehashing function has come full circle, meaning that the key was not found in the hashmap. The `while` loop checks that the current hash value is not `None`, or the key being looked up. If `None` is found, it means that the key does not exist. If the key is found, its data pair can be returned. Inside the loop we rehash and check that the new hash is not the slot we started on.

This implementation is missing the `del`, `len` and `in` operations which are easy enough to write. The hashing function also assumes that all keys will be `int` or `float` types.

---
### See also:
- [[What is a map data type?]]
- [[Operations of a map datatype]]
- [[Resolving hash collisions]]