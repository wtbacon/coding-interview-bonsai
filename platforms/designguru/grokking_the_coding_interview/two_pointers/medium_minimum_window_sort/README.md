# Minimum Window Sort (TODO: solve again)

- Pattern: two pointer (out-of-order bounds)

## Problem

Given an integer array `arr`, return the length of the smallest sub-array in it which when sorted will sort the whole array.

## Notes

- Time: $O(N)$
- Space: $O(1)$
- Approach:
  1. Identify the initial "out-of-order" bounds.
  2. Find the Min/Mas in the sub-array.
  3. Expand the window to include "outliers".
  4. Calculate Length.
