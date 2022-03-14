Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.5.2
Date: 2021-11-02

---
# Resolving hash collisions
On occasions when two items hash to the same slot, we need to resolve the collision.

## Linear probing
A simple way of resolving a collision is to sequentially look for the next available slot in the [[What is a hash table?|hash table]] – if our item hashes to slot 4 but 4 is filled, we check slot 5. If 5 is filled, we check 6, and so on, until we find the next available slot. If we reach the end of the table but haven't yet checked some of the earlier slots (i.e. slots 1, 2, 3 in this example) the we circle back around to the beginning of the table.

This process of resolving collisions is referred to as **open addressing**, meaning that the hash function attempts to find an alternate slot for the item. By sequentially searching through each subsequent slot until an empty one is found, we are performing an open addressing technique called **linear probing**.

Once we have a hash table with open addressing and linear probing, our search method must match the hash function to get a reliable result. In other words, if we are looking for an item which hashes to 4 but we find another item in slot 4, we can't yet return `False` as a collision could have occurred at slot 4 earlier on. We must now do linear probing until either the item is found or an empty slot is found, then we can return `True` or `False` respectfully.

The problem with this approach is that it can easily lead to clustering of the collection's items in the hash table. If two items hash to 0, the second will be put into slot 1. Now any subsequent items which hashes to 0 *or* 1 will have to be put into slot 2, and so on.

We can deal with clustering by skipping slots in our linear probing. Rather than going to the next slot (a jump of 1), we can make a jump of 3. If we have a collision at slot 4, we will check slot 7, then 10, etc. This spaces out collisions more evenly. The process of finding another slot is called **rehashing**.  With linear probing, our rehashing function is $newhash = rehash(oldhashvalue)$, where $rehash(oldhashvalue) = (oldhashvalue + jumpsize) \bmod tablesize$.

The call to $\mod tablesize$ allows us to circle back around to the beginning of the table if we exceed the end.

The size of $jumpsize$ must be such that all slots are eventually checked, otherwise we'd leave part of the table unused. To ensure this, it is a good idea to make the size of the table a prime number.

## Quadratic probing
A variation to linear probing is **quadratic probing**, where on each rehashing iteration $i$ the rehash function's $jumpsize$ is equal to $i^2$. With each collision, the first rehash attempts to resolve it by going to $oldhashvalue + 1$. If that slot is also occupied then it tries $oldhashvalue + 4$, then $oldhashvalue + 9$, and so on until an empty slot is found.

## Chaining
A different method for resolving collisions that doesn't involve rehashing is to simply store multiple items in a table slot. Each occupied hash position will hold a collection of items such as a python list, and if a collision is found then we add the item to the collection at that slot. When searching for an item, first we must find the hash of the item, then search through the collection (if any) found at that hash slot. Depending on the nature and size of the data, we can use sorting and searching algorithms to potentially make the search faster.