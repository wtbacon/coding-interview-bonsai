# Contains Duplicate

- Pattern: Arrays & Hashing

## Problem

Given an integer array `nums`, return `True` if any value appears at least twice, otherwise return `False`.

## Notes

- Time: O(n)
  - On average, adding or checking elements in a `HashSet` has a time complexity of O(1) due to its underlying hash table structure.
- Space: O(n)
- Approach: Use a set to track seen elements.
