# Triplet Sum Close to Target

- Pattern: Two pointers

## Problem

Given an unsorted integer array `arr` and a target number, return a triplet in the array whose sum is as close to the target number as possible.
If there are more than one such triplet, return the sum of the triplet with smaller sum.

## Notes

- Time: $O(N^2)$
  - Sorting takes $O(N{log}N)$
  - THe outer loop runs N times, and the inner two-pointer search runs $O(N)$ times.
- Space: $O(1)$
- Approach: After an initial sort, we can iterate through the array and use two pointers to track the closest sum, breaking ties by selecting the smaller sum.
