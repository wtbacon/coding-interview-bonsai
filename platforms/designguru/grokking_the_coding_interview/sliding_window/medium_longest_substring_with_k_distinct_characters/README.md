# Longest Substring with K Distinct Characters

- Pattern: Sliding Window

## Problem

Given a string `s` and an integer `k`, find the length of the longest substring that contains at most `k` distinct characters.

## Notes

- Time: $O(N)$
- Space: $O(k)$
- Approach:
  1. Initialize a sliding window using two pointers.
  2. Create a frequency map to keep track of character counts within the window.
  3. Iterate through the string, expanding the window by moving the right pointer and updating the frequency map.
  4. If the number of distinct characters exceeds `k`, shrink the window from the left by moving the left pointer and updating the frequency map accordingly.
  5. Keep track of the maximum length of the window that satisfies the condition.
