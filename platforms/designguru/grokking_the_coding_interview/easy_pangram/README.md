# Pangram

- Pattern: Arrays, HashSet

## Problem (write in your words)

Given a string `sentence`, return `True` if it is Pangram, otherwise return `False`.

## Notes

- Time: O(n)
- Space: O(1)
  - The HashSet's maximum size is constant (at most 26 characters), the space complexity is O(1), meaning it is constant.
- Approach: Check whether each letter is alphabet and if so store it a set to track seen elements.
