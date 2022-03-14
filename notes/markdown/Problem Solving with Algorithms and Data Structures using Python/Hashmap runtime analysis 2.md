Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.5.4
Date: 2021-11-03

---
# Hashmap runtime analysis
In a perfect world where no slot collisions occur, the runtime function of searching our hashmap would be $O(1)$, as each hashed key value would direct us straight to the correct slot. However, as collisions increase, the efficiency of searching a hash map decreases as one or more rehashing steps need to occur.

The key piece of information to consider is the [[What is a hash table?|hash table]]'s load factor, $\lambda$.
<br>
$$\lambda = \frac{filled\:slots}{total\:slots}$$
<br>

When $\lambda$ is large, collisions increase and extra steps must be taken to resolve these collisions. If we are using a chaining method of resolving collisions then there are more items to search at each slot.

An average successful search would require at most the number of look-ups calculated by:

<br>
$$\frac{1}{1-\lambda}$$
<br>

Assume we have a load factor of $\lambda=0.5$, meaning that half of our slots are filled, then the above formula evaluates to 2. In this instance, there is a 50% chance that a new hash will result in a collision. If no collision occurs, our runtime is 1.

If a collision occurs, given that 50% of the table is filled, on average we don't expect the next slot we check to also be filled. It's certainly very possible, but in the average case we would expect to execute at most two look-ups.

---
### See also:
- [[Resolving hash collisions]]
- [[What is a map data type?]]