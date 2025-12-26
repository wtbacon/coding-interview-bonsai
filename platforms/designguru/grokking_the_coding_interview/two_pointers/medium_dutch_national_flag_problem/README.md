# Dutch National Flag Problem (TODO: Solve again)

- Pattern: Two pointers(Three-Way Partition)

## Problem

Given an array `arr` containing 0s, 1s and 2s, sort the array in-place.
Treat numbers of the array as objects, and we can't count 0s, 1s, and 2s to recreate the array.

## Notes

- Time: $O(N)$
- Space: $O(1)$
- Approach: Use three pointers, where `next_0_idx` and `next_2_idx` act as boundaries for 0s and 2s, respectively.
  As the `i` pointer traverses the array in a single pass, it swaps elements into their correct zones, effectively "shrinking" the unsorted middle section until the entire array is partitioned.
