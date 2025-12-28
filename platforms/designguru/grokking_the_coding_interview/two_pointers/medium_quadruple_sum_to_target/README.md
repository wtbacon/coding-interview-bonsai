# Quadruple Sum to Target

- Pattern: Two pointers

## Problem

Given an unsorted integer array `arr` and a target number, identify and return all unique quadruplets in it, whose sum is equal to the target number.

## Notes

- Time: $O(N^3)$
  - Sort algorithm takes $O(N{log}N)$ and the triply-nested loop structure results in a $O(N^3)$ time complexity.
- Space: $O(1)$
- Approach: After sorting, the logic mirrors the Triplet Sum approach, extended by an additional outer loop.
