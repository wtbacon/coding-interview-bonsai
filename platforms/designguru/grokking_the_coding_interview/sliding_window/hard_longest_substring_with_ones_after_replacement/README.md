# Longest Substring with Ones after Replacement

- Pattern: Sliding Window

## Problem

Given a binary list `arr` and an integer `k`, you can replace at most `k` '0's with '1's. Find the length of the longest substring that contains only '1's after performing the replacements.

## Notes

- Time: $O(N)$
- Space: $O(1)$
- Approach: Use a sliding window to track the longest substring with at most `k` zero replacements.