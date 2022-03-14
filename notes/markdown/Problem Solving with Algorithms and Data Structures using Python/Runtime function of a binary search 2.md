Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.4.1
Date: 2021-11-01

---
# Runtime function of a binary search
The worst case scenario for a binary search is when the item is not in the collection, or when it is in the collection but it is found during the final comparison – when the length of the collection has been whittled down to 1 through iterative halving.

If we were to count the number of iterations required to half a collection of length $n$ until the length of $n$ equals 1, we can describe this process with the following equation where $i$ represents the number of iterations:

$$\frac{n}{2^i} = 1$$

We can solve for $i$ through the following steps to arrive at a result of $log_2n$:

1. Multiply by $2^i$: $$n = 2^i$$<br>

2. Calculate the base-2 $log$ function:$$log_2n = i$$<br>

When considering asymptotic runtime functions, constants, coefficients and divisors are ignored as they become less significant as $n$ grows. This leaves us with a final result of $log\:n$ iterations – in the worst case scenario, a binary search has a runtime function of $O(log\:n)$.

---
### See also:
- [[What is a binary search?]]
- [[Implementation of a binary search algorithm in python]]