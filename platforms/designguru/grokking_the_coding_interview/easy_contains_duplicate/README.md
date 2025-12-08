# Contains Duplicate

- Pattern: Array, HashSet

## Problem

Given an integer array `nums`, return `True` if any value appears at least twice, otherwise return `False`.

## Notes

- Time: O(n)
  - On average, adding or checking elements in a `HashSet` has a time complexity of O(1) due to its underlying hash table structure.
- Space: O(n)
- Approach: Use a set to track seen elements.
  - In Python, `Set` is a hash-based set and `Dict` is a hash-based dictionary.
  - In general, `Set` is an abstract data type that only allows unique elements, regardless of how it's implemented. A set may be implemented using a balanced binary search tree.
    `HashSet` is a specific implementation of a Set that uses hashing.
