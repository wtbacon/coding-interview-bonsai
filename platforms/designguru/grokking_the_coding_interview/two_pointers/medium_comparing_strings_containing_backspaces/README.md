# Comparing Strings containing Backspaces (TODO: Solve Again)

- Pattern: Two pointers (Iterating backwards)

## Problem

Given two strings containing backspaces (identified by the character `#`), check if the two strings are equal.

## Notes

- Time: $O(M+N)$
  - $M$ and $N$ are the lengths of the two respective strings.
- Space: $O(1)$
- Approach:
  1. Initialize two pointers at the last index of each string.
  2. Account for backspace using a counter for each string.
  3. When a `#` is encountered, increment the counter and move the pointer.
  4. If a regular character is found while `counter > 0`, bypass that character and decrement the counter.
  5. When both pointers land on valid(non-deleted) characters, compare them.
  6. Continue the pointer convergence until both strings are fully processed.
