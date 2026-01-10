# String Anagrams

- Pattern: Sliding Window

## Problem

Given a string and a pattern, return a list of starting indices of the anagrams of the pattern in the given string.

## Notes

- Time: $O(N+M)$
  - $O(N)$: $N$ is the length of the input string.
  - $O(M)$: $M$ is the length of the pattern.
- Space: $O(1)$
  - $O(1)$ assuming a fixed character set (like 26 letters).
- Approach:
  1. Iterate through the string using a fixed-size sliding window.
  2. Count the frequencies of each character in the pattern using a hashmap.
  3. During the iteration, increment the `matched` counter when the frequency target is met.
  4. Decrement the `matched` counter when the condition is no longer met.
  5. Append the starting window index when the `matched` counter equals the number of unique characters in the pattern.
