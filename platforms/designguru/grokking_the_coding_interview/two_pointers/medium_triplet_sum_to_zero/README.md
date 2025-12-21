# Triplet Sum to Zero (TODO: Solve again)

- Pattern: Two pointers

## Problem

Given an integer array of unsorted `nums`, return all unique triplets in that add up to zero.
The solution set must not contain duplicate triplets.
(The constraint is on the uniqueness of the triplets themselves, not the elements within them.)

## Notes

- Time: $O(N{log}N + N^2) = O(N^2)$
  - Sorting the array takes $O(N{log}N)$
  - Search for triplets that sum to 0 takes $O(N^2)$
- Space: $O(1)$
- Approach: After sorting, iterate through the array and use a two-pointer approach for the remaining two elements.
