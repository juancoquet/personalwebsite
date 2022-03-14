Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.5.1
Date: 2021-11-02

---
# Folding method hash function
A folding method hash function first separates the data for the item being hashed into smaller chunks. For example, if we were hashing a phone number 123-456-7890, we could break this number down into five pairs – 12, 34, 56, 78, 90.

The sum of these smaller chunks is then calculated, and the modulus of the result (using the total number of slots in the [[What is a hash table?|hash table]] as the divisor) is the hash value. Assuming we have a hash table with 11 slots, we get the following:
$$12+34+56+78+90 = 270$$
$$270 \bmod11 = 6$$
The abstraction of hash function $h$ on our phone number looks like this:
$$h(1234567890) = 6$$
Some folding methods go one step further by reversing the order of alternate data chunks, which would give the following result:
$$12+43+56+87+90 = 288$$
$$288 \bmod11 = 2$$
$$h2(1234567890) = 2$$
