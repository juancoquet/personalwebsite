---
aliases: [hash table, hash tables, hash map, hash maps]
Date: 2021-11-02
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.5

---
# What is a hash table?
A hash table is a kind of container where a collection of items can be stored in such a way to make them easier to find later. Each position in a hash table, also known as a **slot**, can hold an item and corresponds to an integer index value (also knows as a **hash value** or simply a **hash**) starting at 0.

Items are mapped to a position in the hash table using a **hash function**. A hash function takes an item in the collection and returns an integer within the range 0 and $s-1$ where $s$ is the number of slots in the hash table. It is a series of arbitrary steps that can be followed to map input data of arbitrary size $n$ to a fixed number of slot positions $s$.

A simple example hash function is a *remainder* function. A remainder hash function ($h$) takes the value of an item and divides it by the table size $s$ (the number of slots), then returns the remainder of the calculation. We call this a modulo operation.

$$h(item) = item\bmod{s}$$

Suppose we have a collection of integers 54, 26, 93, 17, 77, 31 and a hash table of 11 slots ($s=11$), with corresponding hashes 0-10. The following table shows how the input values are mapped to a hash using the remainder hash function:

| Item | Hash function (python) | Hash value |
| ---- | ---------------------- | ---------- |
| 54   | `h = 54 % 11`          | 10         |
| 26   | `h = 26 % 11`          | 4          |
| 93   | `h = 93 % 11`          | 5          |
| 17   | `h = 17 % 11`          | 6          |
| 77   | `h = 77 % 11`          | 0          |
| 31   | `h = 31 % 11`          | 9          |

Since all hash values must be within the range of 0 and $s-1$ to correspond to a slot position within the hash table, all hash functions will perform this modulo operation in one way or another.

With the hash calculated for an item, it can now be placed into the table in the corresponding slot. Empty slots simply hold the value `None`. The proportion of slots that are filled in a hash table is referred to as the **load factor**, represented by $\lambda$ in the equation:

$$\lambda = \frac{filled\:slots}{total\:slots}$$

In our case:

$$\lambda = \frac{6}{11}$$

To search for an item in the hash table, we simply call the hash function on the item and look up the corresponding slot returned to see if the item is present. This means that a hash table search has a runtime function of $O(1)$ as a constant amount of time is required to look up the item regardless of the input value.

This simple example of a hash function does not take **collisions** into account. A collision occurs when two items are mapped to the same hash. For example, the number 44 would map to a hash of 0, which is already occupied by the item 77 from our data collection. Hash functions with extra steps can be applied to minimise the number of collisions that occur.

---
### See also:
- [[Folding method hash function]]
- [[Mid-square method hash function]]