# Permutation in a String

- Pattern: Sliding Window

## Problem

Given a string and a pattern, return `True` if the string contains any permutation of the pattern.

## Notes

- Time: $O(N)$
- Space: $O(1)$
- Approach:
  1. Iterate through the string using a sliding window.
  2. During the iteration, maintain a running count of character frequencies using a hashmap.
  3. Decrement the count for characters entering the window and increment for those leaving.
  4. If a character is not found in the pattern, reest of shift the window past that index.
  5. Return `True` when all frequency counts reach zero.
