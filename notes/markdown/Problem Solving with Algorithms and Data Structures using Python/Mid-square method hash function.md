Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.5.1
Date: 2021-11-02

---
# Mid-square method hash function
The mid-square method has two steps. First, square the input data, then perform the modulo step on the middle digit(s) of the square. For example, if we want to hash the number 31 using the mid-square method for a [[What is a hash table?|hash table]] with 11 slots, we go through the following steps:
$$31^2 = 961$$
$$middle\_num(961) = 6$$
$$6 \bmod 11 = 6$$
$$h(31) = 6$$
A larger input item of 92 looks like this:
$$92^2 = 8464$$
$$middle\_num(8464) = 46$$
$$46 \bmod 11 = 2$$
$$h(92) = 2$$

---
### See also:
- [[Folding method hash function]]