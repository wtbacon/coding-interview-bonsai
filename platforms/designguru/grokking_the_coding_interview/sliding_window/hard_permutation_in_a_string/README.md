# Permutation in a String

- Pattern: Sliding Window

## Problem

Given a string and a pattern, return `True` if the string contains any permutation of the pattern.

## Notes

- Time: $O(N)$
- Space: $O(1)$
  - $O(1)$ assuming a fixed character set (like 26 letters).
- Approach:
  1. Iterate through the string using a fixed-size sliding window.
  2. Count the frequencies of each character in the pattern using a hashmap.
  3. During the iteration, increment the `matched` counter when the frequency target is met.
  4. Decrement the `matched` counter when the condition is no longer met.
  5. Return `True` when the `matched` counter equals the number of unique characters in the pattern.
