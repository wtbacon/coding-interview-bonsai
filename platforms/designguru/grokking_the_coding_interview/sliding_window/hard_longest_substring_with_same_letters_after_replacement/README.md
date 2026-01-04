# Longest Substring with Same Letters after Replacement (TODO: Solve again)

- Pattern: Sliding Window

## Problem

Given a string with lowercase letters only, return the length of the longest substring containing the same letters if you're allowed to replace no more than `k` letters with any letter.

## Notes

- Time: $O(N)$
- Space: $O(1)$
  - the space complexity of the hash map is $O(26)$ because the English alphabet has at most 26 characters.
- Approach:
  1. Use the sliding window technique.
  2. Iterate through the string to expand the window, tracking the frequency of the most common character within it.
  3. If the number of characters that need to be replaced exceeds `k`, shrink the window from the left.
  4. Update the maximum length.
